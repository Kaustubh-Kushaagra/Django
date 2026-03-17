from django.urls import path
from courseapp.views import django_view
urlpatterns = [
    path('dj/', django_view,name='django_view'),
]