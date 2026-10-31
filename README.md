# Casting Agency API

A REST API for a casting agency that manages movies, actors and which actors are cast in which movie. Access is controlled with Auth0 role-based access control (RBAC): every endpoint checks a permission inside the caller's JWT, and three roles get progressively more rights.

![Python](https://img.shields.io/badge/Python-3.8-yellow) ![Flask](https://img.shields.io/badge/Flask-REST%20API-black) ![Postgres](https://img.shields.io/badge/PostgreSQL-SQLAlchemy%20%2B%20Alembic-336791) ![Auth0](https://img.shields.io/badge/Auth0-RBAC%20%2F%20JWT-eb5424)

## Features

- CRUD for movies and actors, plus casting actors into movies (many-to-many)
- JWT validation against Auth0's JWKS (RS256), with permission checks per endpoint
- Database migrations with Flask-Migrate / Alembic
- 21 unit tests covering success and failure cases for every endpoint
- Postman collection for manual testing
- Gunicorn `Procfile` for deployment to a PaaS (originally deployed on Heroku)

## Data model

```
Movie (id, title, excerpt, release_date)
   │  1..*
MovieCast (id, movie_id, actor_id)   ── ON DELETE CASCADE on both sides
   │  *..1
Actor (id, name, age, gender, city, state, phone, email, website)
```

## Roles and permissions

| Permission | Casting Assistant | Casting Director | Executive Producer |
|------------|:-:|:-:|:-:|
| `get:movies`, `get:actors` | ✓ | ✓ | ✓ |
| `get:moviecasts` | | ✓ | ✓ |
| `post:actors`, `patch:actors`, `delete:actors` | | ✓ | ✓ |
| `patch:movies` | | ✓ | ✓ |
| `post:movies`, `delete:movies` | | | ✓ |
| `post:moviecasts` | | | ✓ |

## Endpoints

| Method | Path | Permission |
|--------|------|------------|
| GET | `/movies` | `get:movies` |
| GET | `/movies/<id>` | `get:movies` |
| POST | `/movies` | `post:movies` |
| PATCH | `/movies/<id>` | `patch:movies` |
| DELETE | `/movies/<id>` | `delete:movies` |
| GET | `/actors` | `get:actors` |
| GET | `/actors/<id>` | `get:actors` |
| POST | `/actors` | `post:actors` |
| PATCH | `/actors/<id>` | `patch:actors` |
| DELETE | `/actors/<id>` | `delete:actors` |
| GET | `/moviecasts` | `get:moviecasts` |
| POST | `/moviecasts` | `post:moviecasts` |

All responses are JSON with a `success` flag. Errors return JSON as well: `404`, `422`, and Auth0 errors (`401` missing/invalid token, `403` missing permission).

Example:

```bash
curl -H "Authorization: Bearer $TOKEN" http://localhost:5000/movies
```

```json
{
  "success": true,
  "movies": [
    { "id": 1, "title": "Example", "excerpt": "...", "release_date": "2020-05-01" }
  ]
}
```

## Run locally

```bash
python3 -m venv venv && source venv/bin/activate
pip install -r requirements.txt

createdb capstone
export DATABASE_URL=postgresql://<user>:<password>@localhost:5432/capstone

gunicorn app:app          # or: FLASK_APP=app.py flask run
```

Tables are created on startup, and Flask-Migrate is wired in for schema changes (`migrations/`). Auth0 settings (domain, audience `movie`, RS256) are configured at the top of `auth.py`. To call the API, create an Auth0 API with the permissions above, assign them to three roles, and log in as a user in each role to get a token.

## Tests

The test suite runs against a separate database seeded from `capstone_test.psql`. It authenticates with an Executive Producer token set in `test_app.py` (`self.mastertoken`); Auth0 tokens expire, so put a fresh one there before running.

```bash
createdb capstone_test
psql capstone_test < capstone_test.psql

export HEROKU_POSTGRESQL_BRONZE_URL=postgresql://<user>:<password>@localhost:5432/capstone_test
python test_app.py
```

The Postman collection (`Capstone Final Project.postman_collection.json`) checks each endpoint with the Casting Assistant, Casting Director and Executive Producer roles.

---

Built as the capstone project of the Udacity Full Stack Web Developer Nanodegree. Author: Ravshan Khudoyberdiev.
