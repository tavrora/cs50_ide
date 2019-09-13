import os
import datetime

from cs50 import SQL
from flask import Flask, flash, jsonify, redirect, render_template, request, session
from flask_session import Session
from tempfile import mkdtemp
from werkzeug.exceptions import default_exceptions, HTTPException, InternalServerError
from werkzeug.security import check_password_hash, generate_password_hash

from helpers import apology, login_required, lookup, usd

# Configure application
app = Flask(__name__)

# Ensure templates are auto-reloaded
app.config["TEMPLATES_AUTO_RELOAD"] = True


# Ensure responses aren't cached
@app.after_request
def after_request(response):
    response.headers["Cache-Control"] = "no-cache, no-store, must-revalidate"
    response.headers["Expires"] = 0
    response.headers["Pragma"] = "no-cache"
    return response


# Custom filter
app.jinja_env.filters["usd"] = usd

# Configure session to use filesystem (instead of signed cookies)
app.config["SESSION_FILE_DIR"] = mkdtemp()
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)

# Configure CS50 Library to use SQLite database
db = SQL("sqlite:///finance.db")

# Make sure API key is set
if not os.environ.get("API_KEY"):
    raise RuntimeError("API_KEY not set")


@app.route("/")
@login_required
def index():
    """Show portfolio of stocks"""

    # узнаём id авторизованного пользователя
    idSess = session['user_id']
    # print("ololo-index")            # ololo-index
    # print(idSess)                   # [{'id': 54}] регистрация, но 54 при авторизации!
    # ПОЧЕМУ ПРИ РЕГИСТРАЦИИ И ПРИ АВТОРИЗАЦИИ ID CЕССИИ ПРИХОДИТ В РАЗНОМ ФОРМАТЕ?????????? потому что я так передавала в методе регистарции )))
    # print(idSess[0]['id'])          # 54    # при авторизации такого элемента нет ("у числа нет индекса")

    # НО ЕСЛИ ЭТО РЕГИСТРАЦИЯ ТО id=idSess[0]['id'] 🐍
    # берём остаток кэша пользователя из таблицы Users
    userCash = db.execute("SELECT cash FROM users WHERE id = :id", id=idSess)
    # форматируем сумму функцией из хелпера
    userCashFormat = usd(userCash[0]['cash'])

    # ПРОВЕРКА - ЕСТЬ ЛИ ПОКУПКИ У ПОЛЬЗОВАТЕЛЯ - (ИНАЧЕ ОБРАЩЕНИЕ В БД ПО USER_ID, КОТОРОГО ТАМ НЕТ)
    allUserId = db.execute("SELECT DISTINCT user_id FROM portfolio_more")
    # print(allUserId)

    # ЕСЛИ ТАКОЙ ID УЖЕ ЕСТЬ В БД (Т.Е. ПОЛЬЗОВАТЕЛЬ УЖЕ ВЛАДЕЕТ АКЦИЯМИ - АВТОРИЗАЦИЯ), ОТОБРАЖАЕМ ИНФУ
    for any in allUserId:
        # print(any['user_id'])
        # print(idSess)
        if (any['user_id'] == idSess):
            # print("alohaha!-index")

            # делаем выборку всех пакетов акций и вычисляем количество акций в каждом пакете (скаладываем внутри пакета)
            symbShar = db.execute(
                # "SELECT DISTINCT symbol, SUM(shares) FROM portfolio_more GROUP BY symbol HAVING user_id = :user_id", user_id=idSess) # первый вариант - СЛОЖЕНИЕ РАБОТАЕТ НЕВЕРНО
                "SELECT DISTINCT symbol, SUM(shares) FROM portfolio_more GROUP BY symbol, user_id = :user_id HAVING user_id = :user_id", user_id=idSess)
            print(symbShar)
            # [{'symbol': 'abc', 'SUM(shares)': 5}, {'symbol': 'nflx', 'SUM(shares)': 3}]

            # # отладочный
            # viewSymbol=symbShar[0]['symbol']
            # print(viewSymbol)

            # заводим глобальный список для вывода данных в ЛК
            infoView = []
            # переменная для всех активов
            totalSum = 0
            # добавляем в этот список инофрмацию по каждому типу акции
            for i in symbShar:
                # ЕСЛИ КОЛИЧЕСТВО АКЦИЙ НЕ НОЛЬ
                if (int(i['SUM(shares)']) != 0):
                    print(i)
                    # заваодим словарь для каждого типа акции
                    infoViewLocal = {}
                    # добаляем символ акции в верхнем регистре
                    infoViewLocal.update({'symbol': i['symbol'].upper()})
                    # добавляем количество этой акции
                    infoViewLocal.update({'shares': i['SUM(shares)']})
                    # узнаём по API доп.данные по этой акции (наименование компании и текущую цену акции)
                    quote = lookup(i['symbol'])
                    # добавляем название компании, продающей акции
                    infoViewLocal.update({'name': quote['name']})
                    # добавляем текущую цену акции
                    infoViewLocal.update({'price': quote['price']})
                    # вычисляем и форматируем итоговую цену пакета данных акций
                    tot = i['SUM(shares)'] * quote['price']
                    total = usd(i['SUM(shares)'] * quote['price'])
                    # добавляем итоговую цену пакета данных акций
                    infoViewLocal.update({'total': total})

                    # добавляем полный словарь по данной акции в глобальный список
                    infoView.append(infoViewLocal)

                    # все активы = сумма всех акций + свободный кэш (меняется после add cash)
                    # totalSum = usd(int(userCash[0]['cash']) + i['SUM(shares)'] * quote['price'])  # СЧИТАЕТСЯ НЕВЕРНО
                    totalSum = totalSum + tot
                    # print(totalSum)

                # print(infoView)

            totalSum = usd(totalSum + float(userCash[0]['cash']))

            return render_template("index.html", infoView=infoView, userCashFormat=userCashFormat, totalSum=totalSum)

    # ИНАЧЕ ПРОСТО ОТОБРАЖАЕМ ИНДЕКС c кэшем и контрольной суммой (они совпадают, если нет акций)!
    return render_template("index.html", userCashFormat=userCashFormat, totalSum=userCashFormat)



@app.route("/buy", methods=["GET", "POST"])
@login_required
def buy():
    """Buy shares of stock"""

    if request.method == "GET":
        return render_template("buy.html")

    if request.method == "POST":

        symb = request.form.get("symbol")
        shar = request.form.get("shares")

        # Ensure symobl was submitted
        if not symb:
            return apology("must provide symbol", 400)

        # Ensure shares was submitted
        if not shar or not shar.isdigit() or float(shar) < 1 or float(shar)/int(shar) > 1:
            return apology("must provide shares", 400)

        quote = lookup(symb)
        # если акция не найдена
        if (quote == None):
            return apology("invalid symbol", 400)

        price = quote['price']
        # print(price)

        # смотрим, какой пользователь авторизован в данный момент
        idSess = session['user_id']
        # print(idSess)
        # print(symb)
        # print(shar)

        # смотрим, сколько денег у этого пользователя в наличии
        userCash = db.execute("SELECT cash FROM users WHERE id = :id", id=idSess)
        # print(userCash)
        # print(userCash[0]['cash'])

        # если денег не хватает, извиняемся
        if (float(userCash[0]['cash']) < price * int(shar)):
            return apology("insufficient funds", 403)

        # если денег хватает, покупаем акции
        if (float(userCash[0]['cash']) >= price * int(shar)):
            # print("todo")

            # # добавляем запись в портфель пользователя (в новую таблицу)
            # # проверяем по БД есть ли уже у данного пользователя такие акции
            # userPortfolio = db.execute("SELECT user_id, symbol FROM portfolio WHERE user_id = :user_id AND symbol = :symbol", user_id=idSess, symbol=symb)
            # print(userPortfolio)
            # print(len(userPortfolio))

            # # если такой акции у пользователя еще нет, то добавляем новую строку
            # if (len(userPortfolio) == 0):
            #     print("aloha")
            #     db.execute("INSERT INTO portfolio ('id', 'user_id', 'symbol', 'shares') VALUES (NULL, :user_id, :symbol, :shares)", user_id=idSess, symbol=symb, shares=shar)

            # # если такая акция у пользоавтеля уже есть, просто меняем количество
            # intShar = int(shar)
            # print(intShar)
            # db.execute("UPDATE portfolio SET shares = shares + :intShar WHERE user_id = :user_id AND symbol = :symbol", intShar=intShar, user_id=idSess, symbol=symb)

            # ВАРИАНТ С PORTFOLIO_MORE (каждая покупка = новая запись в БД с текущими датой и ценой)
            db.execute("INSERT INTO portfolio_more ('id', 'user_id', 'symbol', 'shares', 'price', 'date') VALUES (NULL, :user_id, :symbol, :shares, :price, :date)",
                       user_id=idSess, symbol=symb.upper(), shares=shar, price=price, date=datetime.datetime.now())

            # вычитаем потраченную сумму из кэша
            cost = price * int(shar)
            db.execute("UPDATE users SET cash = cash - :cost WHERE id = :id", cost=cost, id=idSess)

        # отображаем страницу с покупками пользователя
        return redirect("/")


@app.route("/check", methods=["GET"])
def check():
    """Return true if username available, else false, in JSON format"""

    # Взять список всех имен пользователей из БД
    usernamesAll = db.execute("SELECT username FROM users")

    name = request.args.get("username")
    if len(name) >= 1:
        # Убедитесь, что такого же имени пользователя нет в БД
        for username in usernamesAll:
            if username['username'] == name:
                return jsonify(False)
        return jsonify(True)

    return jsonify(False)


@app.route("/history")
@login_required
def history():
    """Show history of transactions"""

    # узнаём id авторизованного пользователя
    idSess = session['user_id']
    # print(idSess)

    # надо, чтобы была хотя бы одна запись в portfolio_more
    # добавить проверку на то что строки для авторизованного пользователя уже есть (совершал покупки)!
    allPortUser = db.execute("SELECT DISTINCT user_id FROM portfolio_more")
    # print(allPortUser)

    # формируем список user_id, которые есть в таблице portfolio_more
    listPortUser = []
    for portUser in allPortUser:
        listPortUser.append(portUser['user_id'])
    # print(listPortUser)

    # если у пользователя уже были покупки, то отображаем (выпадающей список Sell и History тоже)
    for i in listPortUser:
        # print("eachhhh")
        # print(i)
        if i == idSess:

            historyUser = db.execute(
                "SELECT symbol, shares, price, date FROM portfolio_more WHERE user_id=:user_id", user_id=idSess)
            print(historyUser)

            return render_template("history.html", historyUser=historyUser)

    else:
        # print("rrr :((")
        return render_template("history.html")


@app.route("/login", methods=["GET", "POST"])
def login():
    """Log user in"""

    # Forget any user_id
    session.clear()

    # User reached route via POST (as by submitting a form via POST)
    if request.method == "POST":

        # Ensure username was submitted
        if not request.form.get("username"):
            return apology("must provide username", 403)

        # Ensure password was submitted
        elif not request.form.get("password"):
            return apology("must provide password", 403)

        # Query database for username
        rows = db.execute("SELECT * FROM users WHERE username = :username",
                          username=request.form.get("username"))

        # print("olol-login")
        # print(rows)

        # Ensure username exists and password is correct
        if len(rows) != 1 or not check_password_hash(rows[0]["hash"], request.form.get("password")):
            return apology("invalid username and/or password", 403)

        # Remember which user has logged in
        session["user_id"] = rows[0]["id"]

        # print(rows[0]["id"])

        # Redirect user to home page
        return redirect("/")

    # User reached route via GET (as by clicking a link or via redirect)
    else:
        return render_template("login.html")


@app.route("/logout")
def logout():
    """Log user out"""

    # Forget any user_id
    session.clear()

    # Redirect user to login form
    return redirect("/")


@app.route("/quote", methods=["GET", "POST"])
@login_required
def quote():
    """Get stock quote."""

    if request.method == "GET":
        return render_template("quote.html")

    if request.method == "POST":
        quote = lookup(request.form.get("symbol"))
        # если акция не найдена
        if (quote == None):
            return apology("invalid symbol", 400)
        # если акция найдена
        else:
            return render_template("quote_info.html", name=quote['name'], price=quote['price'], symbol=quote['symbol'])


@app.route("/register", methods=["GET", "POST"])
def register():
    """Register user"""

    # Забыть предыдущих пользователей
    session.clear()

    # Пользователь достиг маршрута через POST (например, отправив форму через POST)
    if request.method == "POST":

        # Взять список всех имен пользователей из БД
        usernamesAll = db.execute("SELECT username FROM users")
        # print(usernamesAll)

        # Убедитесь, что имя пользователя отправлено
        if not request.form.get("username"):
            return apology("must provide username", 400)

        # Убедитесь, что пароль отправлен
        elif not request.form.get("password"):
            return apology("must provide password", 400)

        # Убедитесь, что подтверждение пароля отправлено
        elif not request.form.get("confirmation"):
            return apology("must provide password confirmation", 400)

        # Убедитесь, что пароль и подтверждение совпадают
        elif not request.form.get("password") == request.form.get("confirmation"):
            return apology("must match password and confirmation", 400)

        # Убедитесь, что такого же имени пользователя нет в БД (ЗАЩИТА ОТ ОТКЛЮЧЕНИЯ JS НА КЛИЕНТЕ)
        for username in usernamesAll:
            if username['username'] == request.form.get("username"):
                return apology("username must be unique", 400)

        # Хешировать пароль, чтобы положить хэш в БД
        hash = generate_password_hash(request.form.get("password"))

        # Добвить пользователя в БД с защитой от атак sql-инъекций (id - автоинкремент)
        db.execute("INSERT INTO users ('id', 'username', 'hash', 'cash') VALUES (NULL, :username, :hash, '10000.00')",
                   username=request.form.get("username"), hash=hash)

        # Взять id нового пользователя из БД
        userId = db.execute("SELECT id FROM users WHERE username = :username", username=request.form.get("username"))

        # Помните, какой пользователь находится в системе (ЧТО ТАКОЕ user_id?) userId[0]['id']
        # ЗАПОМИНАЕМ ЧИСЛО, А НЕ МАССИВ С ЧИСЛОМ! 🐞
        session["user_id"] = userId[0]['id']
        print("olol-regist")
        print(userId)

        # Redirect user to home page
        return redirect("/")

    # Пользователь достиг маршрута через GET (например, нажав ссылку или перенаправление)
    else:
        return render_template("register.html")


@app.route("/sell", methods=["GET", "POST"])
@login_required
def sell():
    """Sell shares of stock"""

    # узнаём id авторизованного пользователя
    idSess = session['user_id']
    # print("olol-sell")
    # print(idSess)

    # надо, чтобы была хотя бы одна запись в portfolio_more
    # добавить проверку на то что строки для авторизованного пользователя уже есть (совершал покупки)!
    allPortUser = db.execute("SELECT DISTINCT user_id FROM portfolio_more")
    # print(allPortUser)

    # формируем список user_id, которые есть в таблице portfolio_more
    listPortUser = []
    for portUser in allPortUser:
        listPortUser.append(portUser['user_id'])
    # print(listPortUser)

    # если у пользователя уже были покупки, то отображаем (выпадающей список Sell и History тоже)
    for i in listPortUser:
        # print("hahah")
        # print(i)
        if i == idSess:
            # print("popopop")

            # делаем выборку всех пакетов акций
            symbAll = db.execute("SELECT DISTINCT symbol FROM portfolio_more WHERE user_id = :user_id", user_id=idSess)
            # print(symbAll)

            # заносим названия в верхнем регистре в список
            symbAllUpper = []
            for symbEach in symbAll:
                symbAllUpper.append(symbEach['symbol'].upper())
            # print(symbAllUpper)

            if request.method == "POST":

                symb = request.form.get("symbol")
                shar = request.form.get("shares")

                # проверка пользовательского ввода
                if not request.form.get("symbol"):
                    return apology("must provide symbol", 400)

                if not shar or not shar.isdigit() or float(shar) < 1 or float(shar)/int(shar) > 1:
                    return apology("must provide shares", 400)

                symb = request.form.get("symbol").upper()     # нельзя перевести в верхний регистр пустоту
                # print(symb)

                # проверяем, что у пользователя есть акция, которую он хочет продать
                for s in symbAllUpper:
                    if s == symb:
                        # если есть, проверяем, что количество акций в пакете больше или равно заявленному для продажи
                        # РЕГИСТР НАЗВАНИЯ АКЦИИ В БД (ЗАНОСИТСЯ В ВЕРХНЕМ, ПРОВЕРЯЕТСЯ В ВЕРХНЕМ - для занесенных в нижнем уже не сработает!...)
                        quantitySymb = db.execute(
                            "SELECT SUM(shares) FROM portfolio_more GROUP BY symbol HAVING user_id = :user_id AND symbol=:symbol", user_id=idSess, symbol=symb)
                        # print(quantitySymb)
                        # print(quantitySymb[0]['SUM(shares)'])

                        if quantitySymb[0]['SUM(shares)'] >= int(shar):
                            # совершаем продажу и выходим из цикла
                            # print("sell :)))")

                            # узнаём текущую цену акции
                            quote = lookup(symb)
                            quantitySell = int(shar) * (-1)

                            # вставляем в таблицу покупок (portfolo_more) строку с отрицательным количеством акции, равным количеству проданных акций, + дата, текущая цена и т.д.
                            db.execute("INSERT INTO portfolio_more ('id', 'user_id', 'symbol', 'shares', 'price', 'date') VALUES (NULL, :user_id, :symbol, :shares, :price, :date)",
                                       user_id=idSess, symbol=symb, shares=quantitySell, price=quote['price'], date=datetime.datetime.now())

                            # добавила в index проверку - отображть, если не ноль

                            # обновляем кэш пользователя (добавляем выручку с продажи акций)
                            # выручка = текущая цена * количество проданных
                            costSell = quote['price'] * int(shar)
                            print(costSell)
                            db.execute("UPDATE users SET cash = cash + :costSell WHERE id = :id", costSell=costSell, id=idSess)

                            # отображаем страницу с покупками пользователя
                            return redirect("/")

                        else:
                            # извиняемся
                            return apology("not enough shares in the package", 400)

            else:
                return render_template("sell.html", symbAllUpper=symbAllUpper)

    else:
        # print("bad :(((")
        return render_template("sell.html")


@app.route("/cash", methods=["GET", "POST"])
@login_required
def cash():
    """Get stock quote."""

    # узнаём id авторизованного пользователя
    idSess = session['user_id']
    # print("lololo")
    # print(idSess)
    # print(idSess[0]['id'])

    if request.method == "GET":
        return render_template("cash.html")

    if request.method == "POST":

        # проверка пользовательского ввода
        if not request.form.get("cash"):
            return apology("must provide cash", 400)

        cashAdd = request.form.get("cash")

        if cashAdd.isdigit():
            cashNew = int(request.form.get("cash"))
            db.execute("UPDATE users SET cash = cash + :cashNew WHERE id = :id", cashNew=cashNew, id=idSess)
            return redirect("/")

        else:
            return apology("must provide cash (int)", 400)


def errorhandler(e):
    """Handle error"""
    if not isinstance(e, HTTPException):
        e = InternalServerError()
    return apology(e.name, e.code)


# Listen for errors
for code in default_exceptions:
    app.errorhandler(code)(errorhandler)