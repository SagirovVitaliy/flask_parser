# Flask_parser
Этот репозиторий создан для выполнения тестового задания комапнии 
Авито (https://github.com/avito-tech/mi-backend-trainee-assignment)
на позицию стажера.
Для реализации был выбран Python 3.8.5, в качестве фреймворка Flask, 
а в качестве локальной базы данных SQLite, для сбора данных по расписанию 
Celery в связке с Redis, для тестов Pytest.

Для любого сценария использования необходимо: 
---------------------------
Клонировать репозиторий:\
`git clone https://github.com/SagirovVitaliy/flask_parser.git`

Создать виртуальное окружение:\
`python3 -m venv env`

Активировать виртуальное окружение:\
`source env/bin/activate`

Запуск тестового сервера
------------------------
Устоновите зависимости:\
`pip install -r requirements.txt`

Из папки-корня проекта (это папка где лежит этот README.md) запустите команду:\
`./run.sh`

После того как сервер запущен, на вашем тестовом компьютере войдите в браузер и
перейдите на ссылку\
http://localhost:5000

Для запуска Celery запустите команду (нужно открыть ещё один терминал):\
`celery -A tasks_parser worker -B --loglevel=INFO`

Так как вы запускаете Celery вне Docker не забудьте поменять в tasks_parser.py:\
`broker='redis://redis:6379/0'` на `broker='redis://localhost:6379/0'`

Запуск тестового сервера с помощью Docker
------------------------
Для запуска тестовго сервера запустите команду:\
`docker-compose up`

После того как сервер запущен, на вашем тестовом компьютере войдите в браузер и
перейдите на ссылку\
http://localhost:5000

Запуск тестов
------------------------
Для запуска тестов запустите команду:\
`pytest`

Для опредения покрытия тестами приложения запустите команду:\
`pytest --cov=webapp`


