from rest_framework import serializers
from .models import *


class AuthorSerializer(serializers.ModelSerializer):
	class Meta:
		model = AuthorModel
		#exclude=['BookID']
		fields = '__all__'

class EditorSerializer(serializers.ModelSerializer):
	class Meta:
		model = EditorModel
		#exclude=['BookID']
		fields = '__all__'
		
class PublisherSerializer(serializers.ModelSerializer):
	class Meta:
		model = PublisherModel
		#exclude=['BookID']
		fields = '__all__'

class BookSerializer(serializers.ModelSerializer):
	
	Author = AuthorSerializer(read_only=True, many=True)
	Editor = EditorSerializer(read_only=True, many=True)
	Publisher = PublisherSerializer(read_only=True, many=True)

	class Meta:
		model = BookModel
		fields = '__all__'