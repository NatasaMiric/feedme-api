# Generated by Django 3.2.18 on 2023-04-20 17:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('recipes', '0002_rename_author_recipe_owner'),
    ]

    operations = [
        migrations.AlterField(
            model_name='recipe',
            name='cooking_time',
            field=models.CharField(blank=True, max_length=10),
        ),
    ]
