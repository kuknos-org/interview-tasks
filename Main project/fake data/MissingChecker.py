import requests
from faker import Faker
import random


fake = Faker()


h = requests.get('http://localhost:8000/api/books/?format=json')


#print(list(h.json()[5-1].values())[5] == "Acttion")

#Cond1 = list(h.json()[i-1].values())[1] == []         # Missing Author Checker
#Cond2 = list(h.json()[i-1].values())[2] == []         # Missing Editor Checker
#Cond3 = list(h.json()[i-1].values())[3] == []         # Missing Publisher Checker
# Cond4 = list(h.json()[i-1].values())[4] == int()		# Missing Date
# Cond5 = list(h.json()[i-1].values())[5] == ""			# Missing Genre


i = 1


while i <= len(list(h.json())):
	
	

	if list(h.json()[i-1].values())[1] == []:

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


	elif list(h.json()[i-1].values())[2] == []:

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


	elif list(h.json()[i-1].values())[3] == []:

		requests.post(
	        "http://localhost:8000/api/publishers/",
	        json={"name": fake.name(), "country": fake.country(), "BookID": i},
	    )

	else:

		pass

	i += 1