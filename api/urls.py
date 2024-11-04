from django.urls import path
from .views import CarListAPI, CarDetailAPI, CommentAPI, CarCreateAPI

from api import views

app_name = 'api'

urlpatterns = [
    path('cars/', CarCreateAPI.as_view(), name='cars-create'),
    path('cars/', CarListAPI.as_view(), name='cars-list'),
    path('cars/<int:pk>/', CarDetailAPI.as_view(), name='car-detail'),
    path('cars/<int:pk>/comments/', CommentAPI.as_view(), name='comment-detail'),
]