from django.shortcuts import render

# Create your views here.
def index(request, *agrs, **kwargs):
    return render(request, "frontend/index.html")
