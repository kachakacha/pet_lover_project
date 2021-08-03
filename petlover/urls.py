from django.urls import path
from petlover import views

app_name = 'petlover'

urlpatterns = [
    path('', views.index, name='index'),
    path('<slug:category_name_slug>/',
         views.show_category, name='show_category'),
    path('<slug:category_name_slug>/<slug:pet_name_slug>/', views.show_pets, name='show_pets')
]