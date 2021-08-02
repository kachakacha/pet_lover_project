from django.urls import path
from petlover import views

app_name = 'petlover'

urlpatterns = [
    path('', views.index, name='index'),
    path('category/')
]