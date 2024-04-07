from django.urls import path
from . import views


urlpatterns = [
    path('', views.welcome, name='welcome'),
    path('inventory', views.inventory, name='inventory'),
    path('item/<slug:slug>/', views.item_info, name='item-info'),
    path('search/<slug:list_slug>/', views.list_items, name='list-items'),
    path('lists/newlist', views.CreateList.as_view(), name='create_list'),
    path('lists/delete/<slug:list_slug>/', views.DeleteList, name='delete_list'),
    path('lists/guests/<slug:list_slug>/', views.GuestsList, name='guests_list'),
    path('lists/guests/remove/<slug:list_slug>/<int:userpk>/', views.GuestsListRemove, name='remove_guests_list'),
    path('lists/guests/add/<slug:list_slug>/<int:userpk>/', views.GuestsListAdd, name='add_guests_list'),
    path('item/newitem/<hpk>', views.CreateItem.as_view(), name='create_item'),
    path('item/update/<int:pk>', views.UpdateItem.as_view(), name='update_item'),
    path('item/delete/<int:itempk>/<slug:list_slug>/', views.DeleteItem, name='delete_item'),
    path('item/bought/<int:itempk>/<slug:list_slug>/', views.MarkBoughtItem, name='mark_bought_item'),
    path('item/return/<int:itempk>/<slug:list_slug>/', views.ReturnItemToList, name='return_item'),
]