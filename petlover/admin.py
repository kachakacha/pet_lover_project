from django.contrib import admin
from django.contrib import admin
from petlover.models import Category,Pet
from petlover.models import UserProfile
# Register your models here.

class PetAdmin(admin.ModelAdmin):
    list_display = ('category', 'pet_name', 'information', 'views')

# Add in this class to customise the Admin Interface
class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug':('species',)}


# Register your models here.
admin.site.register(Category, CategoryAdmin)
admin.site.register(Pet, PetAdmin)
admin.site.register(UserProfile)

