from django.urls import path
from rango import views


app_name = 'fplhelp'

urlpatterns = [
    path('', views.index, name='index'),
]