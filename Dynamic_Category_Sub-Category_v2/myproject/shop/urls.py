from django.urls import path
from . import views
urlpatterns = [
    path('',views.home, name='home'),
    path('<str:sub_category_slug>/', views.home, name='product_list_by_category'),
]
