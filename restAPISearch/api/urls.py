from django.urls import path
from . import views
urlpatterns = [
    path('',views.PostListAPIView.as_view(), name='api-list'),
    path('<int:pk>/',views.PostListAPIView.as_view(), name='api-list'),
    
]
