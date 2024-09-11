from django.shortcuts import render
from .models import *
# views.py
def some_view():
    from .utils import get_default_items  # Move the import inside the function
    items = get_default_items()
    # View logic here

# Create your views here.
def home(request):
    return render(request, "store/index.html")

def about(request):
    return render(request, 'store/about.html')

def contact(request):
    return render(request, 'store/contact.html')

def shop(request):
    products = Product.objects.all()
    context = {'products': products}
    return render(request, 'store/shop.html', context)

def store(request):
    items = []
    order = None  # Initialize order to avoid UnboundLocalError
    
    if request.user.is_authenticated:
        try:
            customer = request.user.customer
        except Customer.DoesNotExist:
            customer = None

        if customer:
            order, created = Order.objects.get_or_create(customer=customer, complete=False)
            items = order.orderitems_set.all()

    context = {'items': items, 'order': order}
    return render(request, 'store/store.html', context)


def checkout(request):
    order = None  # Initialize order to avoid UnboundLocalError
    
    if request.method == 'POST':
        # Code to process POST request
        items = get_items_from_request(request)
    else:
        # Ensure `items` is defined here as well
        items = get_default_items()
    
    context = {'items': items, 'order': order}
    return render(request, 'store/checkout.html', context)
