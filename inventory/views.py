from django.shortcuts import render
from . models import ItemsList, Item
from django.shortcuts import get_object_or_404

def inventory(request):
    all_Lists = ItemsList.objects.all()
    context = {'my_Lists':all_Lists}
    return render(request, 'inventory/inventory.html', context=context)