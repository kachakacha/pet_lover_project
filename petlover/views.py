from django.shortcuts import render

# Create your views here.
# index page(homepage)
def index(request):
    return render(request,'petlover/index.html')

def category(request):
    return render(request,'petlover/category.html')