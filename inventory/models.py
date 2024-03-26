from django.db import models
from django.urls import reverse

class ItemsList(models.Model):
    name = models.CharField(max_length=250, db_index=True)
    slug = models.SlugField(max_length=250, unique=True)

    class Meta:
        verbose_name_plural = 'itemsLists'
    
    def __str__(self):
        return self.name
    
    
    def get_absolute_url(self):
        return reverse('items-lists', args=[self.slug])

    def get_balance(self):
        allItems = ItemsList.objects
        # print(allItems)
        return 12536.5
    
    def get_items_len(self):
        allItems = ItemsList.objects
        # print(allItems)
        return 8

    def get_guests_len(self):
        allItems = ItemsList.objects
        # print(allItems)
        return 2
    

class Item(models.Model):
    itemsList = models.ForeignKey(ItemsList, related_name='item', on_delete=models.CASCADE, null=True)
    title = models.CharField(max_length=250)
    brand = models.CharField(max_length=250, default='un-branded')
    description = models.TextField(blank=True)
    slug = models.SlugField(max_length=255)
    price = models.DecimalField(max_digits=7, decimal_places=2)
    image = models.ImageField(upload_to='images/')
    webPage = models.TextField(max_length=250, default='')
    store = models.TextField(max_length=250, blank=False)

    class Meta:
        verbose_name_plural = 'items'
    
    def __str__(self):
        return self.title
    
    def get_absolute_url(self):
        return reverse('item-info', args=[self.slug])
