from django.urls import path
from . import views

urlpatterns = [
    path('users/',views.get_user,name='get_user'),
    path('users/create',views.create_user,name='create_user'),
    path('users/<int:pk>',views.user_detail,name='user_detail'),
]