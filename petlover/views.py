from django.shortcuts import render
from petlover.models import Category, Pet

# Create your views here.
# index page(homepage)
def index(request):
    return render(request,'petlover/index.html')


def show_category(request, category_name_slug):
    context_dict = {}
    try:
        category = Category.objects.get(slug=category_name_slug)
        pet = Pet.objects.filter(category=category)
        context_dict['pet'] = pet
        context_dict['category'] = category

    except Category.DoesNotExist:
        context_dict['category'] = None
        context_dict['pages'] = None
    return render(request, 'petlover/category.html', context=context_dict)