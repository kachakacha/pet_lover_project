from django.db import models
from django.template.defaultfilters import slugify
from django.contrib.auth.models import User


# Create your models here.
class Category(models.Model):
    NAME_MAX_LENGTH = 128
    TEXT_MAX_LENGTH = 512
    species = models.CharField(max_length=NAME_MAX_LENGTH, unique=True)
    description = models.TextField(max_length=TEXT_MAX_LENGTH, unique=False)
    slug = models.SlugField()

    def save(self, *args, **kwargs):
        self.slug = slugify(self.species)
        super(Category, self).save(*args, **kwargs)

    class Meta:
        verbose_name_plural = 'Categories'

    def __str__(self):
        return self.species


class Pet(models.Model):
    NAME_MAX_LENGTH = 128
    TEXT_MAX_LENGTH = 512

    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    pet_name = models.CharField(max_length=NAME_MAX_LENGTH, unique=True)
    information = models.TextField(max_length=TEXT_MAX_LENGTH)
    picture_of_pet = models.ImageField(default=0)
    views = models.IntegerField(default=0)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.pet_name)
        super(Pet, self).save(*args, **kwargs)

    def __str__(self):
        return self.pet_name

# pics uploaded by user
class Pic_of_pet(models.Model):

    Pet = models.ForeignKey(Pet, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    pictures = models.ImageField(default=0)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.pictures)
        super(Pic_of_pet, self).save(*args, **kwargs)

    def __str__(self):
        return self.Pet.pet_name, self.user.username


# information edited by user
class Intro_of_pet(models.Model):
    TEXT_MAX_LENGTH = 512
    UserName = models.ForeignKey(User, on_delete=models.CASCADE)
    InformationContent = models.TextField(max_length=TEXT_MAX_LENGTH)
    pet = models.ForeignKey(Pet, on_delete=models.CASCADE)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.InformationContent)
        super(Intro_of_pet, self).save(*args, **kwargs)

    def __str__(self):
        return self.Pet.pet_name, self.user.username

# users' profile when registered
class UserProfile(models.Model):
    EMAIL_MAX_LENGTH=128
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    # The additional attributes we wish to include.
    email = models.CharField(max_length=EMAIL_MAX_LENGTH, blank=True)

    def __str__(self):
        return self.user.username
