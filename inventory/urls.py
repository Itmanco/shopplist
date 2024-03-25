from django.urls import path
from . import views

urlpatterns = [
    path('', views.inventory, name='inventory'),
    # path('List/<slug:slug>/', views.List_info, name='List-info')
]