from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('product_list/', views.productList, name='product'),
    path('contact/', views.contact, name='contact'),
    path('about/', views.about, name='about'),
    path('register/', views.register, name='register'),
    path('login/', views.login, name='login'),
    path('checkout/', views.checkout, name='checkout'),

    path('single-item/<slug>/',views.single_item, name='single-item'),


    path('order-summary', views.OrderSummaryView.as_view(), name='order-summary'),
    path('add-to-cart/<slug:slug>/',views.add_to_cart, name='add-to-cart'),
    path('remove-form-cart/<slug:slug>/',views.remove_from_cart, name='remove-form-cart'),
    path('remove-item-from-cart/<slug:slug>/',views.remove_single_item_from_cart, name='remove-single-item-from-cart'),
   
]
