from django.urls import path

from comments import views

app_name = 'comment'

urlpatterns = [
    path('my_comment/', views.MyCommentsView.as_view(), name='my_comments'),
    path('delete/<int:pk>', views.commentDelete, name='delete'),
]