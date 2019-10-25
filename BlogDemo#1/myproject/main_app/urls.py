from django.urls import path,re_path
from . import views


urlpatterns = [
   path('',views.index, name="home"),
   path('post/<int:pk>/', views.post_view, name='post'),
   #re_path(r'^post/(?P<pk>[0-9])/$', views.post_view, name='post'),
# both are correct
]
