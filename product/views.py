from django.shortcuts import render, get_object_or_404, HttpResponse, redirect
from .models import Category, Item, order, cart
from django.views.generic import ListView, DetailView
from django.db.models import Q
from django.urls import reverse
# Create your views here.

#def home(request):
#    return render(request, 'product/index.html')
    
def home(request):
    obj=Item.objects.all()
    return render(request, 'product/index.html', {'item': obj})

def details(request,id,slug):
    obj=get_object_or_404(Item,id=id,slug=slug)
    return render(request, 'product/details.html', {'item': obj})

def search(request):
    query=None
    result=[]
    if request.method == 'GET':
        query=request.GET.get('search')
        result=Item.objects.filter(Q(title__icontains=query) | Q(tag__icontains=query) )
        return render(request, 'product/search.html',{'query':query, 'result':result})
    
def add_to_cart(request, slug):
    user = request.user
    item = get_object_or_404(Item, slug=slug)
    cart, _ = Cart.objects.get_or_create(user=user)
    order, created = Order.objects.get_or_create(user=user, item=item)
    
    if created:
        cart.items.add(order)
        cart.save()
    else:
        order.quantity += 1
        order.Item.save()
    return redirect(reverse('details', kwargs={"slug": slug}))
        
def cart(request):
    cart = get_object_or_404(Cart, user=request.user)
    
    return render(request, 'product/cart.html', context={"orders": cart.items.all()})
      
   
def delete_cart(request):
    if cart := request.user.cart:
        cart.items.all().delete() 
        cart.delete() 
    return redirect ('datails')
   
   
#class Homeview(ListView):
    #model = Item
    #template_name = 'home.html'