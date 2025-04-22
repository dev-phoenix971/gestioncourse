from django.urls import path
from .views import race_list, add_race, add_horse, add_race_result, horse_list, update_race, delete_race, update_horse, delete_horse, home

urlpatterns = [
    path('', home, name='home'),
    path('courses/', race_list, name='race_list'),
    path('add-race/', add_race, name='add_race'),
    path('add-horse/', add_horse, name='add_horse'),
    path('add-race-result/', add_race_result, name='add_race_result'),
    path('horses/', horse_list, name='horse_list'),
    path('update-race/<int:race_id>/', update_race, name='update_race'),
    path('delete-race/<int:race_id>/', delete_race, name='delete_race'),
    path('update-horse/<int:horse_id>/', update_horse, name='update_horse'),
    path('delete-horse/<int:horse_id>/', delete_horse, name='delete_horse'),
]
