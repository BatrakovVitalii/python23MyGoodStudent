from django.shortcuts import render
from interface.models import Product
from core.models import Profile


# Create your views here.
def home(request):
    products = Product.objects.all()
    return render(
        request,
        'core/home.html',
        {
            "products": products
        }
    )

def profile(request):
    profiles = Profile.objects.all()
    return render(
        request,
        'Interface/profile.html',
        {
            "profiles": profiles
        }
    )
