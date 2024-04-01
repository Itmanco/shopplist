from django.urls import path
from . import views

urlpatterns = [
    path('', views.welcome, name='welcome'),
    path('inventory', views.inventory, name='inventory'),
    path('item/<slug:slug>/', views.item_info, name='item-info'),
    path('search/<slug:list_slug>/', views.list_items, name='list-items'),
    path('lists/newlist', views.CreateList.as_view(), name='create_list'),
    path('item/newitem/<hpk>', views.CreateItem.as_view(), name='create_item'),
    path('item/update/<int:pk>', views.UpdateItem.as_view(), name='update_item'),
    path('item/delete/<int:itempk>/<slug:list_slug>/', views.DeleteItem, name='delete_item'),
    path('item/bought/<int:itempk>/<slug:list_slug>/', views.MarkBoughtItem, name='mark_bought_item'),
]