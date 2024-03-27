from django import forms
from .models import Item

from django.contrib.auth import get_user_model

User = get_user_model()

class ItemForm(forms.ModelForm):
    class Meta:
        model = Item
        fields = ('title', 'image','brand', 'description','price','webPage')

    widgets = {
        'title': forms.Textarea(attrs={'class': 'form-control'}),
        'brand': forms.Textarea(attrs={'class': 'form-control'}),
        'image': forms.FileInput(attrs={'class': 'form-control'}),
        'description': forms.Textarea(attrs={'class': 'form-control'}),
        'price': forms.Textarea(attrs={'class': 'form-control'}),
        'webPage': forms.Textarea(attrs={'class': 'form-control'}),
    }

    def __init__(self, *args, **kwargs):
        super(ItemForm, self).__init__(*args, **kwargs)
        self.fields['description'].label = ""
        self.fields['title'].label = "Title"
        self.fields['brand'].label = "Brand"
        self.fields['image'].label = "Image"
        self.fields['price'].label = "Price"
        self.fields['webPage'].label = "Web page"