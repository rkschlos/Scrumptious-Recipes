from django.db import models
from django.conf import settings  # to access authentication in settings

USER_MODEL = settings.AUTH_USER_MODEL

# Create your models here.
class MealPlan(models.Model):
    name = models.CharField(max_length=120)
    date = models.DateField  # date for when meal will be served
    owner = models.ForeignKey(
        USER_MODEL,
        related_name="meal_plans",
        on_delete=models.CASCADE,
        null=True,
    )
    recipes = models.ManyToManyField(
        "recipes.Recipe", related_name="meal_plans"
    )


# you can have the same related names in the same class, but
# different classes with the same related will trhow errors.
