from django.urls import path
from fplhelp import views


app_name = 'fplhelp'

urlpatterns = [
    path('', views.index, name='index'),
    path('fdr/', views.fdr, name='fdr')
]