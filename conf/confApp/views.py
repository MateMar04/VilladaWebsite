from django.shortcuts import render


# Create your views here.

def navbar_view(request):
    return render(request, "navbar.html")


def carousel_view(request):
    return render(request, "carousel.html")
