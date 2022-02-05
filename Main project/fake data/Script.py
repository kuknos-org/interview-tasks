import requests
from faker import Faker
import random


fake = Faker()

Genres = [
    "Action",
    "Comedy",
    "Drama",
    "Fantasy",
    "Horror",
    "Mystery",
    "Romance",
    "Thriller",
    "Western",
]


Book_Numbers = 51


for i in range(1, Book_Numbers):

    # Book
    requests.post(
        "http://localhost:8000/api/books/",
        json={
            "BookID": i,
            "Date_Published": random.randint(1985, 2022),
            "Genre": random.choice(Genres),
        },
    )


    # Author
    for j in range(1, random.randint(1, 4)):

        requests.post(
            "http://localhost:8000/api/authors/",
            json={
                "name": fake.name(),
                "age": random.randint(15, 85),
                "email": fake.email(),
                "country": fake.country(),
                "BookID": i,
            },
        )



    # Editor
    for k in range(1, random.randint(1, 4)):
        requests.post(
            "http://localhost:8000/api/editors/",
            json={
                "name": fake.name(),
                "age": random.randint(15, 85),
                "email": fake.email(),
                "country": fake.country(),
                "BookID": i,
            },
        )


    # Publisher
    requests.post(
        "http://localhost:8000/api/publishers/",
        json={"name": fake.name(), "country": fake.country(), "BookID": i},
    )




