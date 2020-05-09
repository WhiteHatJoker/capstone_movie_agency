from flask import Flask, jsonify, abort, request
from flask_cors import CORS

from models import setup_db, MovieCast, Movie, Actor, db_drop_and_create_all
from auth import AuthError, requires_auth




def create_app(test_config=None):
# create and configure the app

    app = Flask(__name__)
    db = setup_db(app)

    CORS(app)

    db_drop_and_create_all()

    '''
    Movies
    ---------------------------------------------------------------------------------
    '''


    # Get information about all movies
    @app.route('/movies')
    @requires_auth('get:movies')
    def get_movies(payload):
        all_movies = Movie.query.all()
        if all_movies:
            movies = [movie.long() for movie in all_movies]
            return jsonify({
                'success': True,
                'movies': movies
            })
        else:
            abort(404)


    # Get individual movie information
    @app.route('/movies/<int:movie_id>')
    @requires_auth('get:movies')
    def get_movie(payload, movie_id):
        movie = Movie.query.filter_by(id=movie_id).one_or_none()
        if movie:
            return jsonify({
                'success': True,
                'movie': [movie.long()]
            })
        else:
            abort(404)


    # Create a movie
    @app.route('/movies/', methods=['POST'])
    @requires_auth('post:movies')
    def create_movie(payload):
        try:
            data = request.get_json()
            if not('title' in data and 'release_date' in data):
                abort(422)

            movie = Movie(
                title=data.get('title', None),
                excerpt=data.get('excerpt', None),
                release_date=data.get('release_date', None)
            )
            db.session.add(movie)
            db.session.commit()
            return jsonify({
                'success': True
            })
        except:
            abort(422)


    # Update a movie information
    @app.route('/movies/<int:movie_id>', methods=['PATCH'])
    @requires_auth('patch:movies')
    def update_movie(payload, movie_id):
        movie = Movie.query.get(movie_id)
        if movie:
            try:
                data = request.get_json()
                if not ('title' in data and 'release_date' in data):
                    abort(422)
                title = data.get('title', None),
                excerpt = data.get('excerpt', None),
                release_date = data.get('release_date', None)
                if title:
                    movie.title = title
                if excerpt:
                    movie.excerpt = excerpt
                if release_date:
                    movie.release_date = release_date
                movie.update()
                return jsonify({
                    'success': True,
                    'movie': movie_id
                })
            except:
                abort(422)
        else:
            abort(404)


    # Delete a movie
    @app.route('/movies/<int:movie_id>', methods=['DELETE'])
    @requires_auth('delete:movies')
    def delete_drink(payload, movie_id):
        movie = Movie.query.get(movie_id)
        try:
            if movie is None:
                abort(404)
            movie.delete()
            return jsonify({
                'success': True,
                'delete': movie_id
            })
        except:
            abort(422)


    '''
    Actors
    ---------------------------------------------------------------------------------
    '''


    #  Get information about all actors
    @app.route('/actors')
    @requires_auth('get:actors')
    def get_actors(payload):
        all_actors = Actor.query.all()
        if all_actors:
            actors = [actor.long() for actor in all_actors]
            return jsonify({
                'success': True,
                'actors': actors
            })
        else:
            abort(404)


    # Get individual actor information
    @app.route('/actors/<int:actor_id>')
    @requires_auth('get:actors')
    def get_actor(payload, actor_id):
        actor = Actor.query.filter_by(id=actor_id).one_or_none()
        if actor:
            return jsonify({
                'success': True,
                'actor': [actor.long()]
            })
        else:
            abort(404)


    # Create an actor
    @app.route('/actors', methods=['POST'])
    @requires_auth('post:actors')
    def create_actor(payload):
        try:
            data = request.get_json()
            if not('name' in data and 'age' in data and 'gender' in data and 'city' in data and 'state' in data and 'phone' in data):
                abort(422)

            actor = Actor(
                name=data.get('name', None),
                age=data.get('age', None),
                gender=data.get('gender', None),
                city=data.get('city', None),
                state=data.get('state', None),
                phone=data.get('phone', None),
                email=data.get('email', None),
                website=data.get('website', None)
            )

            actor.insert()
            return jsonify({
                'success': True
            })
        except:
            abort(422)


    # Update an actor information
    @app.route('/actors/<int:actor_id>', methods=['PATCH'])
    @requires_auth('patch:actors')
    def update_actor(payload, actor_id):
        actor = Actor.query.get(actor_id)
        if actor:
            try:
                data = request.get_json()
                if not ('name' in data and 'age' in data and 'gender' in data and 'city' in data and 'state' in data and 'phone' in data):
                    abort(422)

                name = data.get('name', None),
                age = data.get('age', None),
                gender = data.get('gender', None),
                city = data.get('city', None),
                state = data.get('state', None),
                phone = data.get('phone', None),
                email = data.get('email', None),
                website = data.get('website', None)
                if name:
                    actor.name = name
                if age:
                    actor.age = age
                if gender:
                    actor.gender = gender
                if city:
                    actor.city = city
                if state:
                    actor.state = state
                if phone:
                    actor.phone = phone
                if email:
                    actor.email = email
                if website:
                    actor.website = website
                actor.update()
                return jsonify({
                    'success': True,
                    'actor': actor_id
                })
            except:
                abort(422)
        else:
            abort(404)


    # Delete an actor
    @app.route('/actors/<int:actor_id>', methods=['DELETE'])
    @requires_auth('delete:actors')
    def delete_actor(payload, actor_id):
        actor = Actor.query.get(actor_id)
        try:
            if actor is None:
                abort(404)
            actor.delete()
            return jsonify({
                'success': True,
                'delete': actor_id
            })
        except:
            abort(422)


    '''
    MovieCasts
    ---------------------------------------------------------------------------------
    '''


    #  Get information about all movies with their actors
    @app.route('/moviecasts')
    @requires_auth('get:moviecasts')
    def get_moviecasts(payload):
        movies = Movie.query.all()
        if movies:
            moviecasts = []
            for movie in movies:
                actors = []
                for act in movie.actors:
                    actor = Actor.query.get(act.actor_id)
                    actors.append(actor.long())

                moviecasts.append({
                    'id': movie.id,
                    'title': movie.title,
                    'excerpt': movie.excerpt,
                    'release_date': movie.release_date,
                    'actors': actors
                })
            return jsonify({
                'success': True,
                'moviecasts': moviecasts
            })
        else:
            abort(404)


    # Create a moviecast
    @app.route('/moviecasts', methods=['POST'])
    @requires_auth('post:moviecasts')
    def create_moviecasts(payload):
        try:
            data = request.get_json()
            if not ('actor_id' in data and 'movie_id' in data):
                abort(422)
            actor_id = data.get('actor_id', None)
            movie_id = data.get('movie_id', None)
            actor = Actor.query.get(actor_id)
            movie = Movie.query.get(movie_id)
            moviecasts = MovieCast.query.filter_by(actor_id=actor.id).one_or_none()

            if actor and movie:
                if not moviecasts:
                    new_moviecast = MovieCast(movie_id=movie_id, actor_id=actor_id)
                    new_moviecast.insert()
                    return jsonify({
                        'success': True,
                        'movie_id': movie_id,
                        'actor_id': actor_id
                    })
                else:
                    abort(422)
            else:
                abort(404)
        except:
            abort(422)


    ## Error Handling
    @app.errorhandler(404)
    def not_found(error):
        return jsonify({
            "success": False,
            "error": 404,
            "message": "Resource you are trying to modify is not found"
        }), 404


    @app.errorhandler(422)
    def unprocessable(error):
        return jsonify({
            "success": False,
            "error": 422,
            "message": "Unprocessable data, please check your data"
        }), 422


    @app.errorhandler(AuthError)
    def auth_error(error):
        return jsonify({
            "success": False,
            "error": error.status_code,
            "message": error.error
        }), 403

    return app


app = create_app()


if __name__ == '__main__':
    app.run()
