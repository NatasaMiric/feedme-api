# Generated by Django 3.2.18 on 2023-04-19 17:10

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Recipe',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=150)),
                ('ingredients', models.TextField(blank=True)),
                ('instructions', models.TextField(blank=True)),
                ('category', models.CharField(choices=[('appetizer', 'Appetizer'), ('main course', 'Main course'), ('dessert', 'Dessert'), ('side dish', 'Side dish'), ('beverage', 'Beverage'), ('bread', 'Bread'), ('snack', 'Snack'), ('vegetarian', 'Vegetarian'), ('condiments', 'Condiments'), ('breakfast', 'Breakfast'), ('luch', 'Lunch'), ('dinner', 'Dinner')], default='', max_length=25)),
                ('difficulty', models.CharField(choices=[('easy', 'Easy'), ('moderate', 'Moderate'), ('hard', 'Hard')], default='', max_length=25)),
                ('cooking_time', models.IntegerField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('recipe_image', models.ImageField(blank=True, default='../default_recipeimage_zn2eid', upload_to='images/')),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['-created_at'],
            },
        ),
    ]