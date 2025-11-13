Task Manager — Django + Docker
Простой и удобный Task Manager API, построенный на **Django**, с поддержкой **PostgreSQL**, **Docker**, контейнеризацией и возможностью быстрого развёртывания на любом сервере.

Функциональность

 CRUD операции для задач
 Состояние задачи (в работе, выполнено)
 Админ-панель Django
 Взаимодействие через API
 Полная контейнеризация (Docker + Docker Compose)
 PostgreSQL как основная база данных

 Стек технологий
 **Python 3.11**
 **Django**
 **Gunicorn**
 **PostgreSQL**
 **Docker / Docker Compose**

Установка и запуск локально (без Docker)

git clone https://github.com/Kylychbek03/taskmanager_django.git
cd taskmanager_django

pip install -r requirements.txt
python manage.py migrate
python manage.py runserver
