from django.urls import path
from . import views


app_name='food'
urlpatterns = [
    path('', views.index, name='index'),
    path('items/', views.items, name='items'),
    path('detail/<int:pk>/', views.detail, name='detail'),

    # //add item
    # path('add/', views.create_item, name='create_item'),
    path('add/', views.CreateItem.as_view(), name='create_item'),
    path('update/<int:pk>/', views.update_item, name='update_item'),
    path('delete/<int:pk>/', views.delete_item, name='delete_item'),
]
