from django.contrib import admin

from . models import ItemsList, Item, Guest

@admin.register(ItemsList)
class ItemsListAdmin(admin.ModelAdmin):

    prepopulated_fields = {'slug':('name',)}

@admin.register(Item)
class ItemsAdmin(admin.ModelAdmin):

    prepopulated_fields = {'slug':('title',)}

@admin.register(Guest)
class ItemsAdmin(admin.ModelAdmin):

    list_display = ["id", "user", "itemsList"]


