from django.db import models


class BookModel(models.Model):

	BookID = models.IntegerField(primary_key=True)
	Date_Published = models.IntegerField(default=2022)
	Genre = models.CharField(max_length=60, default="BookGenre")


class AuthorModel(models.Model):

	BookID=models.ForeignKey(BookModel, related_name='Author',on_delete=models.CASCADE)
	name = models.CharField(max_length=60, default="AuthorName")
	age = models.IntegerField()
	email = models.EmailField()
	country = models.CharField(max_length=30, default="AuthorCountry")

	def __str__(self):
		return self.name
	

class EditorModel(models.Model):

	BookID=models.ForeignKey(BookModel, related_name='Editor',on_delete=models.CASCADE)
	name = models.CharField(max_length=60, default="EditorName")
	age = models.IntegerField()
	email = models.EmailField()
	country = models.CharField(max_length=30, default="EditorCountry")

	def __str__(self):
		return self.name	

class PublisherModel(models.Model):

	BookID=models.ForeignKey(BookModel, related_name='Publisher',on_delete=models.CASCADE)
	name = models.CharField(max_length=60, default="PublisherName")
	country = models.CharField(max_length=30, default="PublisherCountry")
	
	def __str__(self):
		return self.name	




