from django.urls import path
from .views import index, gallery

urlpatterns = [
    path('', index, name='index'),
    path('gallery/', gallery, name='gallery' )
]