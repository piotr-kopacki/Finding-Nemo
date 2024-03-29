
<h1 align="center">Finding-Nemo</h1>
<p align="center">My solution to STX Junior Python Develeper recruitment tasks.</p>


## Installation

Requires [Python](https://www.python.org/) 3.5+ to run.

Install the dependencies, apply migrations, optionally install fixtures and start the server.

```sh
$ cd .\Finding-Nemo\
$ pip install -r requirements.txt
$ python3 manage.py makemigrations
$ python3 manage.py migrate
$ python3 manage.py loaddata movies.json # Optional fixtures
$ python3 manage.py runserver
```

## Running with docker

 ```sh
$ cd .\Finding-Nemo\
$ docker build -t nemo .
$ docker run -p 8000:8000 -i -t nemo
```


## Running the tests

```sh
$ python3 manage.py test
```

## API Endpoints

`/movies/` - Returns all movies (paginated)  
`/movies/id/` - Returns details about a movie  
`/db/` - Loads a dataset from movielens
