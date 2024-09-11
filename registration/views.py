from django.shortcuts import render

# Create your views here.
def home(request):
    context ={}
    return render(request, "store/index.html", context)

def shop(request):
    context ={}
    return render(request, "store/shop.html", context)

def about(request):
    context ={}
    return render(request, "store/about.html", context)

def contact(request):
    context ={}
    return render(request, "store/contact.html", context)