from . import views
from django.urls import path

app_name = 'menu'
urlpatterns = [
    path('',views.IndexClassView.as_view(), name='index'),
    path ('<int:pk>/', views.FoodDetail.as_view(), name='detail'),
    path('items/', views.items,name='items'),
    path('dodaj', views.CreateItem.as_view(), name='create_item'),
    path('edit/<int:id>/', views.edit_item, name='edit_item'),
    path('delete/<int:id>', views.delete_item, name='delete_item'),
    path('location/', views.location, name='location'),
    path('about/', views.about, name='about'),
]
