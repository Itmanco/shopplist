from django.shortcuts import render
from . models import ItemsList, Item, Guest
from .forms import ItemForm, ListitemForm
from django.shortcuts import get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views import generic
from django.urls import reverse_lazy
import cloudinary.api
from django.contrib.auth import get_user_model
User = get_user_model()


def welcome(request):
    return render(request, 'inventory/welcome.html')

@login_required(login_url='my-login')
def inventory(request):
    all_Lists = ItemsList.objects.filter(user=request.user)
    context = {
        'my_Lists':all_Lists
    }
    return render(request, 'inventory/inventory.html', context=context)

@login_required(login_url='my-login')
def list_items(request, list_slug):

    context = _listViewContext(request, list_slug)    
             
    return render(request, 'inventory/list-items.html', context)

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


class CreateList(LoginRequiredMixin,generic.CreateView):
    model = ItemsList
    form_class = ListitemForm
    template_name = 'inventory/listitem-form.html'

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.user = self.request.user
        self.object.save()
        return super().form_valid(form)

class UpdateItem(LoginRequiredMixin, generic.UpdateView):
    model = Item
    template_name = 'inventory/item-update.html'
    fields = ['title','brand', 'description','price','image','webPage','store']

    def get_queryset(self):
        queryset = super().get_queryset()
        return queryset.filter(id=int(self.kwargs.get('pk')))

@login_required(login_url='my-login')
def DeleteList(request,list_slug):
    # # Delete items images
    # items =  list(Item.objects.filter(itemsList__slug=list_slug))
    # for item in items:
    #     imageloc = item.image.path
    #     if os.path.isfile(imageloc):
    #          os.remove(imageloc)
    # Delete images using cloudinary
    items =  list(Item.objects.filter(itemsList__slug=list_slug))
    for item in items:
        if item.image:
            cloudinary.api.delete_resources(item.image, resource_type="image", type="upload")
    # Delete Item
    ItemsList.objects.filter(slug=list_slug).delete()
    all_Lists = ItemsList.objects.filter(user=request.user)
    context = {
        'my_Lists':all_Lists
    }
    return render(request, 'inventory/inventory.html', context=context)

@login_required(login_url='my-login')
def GuestsList(request,list_slug):
    listItem = ItemsList.objects.get(slug=list_slug)
    guests =  list(Guest.objects.filter(itemsList__slug=list_slug))
    users = list(User.objects.all().exclude(id=request.user.id))

    # removing user that already exists in the guests list
    for value in guests:
        users.remove(value.user)


    context = {
        'listItem':listItem,
        'guests':guests,
        'users':users
    }
    print(context)
    return render(request, 'inventory/_guests.html', context=context)

@login_required(login_url='my-login')
def DeleteItem(request, itempk,list_slug):
    # # Delete image
    
    item =  Item.objects.get(id=itempk)
    if item.image:
        imageloc = item.image
        print('Image-->>',item.image)
        # if os.path.isfile(imageloc):
        #     os.remove(imageloc)
        # Delete image from cloudinary
        cloudinary.api.delete_resources(imageloc, resource_type="image", type="upload")
    # Delete Item
    Item.objects.filter(id=itempk).delete()   

    context = _listViewContext(request, list_slug)    
             
    return render(request, 'inventory/list-items.html', context)

@login_required(login_url='my-login')
def MarkBoughtItem(request, itempk,list_slug):
    # update Item
    itemsList = ItemsList.objects.get(slug=list_slug)
    item = Item.objects.filter(id=itempk)

    item.update(bought = 'True')  

    context = _listViewContext(request, list_slug)    
             
    return render(request, 'inventory/list-items.html', context)

@login_required(login_url='my-login')
def ReturnItemToList(request, itempk,list_slug):
    # update Item
    itemsList = ItemsList.objects.get(slug=list_slug)
    item = Item.objects.filter(id=itempk)

    item.update(bought = 'False')  

    context = _listViewContext(request, list_slug)    
             
    return render(request, 'inventory/list-items.html', context)


    # prepares the list-items view context and return it
def _listViewContext(request,list_slug):
    itemsList = get_object_or_404(ItemsList, slug=list_slug)
    items = Item.objects.filter(itemsList=itemsList).filter(bought='False')
    boughtItems = Item.objects.filter(itemsList=itemsList).filter(bought='True')
    spent = sum(boughtItems.values_list("price", flat=True))
    boughtItemsLen = len(boughtItems)
    itemsLen = len(items)
    balance = sum(items.values_list("price", flat=True))
    isListOwner = itemsList.user == request.user
    return {
        'itemsList':itemsList, 
        'items':items, 
        'balance':balance,
        'itemsLen':itemsLen, 
        'boughtItems':boughtItems, 
        'boughtItemsLen':boughtItemsLen,
        'spent':spent,
        'isListOwner':isListOwner,
        }