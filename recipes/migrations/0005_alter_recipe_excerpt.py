# Generated by Django 4.2.15 on 2024-09-14 15:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('recipes', '0004_recipe_cooking_time_recipe_prep_time'),
    ]

    operations = [
        migrations.AlterField(
            model_name='recipe',
            name='excerpt',
            field=models.TextField(blank=True, max_length=200),
        ),
    ]
