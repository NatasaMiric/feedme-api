from django.db import models
from django.contrib.auth.models import User


class Recipe(models.Model):
    """
    Recipe model, related to User instance.
    Default image set so that we can always reference image.url.
    """

    CATEGORIES = [
        ('appetizer', 'Appetizer'),
        ('main course', 'Main course'),
        ('dessert', 'Dessert'),
        ('side dish', 'Side dish'),
        ('beverage', 'Beverage'),
        ('bread', 'Bread'),
        ('snack', 'Snack'),
        ('vegetarian', 'Vegetarian'),
        ('condiments', 'Condiments'),
        ('breakfast', 'Breakfast'),
        ('luch', 'Lunch'),
        ('dinner', 'Dinner')
    ]

    DIFFICULTY = [
        ('easy', 'Easy'),
        ('moderate', 'Moderate'),
        ('hard', 'Hard')
    ]

    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=150)
    ingredients = models.TextField(blank=True)
    instructions = models.TextField(blank=True)
    category = models.CharField(max_length=25, choices=CATEGORIES, default='')
    difficulty = models.CharField(
        max_length=25, choices=DIFFICULTY, default=''
        )
    cooking_time = models.CharField(max_length=10, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    recipe_image = models.ImageField(
        upload_to='images/', default='../default_recipeimage_zn2eid',
        blank=True
    )

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return f'{self.id} {self.title}'
