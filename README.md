# Flask_parser
Этот репозиторий создан для выполнения тестового задания комапнии 
Авито (https://github.com/avito-tech/mi-backend-trainee-assignment)
на позицию стажера.
Для реализации был выбран Python 3.8.5. В качествефреймворка был выбрал Flask, 
а в качестве локальной базы данных была выбран SQLite.

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

Запуск тестового сервера с помощью Docker
------------------------
Для запуска тестовго сервера запустите команду:\
`docker-compose up`

После того как сервер запущен, на вашем тестовом компьютере войдите в браузер и
перейдите на ссылку\
http://localhost:5000




