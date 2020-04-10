# Softalaproject repo for automated fridge management app
The application is containerized with Docker. 

The build is done with Django and Node. 

Project uses SQLite for the database.

## SW requirements:
Git bash (if you're using Windows): https://gitforwindows.org/

Docker or Python3.

## Start server:


Locally using python;

1. Start server

	python manage.py runserver

2. Open localhost or http://127.0.0.1/ on your host machine.

3. To stop hosting the server use ctrl + c in the python console window.

Starting with Docker-compose;

1. Build Docker image:

	docker-compose build

2. Start application:

	docker-compose up -d

3. Stop using application

	docker-compose down

Starting with Docker (container)

1. Build container

	docker build -t djangoapp .

2. Run container 

	docker container run -p 8000:8000 --name djangoapp djangoapp

3. To stop container ctrl + c
