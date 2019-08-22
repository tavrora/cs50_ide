<?php

$result = mail("test@test.ru","Анкета сайта","С сайта была получена анкета с такими данными: 
\nИмя: $_POST[name]
\nПароль: $_POST[password]
Испытывает ли восторг от изучения программирования: $_POST[vostorg]
Что изучает 
HTML: $_POST[html], CSS: $_POST[css], SQL: $_POST[sql], Командная строка $_POST[commandline], Python: $_POST[python]
Сколько вермени в день уделяет обучению: $_POST[lerns]
Сколько часов в день спит: $_POST[sleep] часов
Советы по изучению программирования: $_POST[text]");

if ($result) 
{
	echo "<p>Сообщение отправлено успешно!</p>";
} 
else 
{
	echo "<p>Сообщение не отправлено!</p>";
}

?>