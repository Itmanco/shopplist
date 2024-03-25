from django.contrib import admin

from . models import ItemsList, Item

@admin.register(ItemsList)
class ItemsListAdmin(admin.ModelAdmin):

    prepopulated_fields = {'slug':('name',)}

@admin.register(Item)
class ItemsAdmin(admin.ModelAdmin):

    prepopulated_fields = {'slug':('title',)}
