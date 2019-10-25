from django.urls import path
from . import views
urlpatterns = [
    path('', views.home, name="home"),
    path('pdf/', views.GeneratePDF.as_view(), name="pdf"),
]
