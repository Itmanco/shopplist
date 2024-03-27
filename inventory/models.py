from django.db import models
from django.urls import reverse
from django.contrib.auth import get_user_model

User = get_user_model()

class ItemsList(models.Model):
    name = models.CharField(max_length=250, db_index=True)
    slug = models.SlugField(max_length=250, unique=True)
    user = models.ForeignKey(User, related_name='userlists', on_delete=models.CASCADE)

    # class Meta:
    #     verbose_name_plural = 'itemsLists'
    
    def __str__(self):
        return self.name
    
    
    def get_absolute_url(self):
        return reverse('list-items', args=[self.slug])

    def get_balance(self):
        items = Item.objects.filter(itemsList__id=self.id)
        entry_list = list(items)
        balance = 0
        for item in entry_list:
            balance += item.price
        return balance
    
    def get_items_len(self): 
        items = Item.objects.filter(itemsList__id=self.id)
        entry_list = list(items)
        return len(entry_list)

    def get_guests_len(self):
        # print(allItems)
        return 0
    

class Item(models.Model):
    itemsList = models.ForeignKey(ItemsList, related_name='items', on_delete=models.CASCADE, null=True)
    title = models.CharField(max_length=250)
    brand = models.CharField(max_length=250, default='')
    description = models.TextField(blank=True)
    slug = models.SlugField(max_length=255)
    price = models.DecimalField(max_digits=7, decimal_places=2, default=0)
    image = models.ImageField(upload_to='images/')
    webPage = models.URLField(max_length=100, blank=True, default='http://')
    store = models.CharField(max_length=100, blank=False)

    # class Meta:
    #     verbose_name_plural = 'items'
    
    def __str__(self):
        return self.title
    
    def get_absolute_url(self):
        # return reverse('list-items', args=[self.itemsList.slug])
        return reverse('list-items', kwargs={'list_slug': self.itemsList.slug})
