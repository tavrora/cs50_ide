import cs50
import csv

from flask import Flask, jsonify, redirect, render_template, request

# Configure application
app = Flask(__name__)

# Reload templates when they are changed
app.config["TEMPLATES_AUTO_RELOAD"] = True


@app.after_request
def after_request(response):
    """Disable caching"""
    response.headers["Cache-Control"] = "no-cache, no-store, must-revalidate"
    response.headers["Expires"] = 0
    response.headers["Pragma"] = "no-cache"
    return response


@app.route("/", methods=["GET"])
def get_index():
    return redirect("/form")


@app.route("/form", methods=["GET"])
def get_form():
    return render_template("form.html")


@app.route("/form", methods=["POST"])
def post_form():
    # (в скобках значения атрибута "name"?)
    firstname = request.form.get("firstname")     # это серверная проверка пустоты формы на случай отключения js
    lastname = request.form.get("lastname")
    password = request.form.get("password")     # проверка только на бэке
    if not firstname or not lastname or not password:
        return render_template("error.html", message="Вы, хитрец, отключили js и не заполнили имя или пароль (или просто не заполнили пароль). Пожалуйста, заполните указанные поля")

    # в случае валидных данных (заполнены имя и пароль) - сохраняем данные в файле csv
    # и переводим пользователя на таблицу просмотра данных

    with open("survey.csv", "a") as file:
        writer = csv.writer(file)
        writer.writerow((request.form.get("firstname"), request.form.get("lastname"),
                         request.form.get("email"), request.form.get("password"),
                         request.form.get("text")))

    return redirect("/sheet")


@app.route("/sheet", methods=["GET"])
def get_sheet():
    with open("survey.csv", "r") as file:
        reader = csv.reader(file)
        respondents = list(reader)
    return render_template("sheet.html", respondents=respondents)
