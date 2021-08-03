from django.shortcuts import render
from petlover.models import Category, Pet

# Create your views here.
# index page(homepage)
def index(request):
    category_list = Category.objects.all()[:]
    context_dict={}
    context_dict['categories']=category_list

    return render(request,'petlover/index.html', context=context_dict)



def show_category(request,pet_name_slug):
    context_dict = {}
    try:
        category = Category.objects.get(slug=category_prname_slug)
        pages = Page.objects.filter(category=category)
        context_dict['pages'] = pages
        context_dict['category'] = category

    except Category.DoesNotExist:
        context_dict['category'] = None
        context_dict['pages'] = None
    return render(request, 'rango/category.html', context=context_dict)
