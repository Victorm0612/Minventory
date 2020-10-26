# Minventory API

## Project Setup

Create a file called .env under the folder ProjectDs1, that file should contain:

```
DB_HOST=db
DB_PASSWORD=minventory123
DB_PORT=5432
DB_NAME=minventory_db
DB_USER=minventoryuser
```
The below configuration is used just for testing purposes and is not being used in production environments.

There are two ways to install and start the API, one of them with Docker and the other one without it.

### With Docker

```
docker-compose up
```

Then the API should be available on http://localhost:8000/

to stop the API run:

```
docker-compose down
```

### Without Docker

Keep in mind that this project uses PostgreSQL as DB so, you should have it installed (just in case that you are not using Docker).

Activate your virtual environment (the word api-env should be changed to the name of the virtual environment that you are currently using):

```
source api-env/bin/activate  # On Windows use `env\Scripts\activate`
```

In case you don't have the needed modules/dependencies needed run the next command (if you have pip3 as your default pip then use pip instead of pip3):

```
pip3 install -r requirements.txt
```

In case you don't have the latest DB changes then run the migrations (if you have python3 as your default pip then use python instead of python3):

```
python3 manage.py makemigrations && python3 manage.py migrate
```

now, you can start the API using this command:

```
python3 manage.py runserver 0.0.0.0:8000
```

Then the API should be available on http://localhost:8000/


## Developers
* [Arianny Jackeline Parra Janse - 1745205](https://github.com/AriannyJanse/) 
* [Jose Manuel Martinez Castillo - 1740895](https://github.com/jose0926/)
* [Juan Pablo Velasco Mellizo - 1766616](juan.mellizo@correounivalle.edu.co/)
* [Víctor Manuel Vargas Rojas - 1842274](https://github.com/Victorm0612/)
