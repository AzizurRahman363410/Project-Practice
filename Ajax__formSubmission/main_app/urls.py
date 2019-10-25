from django.urls import path
from . import views
urlpatterns = [
    path('', views.home, name='home'),
    path('signup/', views.SignUpView.as_view(), name='signup'),
    path('create_post/', views.create_post, name='create_post'),
    path('delete_post/<int:pk>/', views.delete_post, name='delete_post'),
   
   
]
