from django.urls import path
from . import views

urlpatterns = [
    path('', views.welcome, name='welcome'),
    path('inventory', views.inventory, name='inventory'),
    path('item/<slug:slug>/', views.item_info, name='item-info'),
    path('search/<slug:list_slug>/', views.list_items, name='list-items'),
    path('item/newitem/<hpk>', views.CreateItem.as_view(), name='create_item'),
]