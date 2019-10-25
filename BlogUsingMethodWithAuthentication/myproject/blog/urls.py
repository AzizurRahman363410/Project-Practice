from django.urls import path
from . import views
urlpatterns = [
    path('',views.home, name='home'),
    path('detail/<int:pk>/',views.detail, name='detail'),
    path('create_post',views.create_post, name='create_post'),
    path('update_post/<int:pk>/',views.update_post, name='update_post'),
    path('delete_post/<int:pk>/',views.delete_post, name='delete_post'),
    path('search/',views.search, name='search'),
]
