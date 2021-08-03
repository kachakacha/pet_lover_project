from django.contrib.auth.models import User
from django.shortcuts import render
from petlover.models import Category, Pet, UserProfile
from petlover.forms import UserForm, UserProfileForm

from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponse
from django.urls import reverse
from django.shortcuts import redirect
from django.contrib.auth.decorators import login_required


# Create your views here.
# index page(homepage)
def index(request):
    category_list = Category.objects.all()[:]
    context_dict = {}
    context_dict['categories'] = category_list

    return render(request, 'petlover/index.html', context=context_dict)


def show_category(request, category_name_slug):
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


def show_pets(request, category_name_slug, pet_name_slug):
    context_dict = {}
    try:
        category = Category.objects.get(slug=category_name_slug)
        pet = Pet.objects.get(slug=pet_name_slug)
        context_dict['pet'] = pet
        context_dict['category'] = category

    except Pet.DoesNotExist:
        context_dict['category'] = None
        context_dict['pet'] = None

    return render(request, 'petlover/pet_intro.html', context=context_dict)

def register(request):
    registered = False

    if request.method == 'POST':
        user_form = UserForm(request.POST)
        profile_form = UserProfileForm(request.POST)

        if user_form.is_valid() and profile_form.is_valid():
            user = user_form.save()

            user.set_password(user.password)
            user.save()

            profile = profile_form.save(commit=False)
            profile.user = user

            if 'picture' in request.FILES:
                profile.picture = request.FILES['picture']

            profile.save()
            registered = True

        else:
            print(user_form.errors, profile_form.errors)

    else:
        user_form = UserForm()
        profile_form = UserProfileForm()

    return render(request,
                  'petlover/register.html',
                  context={'user_form': user_form,
                           'profile_form': profile_form,
                           'registered': registered})


def user_login(request):
    if request.method == 'POST':

        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(username=username, password=password)

        if user:

            if user.is_active:
                login(request, user)
                return redirect(reverse('petlover:index'))
            else:
                return HttpResponse("Your  account is disabled.")

        else:
            print(f"Invalid login details: {username}, {password}")
            return HttpResponse("Invalid login details supplied.")
    else:
        return render(request, 'petlover/login.html')