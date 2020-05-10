import os
import unittest
import json
from flask_sqlalchemy import SQLAlchemy

from app import create_app
from models import setup_db, MovieCast, Movie, Actor

new_actor_id = None
new_movie_id = None

class MovieAgencyTestCase(unittest.TestCase):
    """This class represents the capstone test case"""

    def setUp(self):
        """Define test variables and initialize app."""
        self.app = create_app()
        self.client = self.app.test_client()
        self.database_name = "capstone_test"
        self.database_path = "postgresql://{}/{}".format('postgres:postgres@localhost:5432', self.database_name)
        setup_db(self.app, self.database_path)
        self.mastertoken = "eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6IkcxY0oySW1yY1RmejJKWmY0QlFJTyJ9.eyJpc3MiOiJodHRwczovL3Jvbi1mbnNkLmF1dGgwLmNvbS8iLCJzdWIiOiJhdXRoMHw1ZWI2YmZhNjZiNjliYzBjMTIwNzMyNWYiLCJhdWQiOiJtb3ZpZSIsImlhdCI6MTU4OTA0MzQyMCwiZXhwIjoxNTg5MTI5ODIwLCJhenAiOiJQVDl4UnRsN1RmYUtYMDlQRG0ycUpTRllvVmxYRERYSCIsInNjb3BlIjoiIiwicGVybWlzc2lvbnMiOlsiZGVsZXRlOmFjdG9ycyIsImRlbGV0ZTptb3ZpZXMiLCJnZXQ6YWN0b3JzIiwiZ2V0Om1vdmllY2FzdHMiLCJnZXQ6bW92aWVzIiwicGF0Y2g6YWN0b3JzIiwicGF0Y2g6bW92aWVzIiwicG9zdDphY3RvcnMiLCJwb3N0Om1vdmllY2FzdHMiLCJwb3N0Om1vdmllcyJdfQ.V-x-tZC0HkiJdaIkKbxpPzWqp0RclTFFKoaGoEnzZunR2mpc6Bgz4o1ihb9IqVgMZNPXtTRhqrLwqdyHt9jd1G2qM7Yv5vUjxGyWVAziHZPJ7AeIh-5S63GGwrOzHJ3Wp2i0_ooP3nTrGa2ANsp9NjIZHbFzVr5LGtN2slsAmOVeFftyrHNYaxMv8UF7jSfC48jMv-7h-8CXnngWYw97q9hZXj7r-cuMZakSvMG2TExFdk26PFjrhEs_nfIfhxXY0uHIEPcbzR6GvBg2X7Dx_02UlkqKE4usU7pUcbEMoWnHKvZmTAyKVZj8qk2r4Vk3LwIUEWJA1HF2YTbnUwEw6w"

        # binds the app to the current context
        with self.app.app_context():
            self.db = SQLAlchemy()
            self.db.init_app(self.app)
            # create all tables
            self.db.create_all()

    def tearDown(self):
        """Executed after each test"""
        pass

    def test_add_movie(self):
        """ Test the POST /movies endpoint which creates a new movie """
        global new_movie_id
        movie = {
            "title": "Dark Knight",
            "excerpt": "See the famous Dark Knight in action",
            "release_date": "2020-10-08"
        }
        headers = {
            'Content-Type': 'application/json',
            'Authorization': f'Bearer {self.mastertoken}'
        }
        api = self.client.post('/movies', data=json.dumps(movie), headers=headers)
        self.assertEqual(api.status_code, 200)
        body = json.loads(api.data)
        self.assertEqual(body["success"], True)
        new_movie_id = body["id"]

    def test_b_add_movie_fail(self):
        """ Tests the POST /movies API endpoint by sending incomplete data """
        movie = {
            "excerpt": "See the famous Dark Knight in action",
            "release_date": "2020-10-08"
        }
        headers = {
            'Content-Type': 'application/json',
            'Authorization': f'Bearer {self.mastertoken}'
        }
        api = self.client.post('/movies', data=json.dumps(movie), headers=headers)
        self.assertEqual(api.status_code, 422)
        data = json.loads(api.data)
        self.assertEqual(data["success"], False)
        self.assertEqual(data["message"], "Unprocessable data, please check your data")

    def test_c_update_movie(self):
        """ Test the PATCH /movies by updating the movie information """
        global new_movie_id
        movie = {
            "title": "Dark Knight and Joker",
            "release_date": "2020-10-08"
        }
        headers = {
            'Content-Type': 'application/json',
            'Authorization': f'Bearer {self.mastertoken}'
        }
        api = self.client.patch(f'/movies/' + str(new_movie_id), data=json.dumps(movie), headers=headers)
        self.assertEqual(api.status_code, 200)
        body = json.loads(api.data)
        self.assertEqual(body["success"], True)
        self.assertEqual(body["movie"], new_movie_id)

    def test_d_update_movie_fail(self):
        """ Test the PATCH /movies by sending incomplete data """
        global new_movie_id
        movie = {
            "release_date": "2020-10-08"
        }
        headers = {
            'Content-Type': 'application/json',
            'Authorization': f'Bearer {self.mastertoken}'
        }
        api = self.client.patch(f'/movies/{new_movie_id}', data=json.dumps(movie), headers=headers)
        self.assertEqual(api.status_code, 422)
        body = json.loads(api.data)
        self.assertEqual(body["success"], False)
        self.assertEqual(body["message"], "Unprocessable data, please check your data")

    def test_e_add_actor(self):
        """ Test the POST /actors endpoint which creates a new actor """
        global new_actor_id
        actor = {
            "name": "Sylvester Stallone",
            "age": 59,
            "gender": "Male",
            "city": "Arizona",
            "state": "TX",
            "phone": "123456",
            "email": "sylvie@gmail.com",
            "website": "sylvie.com"
        }
        headers = {
            'Content-Type': 'application/json',
            'Authorization': f'Bearer {self.mastertoken}'
        }
        api = self.client.post('/actors', data=json.dumps(actor), headers=headers)
        self.assertEqual(api.status_code, 200)
        body = json.loads(api.data)
        self.assertEqual(body["success"], True)
        new_actor_id = body["id"]

    def test_f_add_actor_fail(self):
        """ Tests the POST /actors API endpoint by sending data with missing information """
        actor = {
            "age": 39,
            "gender": "Male",
            "city": "Arizona",
            "state": "TX",
            "phone": "123456",
            "email": "dwayne@gmail.com",
            "website": "dwayne.com"
        }
        headers = {
            'Content-Type': 'application/json',
            'Authorization': f'Bearer {self.mastertoken}'
        }
        api = self.client.post('/actors', data=json.dumps(actor), headers=headers)
        self.assertEqual(api.status_code, 422)
        data = json.loads(api.data)
        self.assertEqual(data["success"], False)
        self.assertEqual(data["message"], "Unprocessable data, please check your data")

    def test_g_update_actor(self):
        """ Test the PATCH /actor by updating the actor information """
        global new_actor_id
        actor = {
            "name": "Sylvie",
            "age": 75,
            "gender": "Male",
            "city": "Dallas",
            "state": "TX",
            "phone": "123456",
            "email": "sylvie@gmail.com",
        }
        headers = {
            'Content-Type': 'application/json',
            'Authorization': f'Bearer {self.mastertoken}'
        }
        api = self.client.patch(f'/actors/{new_actor_id}', data=json.dumps(actor), headers=headers)
        self.assertEqual(api.status_code, 200)
        body = json.loads(api.data)
        self.assertEqual(body["success"], True)
        self.assertEqual(body["actor"], new_actor_id)

    def test_h_update_actor_fail(self):
        """ Test the PATCH /actors by sending incomplete data """
        global new_actor_id
        actor = {
            "website": "ssl.com"
        }
        headers = {
            'Content-Type': 'application/json',
            'Authorization': f'Bearer {self.mastertoken}'
        }
        api = self.client.patch(f'/actors/{new_actor_id}', data=json.dumps(actor), headers=headers)
        self.assertEqual(api.status_code, 422)
        body = json.loads(api.data)
        self.assertEqual(body["success"], False)
        self.assertEqual(body["message"], "Unprocessable data, please check your data")


    def test_i_add_moviecast(self):
        """ Test the POST /moviecasts endpoint which creates a new moviecast """
        global new_actor_id
        global new_movie_id
        moviecast = {
            "actor_id": new_actor_id,
            "movie_id": new_movie_id
        }
        headers = {
            'Content-Type': 'application/json',
            'Authorization': f'Bearer {self.mastertoken}'
        }
        api = self.client.post('/moviecasts', data=json.dumps(moviecast), headers=headers)
        self.assertEqual(api.status_code, 200)
        body = json.loads(api.data)
        self.assertEqual(body["success"], True)
        self.assertEqual(body["movie_id"], new_movie_id)
        self.assertEqual(body["actor_id"], new_actor_id)

    def test_j_add_moviecast_fail(self):
        """ Tests the POST /moviecasts API endpoint by sending not existing IDs """
        moviecast = {
            "actor_id": 1000,
            "movie_id": 1000
        }
        headers = {
            'Content-Type': 'application/json',
            'Authorization': f'Bearer {self.mastertoken}'
        }
        api = self.client.post('/moviecasts', data=json.dumps(moviecast), headers=headers)
        self.assertEqual(api.status_code, 422)
        data = json.loads(api.data)
        self.assertEqual(data["success"], False)
        self.assertEqual(data["message"], "Unprocessable data, please check your data")

    def test_k_get_movies(self):
        """Tests the GET /movies API endpoint to get all movies """
        headers = {
            'Authorization': f'Bearer {self.mastertoken}'
        }
        api = self.client.get('/movies', headers=headers)
        self.assertEqual(api.status_code, 200)
        data = json.loads(api.data)
        self.assertEqual(data["success"], True)
        self.assertTrue(data["movies"])

    def test_l_get_movie(self):
        """Tests the GET /movie API endpoint to get one movie """
        global new_movie_id
        headers = {
            'Authorization': f'Bearer {self.mastertoken}'
        }
        api = self.client.get(f'/movies/{new_movie_id}', headers=headers)
        self.assertEqual(api.status_code, 200)
        data = json.loads(api.data)
        expected_movie = [{
            'excerpt': None,
            'id': new_movie_id,
            'release_date': 'Thu, 08 Oct 2020 00:00:00 GMT',
            'title': 'Dark Knight and Joker'
        }]
        self.assertEqual(data["success"], True)
        self.assertTrue(data["movie"])

    def test_m_get_movie_fail(self):
        """Tests the GET /movie API endpoint to get one non-existent movie """
        headers = {
            'Authorization': f'Bearer {self.mastertoken}'
        }
        api = self.client.get('/movies/1000', headers=headers)
        self.assertEqual(api.status_code, 404)
        data = json.loads(api.data)
        self.assertEqual(data["success"], False)
        self.assertEqual(data["message"], "Resource you are trying to modify is not found")

    def test_n_get_actors(self):
        """Tests the GET /actors API endpoint to get all actors """
        headers = {
            'Authorization': f'Bearer {self.mastertoken}'
        }
        api = self.client.get('/actors', headers=headers)
        self.assertEqual(api.status_code, 200)
        data = json.loads(api.data)
        self.assertEqual(data["success"], True)
        self.assertTrue(data["actors"])

    def test_o_get_actor(self):
        """Tests the GET /actor API endpoint to get one actor """
        global new_actor_id
        headers = {
            'Authorization': f'Bearer {self.mastertoken}'
        }
        api = self.client.get(f'/actors/{new_actor_id}', headers=headers)
        self.assertEqual(api.status_code, 200)
        data = json.loads(api.data)
        expected_actor = [{
            "id": new_actor_id,
            "name": "Sylvie",
            "age": 75,
            "gender": "Male",
            "city": "Dallas",
            "state": "TX",
            "phone": "123456",
            "email": "sylvie@gmail.com",
            "website": "sylvie.com"
        }]
        self.assertEqual(data["success"], True)
        self.assertTrue(data["actor"])
        self.assertEqual(data["actor"], expected_actor)

    def test_p_get_actor_fail(self):
        """Tests the GET /actors API endpoint to get one non-existent actor """
        headers = {
            'Authorization': f'Bearer {self.mastertoken}'
        }
        api = self.client.get('/actors/1000', headers=headers)
        self.assertEqual(api.status_code, 404)
        data = json.loads(api.data)
        self.assertEqual(data["success"], False)
        self.assertEqual(data["message"], "Resource you are trying to modify is not found")

    def test_q_get_moviecasts(self):
        """Tests the GET /moviecasts API endpoint to get all moviecasts """
        headers = {
            'Authorization': f'Bearer {self.mastertoken}'
        }
        api = self.client.get('/moviecasts', headers=headers)
        self.assertEqual(api.status_code, 200)
        data = json.loads(api.data)
        self.assertEqual(data["success"], True)
        self.assertTrue(data["moviecasts"])

    def test_r_delete_actor(self):
        """ Tests the DELETE /actors endpoint which deletes a specific actor """
        global new_actor_id
        headers = {
            'Authorization': f'Bearer {self.mastertoken}'
        }
        api = self.client.delete(f'/actors/{new_actor_id}', headers=headers)
        self.assertEqual(api.status_code, 200)
        body = json.loads(api.data)
        self.assertEqual(body["success"], True)

    def test_s_delete_actor_fail(self):
        """ Tests the DELETE /actors endpoint which deletes a specific actor """
        global new_actor_id
        headers = {
            'Authorization': f'Bearer {self.mastertoken}'
        }
        api = self.client.delete(f'/actors/{new_actor_id}', headers=headers)
        self.assertEqual(api.status_code, 422)
        data = json.loads(api.data)
        self.assertEqual(data["success"], False)
        self.assertEqual(data["message"], "Unprocessable data, please check your data")

    def test_t_delete_movie(self):
        """ Tests the DELETE /movies endpoint which deletes a specific movie """
        global new_movie_id
        headers = {
            'Authorization': f'Bearer {self.mastertoken}'
        }
        api = self.client.delete(f'/movies/{new_movie_id}', headers=headers)
        self.assertEqual(api.status_code, 200)
        body = json.loads(api.data)
        self.assertEqual(body["success"], True)

    def test_u_delete_movie_fail(self):
        """ Tests the DELETE /movies endpoint which deletes a specific movie """
        headers = {
            'Authorization': f'Bearer {self.mastertoken}'
        }
        api = self.client.delete(f'/movies/{new_movie_id}', headers=headers)
        self.assertEqual(api.status_code, 422)
        data = json.loads(api.data)
        self.assertEqual(data["success"], False)
        self.assertEqual(data["message"], "Unprocessable data, please check your data")


if __name__ == "__main__":
    unittest.main()
