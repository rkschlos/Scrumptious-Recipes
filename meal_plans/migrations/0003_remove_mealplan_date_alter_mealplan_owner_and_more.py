# Generated by Django 4.0.3 on 2022-03-17 18:14

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('recipes', '0008_recipe_author'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('meal_plans', '0002_alter_mealplan_date'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='mealplan',
            name='date',
        ),
        migrations.AlterField(
            model_name='mealplan',
            name='owner',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='meal_plans', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='mealplan',
            name='recipes',
            field=models.ManyToManyField(related_name='meal_plans', to='recipes.recipe'),
        ),
    ]
