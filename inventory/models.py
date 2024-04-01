from django.db import models
from django.urls import reverse
from django.utils.text import slugify
from django.contrib.auth import get_user_model

User = get_user_model()

class ItemsList(models.Model):
    name = models.CharField(max_length=250, db_index=True)
    slug = models.SlugField(max_length=255)
    user = models.ForeignKey(User, related_name='userlists', on_delete=models.CASCADE)

    # class Meta:
    #     verbose_name_plural = 'itemsLists'
    
    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super().save(*args, **kwargs)

    def get_items_url(self):
        return reverse('list-items', kwargs={'list_slug': self.slug})   
    
    def get_absolute_url(self):
        return reverse('inventory')

    def get_balance(self):
        items = Item.objects.filter(itemsList__id=self.id).filter(bought='False')
        entry_list = list(items)
        balance = 0
        for item in entry_list:
            balance += item.price
        return balance

    def get_spent(self):
        items = Item.objects.filter(itemsList__id=self.id).filter(bought='True')
        entry_list = list(items)
        spent = 0
        for item in entry_list:
            spent += item.price
        return spent
    
    def get_items_len(self): 
        items = Item.objects.filter(itemsList__id=self.id)
        entry_list = list(items)
        return len(entry_list)

    def get_guests_len(self):
        return 0
    

class Item(models.Model):
    itemsList = models.ForeignKey(ItemsList, related_name='items', on_delete=models.CASCADE, null=True)
    title = models.CharField(max_length=100)
    brand = models.CharField(max_length=100)
    description = models.TextField(max_length=250,blank=True)
    slug = models.SlugField(max_length=255)
    price = models.DecimalField(max_digits=7, decimal_places=2, default=0)
    image = models.ImageField(upload_to='images/')
    webPage = models.URLField(max_length=100, blank=True, default='http://')
    store = models.CharField(max_length=100, blank=False)
    bought = models.CharField(max_length=10, default='False')

    # class Meta:
    #     verbose_name_plural = 'items'
    
    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super().save(*args, **kwargs)
    
    def get_absolute_url(self):
        return reverse('list-items', kwargs={'list_slug': self.itemsList.slug})
