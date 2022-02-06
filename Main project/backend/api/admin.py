from django.contrib import admin
from .models import BookModel, AuthorModel, EditorModel, PublisherModel

# Register your models here.
admin.site.register(BookModel)
admin.site.register(EditorModel)
admin.site.register(AuthorModel)
admin.site.register(PublisherModel)
