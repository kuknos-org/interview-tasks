from django.test import TestCase
from django.urls import reverse, resolve
from django.test import Client


c = Client()


class ViewsTestCase(TestCase):

    def setUp(self):
        pass

    def tearDown(self):
        pass

    # HTTP Get Method Checker

    def test_index_books(self):
        response = self.client.get('http://localhost:8000/api/books/')
        self.assertEqual(response.status_code, 200)

    def test_index_authors(self):
        response = self.client.get('http://localhost:8000/api/authors/')
        self.assertEqual(response.status_code, 200)

    def test_index_editors(self):
        response = self.client.get('http://localhost:8000/api/editors/')
        self.assertEqual(response.status_code, 200)

    def test_index_publishers(self):
        response = self.client.get('http://localhost:8000/api/publishers/')
        self.assertEqual(response.status_code, 200)    

    def test_get_books(self):
        match = resolve('/api/books/')
        self.assertEqual(match.url_name, "Books")

    def test_get_authors(self):

        match = resolve('/api/authors/')
        self.assertEqual(match.url_name, "Authors")

    def test_get_editors(self):

        match = resolve('/api/editors/')
        self.assertEqual(match.url_name, "Editors")

    def test_get_publishers(self):

        match = resolve('/api/publishers/')
        self.assertEqual(match.url_name, "Publishers")



    # HTTP Post Method Checker

    def test_post_books(self):                # Books

        data = {"BookID": 56,
            "Date_Published": 2013,
            "Genre": "MAX"
            }

        response = c.post('/api/books/', data = data)
        self.assertEqual(response.status_code, 201)



    # HTTP Put Method Checker

    def test_put_books(self):                  # Books

        data = {"BookID": 10,
            "Date_Published": 2013,
            "Genre": "MAX"
            }

        response = c.put('/api/books/10', data= data , follow=True)
        self.assertEqual(response.status_code, 200)


    def test_put_authors(self):                  # Authors

        data = {"id": 19,
            "name": "Justina Frazier",
            "age": 32,
            "email": "allison97@example.net",
            "country": "Dominica",
            "BookID": 11
            }

        response = c.put('/api/authors/11', data= data , follow=True)
        self.assertEqual(response.status_code, 200)



    def test_put_editors(self):                  # Editors

        data = {"id": 21,
            "name": "Justina Frazier",
            "age": 41,
            "email": "alliso27@example.net",
            "country": "Dominica",
            "BookID": 15            }

        response = c.put('/api/editors/15', data= data , follow=True)
        self.assertEqual(response.status_code, 200)


    def test_put_publishers(self):                  # Publishers

        data = {"id": 21,
            "name": "Fered Rodrigo",
            "age": 23,
            "email": "rodrigo23@example.net",
            "country": "Italy",
            "BookID": 15            }

        response = c.put('/api/publishers/15', data= data , follow=True)
        self.assertEqual(response.status_code, 200)