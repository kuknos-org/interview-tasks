# Python/Django Interview
For this task you would be building a basic blog application using Django (https://docs.djangoproject.com/en/3.0/) and Django rest framework (https://www.django-rest-framework.org/). The app should contain the api endpoints below, and MUST contain unit tests.

You will be tested on the quality of code and how exhaustive your unit tests are. Your application should, of course, meet all requirements.

Please upload solution to github (or gitbucket or gitlab) and submit solution link.

## ER Diagram
ER Diagram: https://github.com/kuknos-org/interview-tasks/blob/master/Er-diagram.pdf

The data models should follow the ER diagram format in the image above.
`1:*` simply means one or more than one (i.e a `Book` can have one or two or three authors etc)
`1` means one (i.e a `Book` can have only one publisher)

## API Endpoints
The following endpoints should be created on the `Book`, `Author`, `Editor`, and `Publisher` models: `POST`, `UPDATE`, `DELETE`.

It should also be possible to list all the model objects via an endpoint (See viewsets on DRF: https://www.django-rest-framework.org/api-guide/viewsets/).

## Tests
Unit tests must be written for all the model objects and enpoints. A code coverage of 90% is preferrable.

## Docker (not required)
Use Docker to containarise the application if you can.

## Create fake data
Write a script which creates dummy data for all the models. You can use the python `Faker` library to help create the data (https://pypi.org/project/Faker/).

## Bonus (not required!)
Deploy application to heroku (https://devcenter.heroku.com/articles/django-app-configuration)

