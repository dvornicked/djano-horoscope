from django.urls import path
from . import views

urlpatterns = [
    path('<sign>', views.zodiac),
]
