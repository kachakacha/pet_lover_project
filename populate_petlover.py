import os

os.environ.setdefault('DJANGO_SETTINGS_MODULE',
                      'pet_lover_project.settings')
import django

django.setup()
from petlover.models import Category, Pet


def populate():
    # First, we will create lists of dictionaries containing the pages
    # we want to add into each category.
    # Then we will create a dictionary of dictionaries for our categories.
    # This might seem a little bit confusing, but it allows us to iterate
    # through each data structure, and add the data to our models.
    dog = [
        {'pet_name': 'American Bulldog',
         'InformationContent': 'The American Bulldog is stocky and muscular, but also agile and built for chasing down straycattle and helping with farm work. In fact, some are known to jump six feet or more into the air.American Bulldogs are intelligent and affectionate, which makes them great, protective family dogs; although, they have high exercise needs and require an experienced, active pet parent. They can vary in appearance, as there are multiple types, including the Bully or Classic type, also known as the Johnson type, the Standard or Performance type, also called the Scott type, and hybrids of the two.',
         'views': 3843},
        {'pet_name': 'Bichon Frise',
         'InformationContent': 'The Bichon Frise is a cheerful, small dog breed with a love of mischief and a lot of love to give. With their black eyes and fluffy white coat, the Bichon looks almost like a child’s toy.Even though these are purebred dogs, you may find them in the care of shelters or rescue groups. Remember to adopt! Don’t shop if you want to bring a dog home.',
         'views': 6123}]

    cat = [
        {'pet_name': '1',
         'InformationContent': '11',
         'views': 8235},
        {'pet_name': '2',
         'InformationContent': '22',
         'views': 1235},
    ]

    bird = [
        {'pet_name': '3',
         'InformationContent': '33',
         'views': 1235},
        {'pet_name': '4',
         'InformationContent': '44',
         'views': 8442}]

    rabbit = [{'pet_name': '5',
                'InformationContent': '55',
                'views': 1234},
               {'pet_name': '6',
                'InformationContent': '66',
                'views': 9903}]

    category = {'Dogs': {'pet': dog},
                'Cats': {'pet': cat},
                'Rabbits': {'pet': rabbit},
                'Birds':{'pet':bird}}

    # If you want to add more pets,
    # add them to the dictionaries above.

    # The code below goes through the category dictionary, then adds each category,
    # and then adds all the associated pets for that category.
    for cat, cat_data in category.items():
        c = add_category(cat)
        for p in cat_data['pet']:
            add_pet(c, p['pet_name'], p['InformationContent'], views=p['views'])

    # Print out the categories we have added.
    for c in Category.objects.all():
        for p in Pet.objects.filter(category=c):
            print(f'- {c}: {p}')


def add_pet(category, pet_name, information_content, views=0):
    p = Pet.objects.get_or_create(category=category, pet_name=pet_name)[0]
    p.information=information_content
    p.views = views
    p.save()
    return p


def add_category(species):
    c = Category.objects.get_or_create(species=species)[0]
    c.species = species
    c.save()
    return c


if __name__ == '__main__':
    print('Starting petlover population script...')
    populate()
