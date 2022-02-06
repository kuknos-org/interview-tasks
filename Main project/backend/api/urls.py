from django.urls import path, include
from .views import * 
# from rest_framework.routers import DefaultRouter   # Method 2

app_name = 'api'


# router = DefaultRouter()
# router.register("books",Books, basename='Books')
# router.register("authors",Authors, basename='Authors')
# router.register("editors",Editors, basename= 'Editors')
# router.register("publishers",Publishers, basename = 'Publishers')


urlpatterns = [
    # path('', include(router.urls)),

    path('books/',Books.as_view({'get': 'list','post':'create',
        'delete':'destroy','put':'update'}), name='Books'),

    path('authors/',Authors.as_view({'get': 'list','post':'create',
        'delete':'destroy','put':'update'}),name='Authors'),

    path('editors/',Editors.as_view({'get': 'list','post':'create',
        'delete':'destroy','put':'update'}),name='Editors'),

    path('publishers/',Publishers.as_view({'get': 'list','post':'create',
        'delete':'destroy','put':'update'}),name='Publishers'),

    path('books/<int:pk>/',BookDetail.as_view({'get': 'list','post':'create',
        'delete':'destroy','put':'update'}),name='SingleBook'),

    path('authors/<int:pk>/',AuthorDetail.as_view({'get': 'list','post':'create',
        'delete':'destroy','put':'update'}),name='SingleAuthor'),

    path('editors/<int:pk>/',EditorDetail.as_view({'get': 'list','post':'create',
        'delete':'destroy','put':'update'}),name='SingleEditor'),

    path('publishers/<int:pk>/',PublisherDetail.as_view({'get': 'list','post':'create',
        'delete':'destroy','put':'update'}),name='SinglePublisher'),
]