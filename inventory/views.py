from django.shortcuts import render
from . models import ItemsList, Item
from django.shortcuts import get_object_or_404
from django.contrib.auth.decorators import login_required


def welcome(request):
    return render(request, 'inventory/welcome.html')

@login_required(login_url='my-login')
def inventory(request):
    all_Lists = ItemsList.objects.all()
    context = {'my_Lists':all_Lists}
    return render(request, 'inventory/inventory.html', context=context)