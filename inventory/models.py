from django.db import models
from django.urls import reverse
from django.utils.text import slugify
from django.contrib.auth import get_user_model
from cloudinary.models import CloudinaryField

User = get_user_model()


class ItemsList(models.Model):
    name = models.CharField(max_length=250, db_index=True)
    slug = models.SlugField(max_length=255, unique=True)
    user = models.ForeignKey(User, related_name='userlists', on_delete=models.CASCADE)

    # class Meta:
    #     verbose_name_plural = 'itemsLists'
    
    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        self.slug = self.get_slug()
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

    def get_guests(self):
        items = Guest.objects.filter(itemsList__id=self.id)
        guests = list(items)
        return guests

    def get_slug(self):
        slug = slugify(self.name)
        unique_slug = slug

        number = 1
        while ItemsList.objects.filter(slug=unique_slug).exists():
            unique_slug = f'{slug}-{number}'
            number += 1

        return unique_slug
    
class Item(models.Model):
    itemsList = models.ForeignKey(ItemsList, related_name='items', on_delete=models.CASCADE, null=True)
    title = models.CharField(max_length=100)
    brand = models.CharField(max_length=100)
    description = models.TextField(max_length=250,blank=True)
    slug = models.SlugField(max_length=255, unique=True)
    price = models.DecimalField(max_digits=7, decimal_places=2, default=0)
    #  Remove to integrate with cloudinary
    # image = models.ImageField(upload_to='images/')
    image = CloudinaryField('image')
    webPage = models.URLField(max_length=100, blank=True, default='http://')
    store = models.CharField(max_length=100, blank=False)
    bought = models.CharField(max_length=10, default='False')

    # class Meta:
    #     verbose_name_plural = 'items'
    
    def __str__(self):
        return self.title

    def get_slug(self):
        slug = slugify(self.title)
        unique_slug = slug

        number = 1
        while Item.objects.filter(slug=unique_slug).exists():
            unique_slug = f'{slug}-{number}'
            number += 1

        return unique_slug
    

    def save(self, *args, **kwargs):
        self.slug = self.get_slug()
        super().save(*args, **kwargs)

    
    def get_absolute_url(self):
        return reverse('list-items', kwargs={'list_slug': self.itemsList.slug})

class Guest(models.Model):
    user = models.ForeignKey(User, related_name='listguests', on_delete=models.CASCADE)
    itemsList = models.ForeignKey(ItemsList, related_name='guestsbylist', on_delete=models.CASCADE)
    """
        Permit_level have 3 levels for a guest:
        R = Can watch pictures and read
        C = R + can add new items
        I = C + can remove.
    """
    permit_level = models.CharField(max_length=1, verbose_name="allow",  null=False, blank=False, default="R")

    def __str__(self):
        level = "Allow: Read list items."
        match self.permit_level:
            case "C":
                level = "Allow: Add new items to the list."
            case "I":
                level = "Allow: Create, Update and Delete items in the list."

        return self.user.username + "\n"+level

    def get_level_description(self):
        level = "Read"
        match self.permit_level:
            case "C":
                level = "Read, Create."
            case "I":
                level = "Create, Read, Delete Items."

        return level


    class Meta:
        unique_together = ('user', 'itemsList')