from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('<int:sign>', views.zodiac_int),
    path('<str:sign>', views.zodiac, name='horoscope'),
]
