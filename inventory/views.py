from django.shortcuts import render
from . models import ItemsList, Item
from .forms import ItemForm
from django.shortcuts import get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views import generic
from django.urls import reverse_lazy


def welcome(request):
    return render(request, 'inventory/welcome.html')

@login_required(login_url='my-login')
def inventory(request):
    all_Lists = ItemsList.objects.filter(user=request.user)
    context = {'my_Lists':all_Lists}
    return render(request, 'inventory/inventory.html', context=context)

@login_required(login_url='my-login')
def list_items(request, list_slug):
    itemsList = get_object_or_404(ItemsList, slug=list_slug)
    # context information
    items = Item.objects.filter(itemsList=itemsList)
    itemsLen = len(items);
    balance = sum(items.values_list("price", flat=True))
    
             
    return render(request, 'inventory/list-items.html', {'itemsList':itemsList, 'items':items, 'balance':balance,'itemsLen':itemsLen})

@login_required(login_url='my-login')
def item_info(request, slug):
    item = get_object_or_404(Item, slug=slug)
    context = {'item':item}
    return render(request, 'inventory/item-info.html', context)

class CreateItem(LoginRequiredMixin,generic.CreateView):
    model = Item
    form_class = ItemForm
    template_name = 'inventory/item-form.html'

    def get_context_data(self, **kwargs):
        context = super(CreateItem, self).get_context_data(**kwargs)
        context["listItems_id"] = self.kwargs.get('hpk')        
        return context

    def form_valid(self, form):
        self.object = form.save(commit=False)
        itemsList = ItemsList.objects.get(id=self.kwargs.get('hpk'))
        self.object.itemsList = itemsList
        self.object.save()
        return super().form_valid(form)

@login_required(login_url='my-login')
def DeleteItem(request, itempk,list_slug):
    print('-->',itempk,list_slug)
    # Delete Item
    itemsList = ItemsList.objects.get(slug=list_slug)
    Item.objects.filter(id=itempk).delete()

    # context information
    items = Item.objects.filter(itemsList=itemsList)
    itemsLen = len(items);
    balance = sum(items.values_list("price", flat=True))
    
             
    return render(request, 'inventory/list-items.html', {'itemsList':itemsList, 'items':items, 'balance':balance,'itemsLen':itemsLen})