from django.urls import path

from cars import views

app_name = 'car'

urlpatterns = [
    path('<int:pk>', views.CarCardView.as_view(), name='card_car'),
    path('create/', views.CarCreateView.as_view(), name='create'),
    path('my_car/', views.MyCarView.as_view(), name='my_cars'),
    path('update/<int:pk>', views.CarUpdateView.as_view(), name='update'),
    path('delete/<int:pk>', views.carDelete, name='delete'),
]