from django.contrib import admin


# Register your models here.
from recipes.models import Recipe, Measure, FoodItem, Ingredient, Step

admin.site.register(Recipe)
admin.site.register(Measure)
admin.site.register(FoodItem)
admin.site.register(Ingredient)
admin.site.register(Step)
