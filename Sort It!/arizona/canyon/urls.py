from django.urls import path, re_path
from . import views

app_name = 'canyon'


urlpatterns = [
    path('', views.index, name='Home'),
    path('results/', views.results, name='Results'),
]

