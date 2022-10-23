from django.urls import path
from . import views

urlpatterns = [
    path('<int:sign>', views.zodiac_int),
    path('<str:sign>', views.zodiac),
]
