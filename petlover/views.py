from django.shortcuts import render
from petlover.models import Category, Pet

# Create your views here.
# index page(homepage)
def index(request):
    category_list = Category.objects.all()[:]
    context_dict={}
    context_dict['categories']=category_list

    return render(request,'petlover/index.html', context=context_dict)



def show_category(request,category_name_slug):
    context_dict = {}
    try:
        category = Category.objects.get(slug=category_name_slug)
        pets = Pet.objects.filter(category=category)
        context_dict['pets'] = pets
        context_dict['category'] = category

    except Category.DoesNotExist:
        context_dict['category'] = None
        context_dict['pets'] = None
    return render(request, 'petlover/category.html', context=context_dict)

def show_pets(request,category_name_slug,pet_name_slug):
    context_dict = {}
    try:
        category = Category.objects.get(slug=category_name_slug)
        pet = Pet.objects.get(slug=pet_name_slug)
        context_dict['pet']=pet
        context_dict['category'] = category

    except Pet.DoesNotExist:
        context_dict['category'] = None
        context_dict['pet'] = None

    return render(request, 'petlover/pet_intro.html', context=context_dict)

