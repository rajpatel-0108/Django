import code
import imp
from operator import mod
from tabnanny import verbose
from tkinter import CASCADE
from turtle import title
from unicodedata import name
from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from django.urls import reverse
from django.utils.text import slugify

# Create your models here.

class Country(models.Model):
    name=models.CharField(max_length=50)
    code=models.CharField(max_length=2)

    def __str__(self):
        return self.name
    class Meta:
        verbose_name_plural = "Countries"

class Address(models.Model):
    street = models.CharField(max_length=80)
    zipcode = models.CharField(max_length=5)
    city = models.CharField(max_length=50)


    def full_address(self):
        return f" {self.street} {self.city} {self.zipcode} "
    
    def __str__(self):
        return self.full_address()

    class Meta:
        verbose_name_plural = "Address Entries"

class Author(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    address = models.OneToOneField(Address, on_delete=models.CASCADE, null=True)


    def full_name(self):
        return f" {self.first_name} {self.last_name} "

    def __str__(self):
        return self.full_name()

class Book(models.Model):
    title = models.CharField(max_length=50)
    rating = models.IntegerField(
        validators=[MinValueValidator(1), MaxValueValidator(5)])
    author = models.ForeignKey(Author, on_delete=models.CASCADE, null=True, related_name="books")
    is_bestselling = models.BooleanField(default=False)
    slug = models.SlugField(default="",blank=True,null=False, db_index=True)
    published_country = models.ManyToManyField(Country,null=False)

    def get_absolute_url(self):
        return reverse("book-detail", args=[self.slug])
    
    def save(self):
        self.slug = slugify(self.title)
        super().save()

    def __str__(self):
        return f" {self.title} ({self.rating})"
