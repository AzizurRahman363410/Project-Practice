from django.urls import path
from . import views
urlpatterns = [
    path('',views.BlogListView.as_view(),name='post_list' ),
    path('post_detail/<int:pk>/',views.BlogDetailView.as_view(),name='post_detail'),
    path('post_update/<int:pk>/',views.BlogUpdateView.as_view(),name='post_update'),
    path('post_create',views.BlogCreateView.as_view(),name='post_create'),
    path('post_delete/<int:pk>/',views.BlogDeleteView.as_view(),name='post_delete'),
    path('post_search/',views.BlogSearchView.as_view(),name='post_search'),
]