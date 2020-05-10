# Full Stack Trivia API Backend

## Getting Started

The API for a Movie Agency is up and running at the following base URL: https://movie-agency-api.herokuapp.com/ without a frontend.
All the endpoints will be mentioned later. Please see the installation instructions below.

### Installing Dependencies

#### Python 3.8

Follow instructions to install the latest version of python for your platform in the [python docs](https://docs.python.org/3/using/unix.html#getting-and-installing-the-latest-version-of-python)

#### Virtual Enviornment

We recommend working within a virtual environment whenever using Python for projects. This keeps your dependencies for each project separate and organaized. Instructions for setting up a virual enviornment for your platform can be found in the [python docs](https://packaging.python.org/guides/installing-using-pip-and-virtual-environments/). Once you install a virtual environment create and run a virtual environment within the `/backend` folder.

```bash
virtualenv env
source env/Scripts/activate
```

#### PIP Dependencies

Once you have your virtual environment setup and running, install dependencies by running:

```bash
pip install -r requirements.txt
```

This will install all of the required packages we selected within the `requirements.txt` file.


## Database Setup
Right now, the project is configured to be communicating with the Heroku databases so you would need to create your own database and configure the connection using the following guide:
Create a database called `capstone`:
```bash
createdb capstone
```

Now, make sure that your Postgres user and password credentials are correct in `database_path` on line 7 of [`models.py`](./models.py)


Finally, run flask upgrade to automatically set up the database tables and relations:
```bash
flask db upgrade
```

## Setting up CORS

On line 27 of [`__init__.py`](./flaskr/__init__.py) you would need to update the origins URL to the one where your website URL will be located, so that CORS policy won't block front website from accessing data from the API.

## Running the server

From within the `backend` directory first ensure you are working using your created virtual environment.

To run the server, execute:

```bash
export FLASK_APP=app
export FLASK_ENV=development
flask run
```

At this point, your API endpoint is running and ready to receive queries.

## Testing
To make sure that the API is working, you would need to run tests. There are two available testing options in this project:

1. You can import `Capstone Final Project.postman_collection.json` collection file into your Postman and simply run the tests. All the necessary variables to test the API should be inside of the file.

2. You can also run Unit Tests. For that, first, you would need to create a testing database and import a dump contained in `capstone_test.psql`:

```
createdb capstone_test
psql capstone_test < capstone_test.psql
```

Then, you would need to update the `database_path` on line 19 of [`test_app.py`](./test_app.py) with your database connection settings.
Finally, use the following terminal command to run the tests:

```
python test_app.py
```
After running all the commands you should see that all tests were successfully run. If not, you must have missed something on your way to running the backend.

## API Documentation

### `Authorization`

You would need 3 different role JWT Tokens to be able to authenticate to an API. Pass them along as an Authorization Bearer Tokens.
##### Casting Assistant JWT
```
eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6IkcxY0oySW1yY1RmejJKWmY0QlFJTyJ9.eyJpc3MiOiJodHRwczovL3Jvbi1mbnNkLmF1dGgwLmNvbS8iLCJzdWIiOiJhdXRoMHw1ZWFmMGE5NDZiNjliYzBjMTJmMDdkNWEiLCJhdWQiOiJtb3ZpZSIsImlhdCI6MTU4OTEzMDQ0NSwiZXhwIjoxNTg5MjE2ODQ1LCJhenAiOiJQVDl4UnRsN1RmYUtYMDlQRG0ycUpTRllvVmxYRERYSCIsInNjb3BlIjoiIiwicGVybWlzc2lvbnMiOlsiZ2V0OmFjdG9ycyIsImdldDptb3ZpZXMiXX0.KtIRSXoAQmJqyjWb5fWfNFHzVL27ZUnmpDNHyLIXFt_ynYo8oPDXrxX1x1bALYMJjdlk8bpMC2LP9-WWjuZn-mtUn4gyveUqlYcto1RAwH4yX58Ubrg_xZGHN1KDXGuqlx5c5C9223v4JGSy_dY14rvRiUUNkMGIv1a61YnB0Ab5T9AmdqtipDdEeBSCz3sdI8TDQV2kW5k8hg0dh1yGgsyfjl_pudh_UIIjt-6aOsj6EvtRzTX0vat-_FckR01KCdgwYwCS5EZKqC52kPurFZRusFlYW0gR7PmWcsSSJJR7V8YP7VzYITqwMhrWhT62Ekl-nI52jQ_oo3PYPG3_Yw
```
##### Casting Director JWT
```
eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6IkcxY0oySW1yY1RmejJKWmY0QlFJTyJ9.eyJpc3MiOiJodHRwczovL3Jvbi1mbnNkLmF1dGgwLmNvbS8iLCJzdWIiOiJhdXRoMHw1ZWFmMGFkZTU0YjE0YzBjMTI3MjQyMDUiLCJhdWQiOiJtb3ZpZSIsImlhdCI6MTU4OTEzMDM3NywiZXhwIjoxNTg5MjE2Nzc3LCJhenAiOiJQVDl4UnRsN1RmYUtYMDlQRG0ycUpTRllvVmxYRERYSCIsInNjb3BlIjoiIiwicGVybWlzc2lvbnMiOlsiZGVsZXRlOmFjdG9ycyIsImdldDphY3RvcnMiLCJnZXQ6bW92aWVjYXN0cyIsImdldDptb3ZpZXMiLCJwYXRjaDphY3RvcnMiLCJwYXRjaDptb3ZpZXMiLCJwb3N0OmFjdG9ycyJdfQ.VacDS8DDAsjvwx448axJJPWUrkhp0W8ds105omrGPig5hZWriz4VOViG1b-XUznKqXmp5lrN-QfYYetV4uqhEHQWiOXmCU4qxqhIWaxo2JXMtR_1AJygvgxr9kvKrTAG1_94H0HNaQUmhsrQcTDgrInxKkCUQ1D3i3a5AxBNYU-njC07Uk4WakrYOiCEx3fBUH8pmxzt2UMkgTDxfdgAk57OCnclCDSDa3lNyKl7G0eoMbSZqpAHapIY2bjkoakvhqzhMZtcpGSGcf5Sf9You7uedaq7MNfvIcxXMZQgH0U-SK6A4BL1FbNuky9MDQnFHEqc_glkqSu7ZzumAXwkgA
```
##### Executive Producer JWT
```
eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6IkcxY0oySW1yY1RmejJKWmY0QlFJTyJ9.eyJpc3MiOiJodHRwczovL3Jvbi1mbnNkLmF1dGgwLmNvbS8iLCJzdWIiOiJhdXRoMHw1ZWI2YmZhNjZiNjliYzBjMTIwNzMyNWYiLCJhdWQiOiJtb3ZpZSIsImlhdCI6MTU4OTEzMDIyOCwiZXhwIjoxNTg5MjE2NjI4LCJhenAiOiJQVDl4UnRsN1RmYUtYMDlQRG0ycUpTRllvVmxYRERYSCIsInNjb3BlIjoiIiwicGVybWlzc2lvbnMiOlsiZGVsZXRlOmFjdG9ycyIsImRlbGV0ZTptb3ZpZXMiLCJnZXQ6YWN0b3JzIiwiZ2V0Om1vdmllY2FzdHMiLCJnZXQ6bW92aWVzIiwicGF0Y2g6YWN0b3JzIiwicGF0Y2g6bW92aWVzIiwicG9zdDphY3RvcnMiLCJwb3N0Om1vdmllY2FzdHMiLCJwb3N0Om1vdmllcyJdfQ.bIxnaPnnRK2LOGXXp_yTqM9_qTisXPWdbSqq59QHexrpsM7AeLwlLI8Zq6hQ-kkxITHTW0grGvOwolu35DvSBI40SBfh3Hj0t4jPWJ8V6EAaX9NYUbDL0imj_xI2jJUl_mxCLEREqEgnjHjZNnKOtaBc4UmoUHWDL_NRaMQ7xCS30EU7J-iEAHbI_5ziu4TnW-9bhrG9AIn8U6BadYt-fNP0pz1BkpV0J-n4rjv2-gv49l4C_I5GMuVszJjpygfH-LwF_174hdo-Qe5zIX7Jfhj-LoIZGHs0Z2XYYXzU0pSS8TfPmEV5JqiOf27B2zYUPxmn066S6znw6rD7M56yTg
```
### `All Endpoints`
1. `GET /movies`
2. `GET /movies/<int:movie_id>`
3. `POST /movies`
4. `PATCH /movies/<int:movie_id>`
5. `DELETE /movies/<int:movie_id>`
6. `GET /actors`
7. `GET /actors/<int:actor_id>`
8. `POST /actors`
9. `PATCH /actors/<int:actor_id>`
10. `DELETE /actors/<int:movie_id>`
11. `GET /moviecasts`
12. `POST /moviecasts`

### `GET /movies`

Returns an array of all the movies.

##### Response
```
{
    "movies": [
        {
            "excerpt": "Abou",
            "id": 25,
            "release_date": "Thu, 08 Oct 2020 00:00:00 GMT",
            "title": "Wat"
        },
        {
            "excerpt": null,
            "id": 27,
            "release_date": "Thu, 08 Oct 2020 00:00:00 GMT",
            "title": "Wataaa"
        }
    ],
    "success": true
}
```

### `GET /movies/<int:movie_id>`

Gets a specific movie information.

##### Response
```
{
    "movie": [
        {
            "excerpt": null,
            "id": 27,
            "release_date": "Thu, 08 Oct 2020 00:00:00 GMT",
            "title": "Wataaa"
        }
    ],
    "success": true
}
```

### `POST /movies`

Creates a new movie with the given details as part of the body.

##### Arguments


```
{
    "title": "Wat",
    "excerpt": "Abou",
    "release_date": "2020-10-08"
}
```

##### Response

```
{
    "id": 28,
    "success": true
}
```

### `PATCH /movies/<int:movie_id>`

Updates a specific movie information with the given details as part of the body.

##### Arguments


```
{
    "title": "Wataaa",
    "release_date": "2020-10-08"
}
```

##### Response

```
{
    "movie": 28,
    "success": true
}
```

### `DELETE /movies/<int:movie_id>`

Deletes a specific movie.

##### Response
```
{
    "delete": 28,
    "success": true
}
```

### `GET /actors`

Returns an array of all the actors.

##### Response
```
{
    "actors": [
        {
            "age": 29,
            "city": "Boston",
            "email": "rkhudoyber@gm.com",
            "gender": "Male",
            "id": 22,
            "name": "Ron",
            "phone": "123456",
            "state": "MA",
            "website": "wwwwww"
        },
        {
            "age": 29,
            "city": "Boston",
            "email": "rkhudoyber@gm.com",
            "gender": "Male",
            "id": 25,
            "name": "Ron",
            "phone": "123456",
            "state": "MA",
            "website": "wwwwww"
        }
    ],
    "success": true
}
```

### `GET /actors/<int:actor_id>`

Gets a specific actor information.

##### Response
```
{
    "actor": [
        {
            "age": 29,
            "city": "Boston",
            "email": "rkhudoyber@gm.com",
            "gender": "Male",
            "id": 25,
            "name": "Ron",
            "phone": "123456",
            "state": "MA",
            "website": "wwwwww"
        }
    ],
    "success": true
}
```

### `POST /actors`

Creates a new actor with the given details as part of the body.

##### Arguments

```
{
    "name": "Ron",
    "age": 29,
    "gender": "Male",
    "city": "Boston",
    "state": "MA",
    "phone": "123456",
    "email": "rkhudoyber@gm.com",
    "website": "wwwwww"
}
```

##### Response

```
{
    "id": 26,
    "success": true
}
```

### `PATCH /actors/<int:actor_id>`

Updates a specific actor information with the given details as part of the body.

##### Arguments


```
{
    "name": "Ron",
    "age": 29,
    "gender": "Male",
    "city": "Boston",
    "state": "MA",
    "phone": "123456"
}
```

##### Response

```
{
    "actor": 26,
    "success": true
}
```

### `DELETE /actors/<int:actor_id>`

Deletes a specific actor.

##### Response
```
{
    "delete": 28,
    "success": true
}
```

### `GET /moviecasts`

Returns an array of all the movies with the assigned actors.

##### Response
```
{
    "moviecasts": [
        {
            "actors": [
                {
                    "age": 29,
                    "city": "Boston",
                    "email": "rkhudoyber@gm.com",
                    "gender": "Male",
                    "id": 27,
                    "name": "Ron",
                    "phone": "123456",
                    "state": "MA",
                    "website": "wwwwww"
                }
            ],
            "excerpt": "Abou",
            "id": 29,
            "release_date": "Thu, 08 Oct 2020 00:00:00 GMT",
            "title": "Wat"
        }
    ],
    "success": true
}
```


### `POST /moviecasts`

Creates a new moviecast by assigning an actor to the movie.

##### Arguments


```
{
	"actor_id": 2,
	"movie_id": 3
}
```

##### Response

```
{
    "actor_id": 2,
    "movie_id": 3,
    "success": true
}
```


### Errors

##### `422 - Unprocessable`

Response
```
{
    "success": False,
    "error": 422,
    "message": "Unprocessable data, please check your data"
}
```

##### `404 - Resource not found`

Response
```
{
    "success": False,
    "error": 404,
    "message": "Resource you are trying to modify is not found"
}
```

##### `401 - Authorization Error`

Response
```
{
    "success": False,
    "error": 401,
    "message": "Authorization header is expected"
}
```

##### `403 - Not enough permissions`

Response
```
{
    "success": False,
    "error": 403,
    "message": "You do not have enough permissions to perform this operation"
}
```