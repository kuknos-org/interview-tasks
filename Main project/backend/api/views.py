from rest_framework import viewsets, generics
from . import models, serializers



########## Main Pages ##########



class Books(viewsets.ModelViewSet):  #generics.RetrieveUpdateDestroyAPIView  -for Method 2

    queryset = models.BookModel.objects.all()
    serializer_class = serializers.BookSerializer


class Authors(viewsets.ModelViewSet):   #generics.RetrieveUpdateDestroyAPIView  -for Method 2

    queryset = models.AuthorModel.objects.all()
    serializer_class = serializers.AuthorSerializer


class Editors(viewsets.ModelViewSet): #generics.RetrieveUpdateDestroyAPIView  -for Method 2

    queryset = models.EditorModel.objects.all()
    serializer_class = serializers.EditorSerializer


class Publishers(viewsets.ModelViewSet): #generics.RetrieveUpdateDestroyAPIView  -for Method 2

    queryset = models.PublisherModel.objects.all()
    serializer_class = serializers.PublisherSerializer



########## Single Pages ##########



class BookDetail(viewsets.ModelViewSet):


    def get_queryset(self):
        pk = self.kwargs.get("pk")
        return models.BookModel.objects.filter(BookID = pk)
    
    serializer_class = serializers.BookSerializer


class AuthorDetail(viewsets.ModelViewSet):


    def get_queryset(self):
        pk = self.kwargs.get("pk")
        return models.AuthorModel.objects.filter(id = pk)
    
    serializer_class = serializers.AuthorSerializer


class EditorDetail(viewsets.ModelViewSet):


    def get_queryset(self):
        pk = self.kwargs.get("pk")
        return models.EditorModel.objects.filter(id = pk)
    
    serializer_class = serializers.EditorSerializer

class PublisherDetail(viewsets.ModelViewSet):


    def get_queryset(self):
        pk = self.kwargs.get("pk")
        return models.PublisherModel.objects.filter(id = pk)
    
    serializer_class = serializers.PublisherSerializer



