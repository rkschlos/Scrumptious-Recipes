from django.forms import ModelForm

from meal_plans.models import MealPlan


class MealPlanForm(ModelForm):
    class Meta:
        model = MealPlan
        fields = ["name", "recipes"]


class MealPlanDeleteForm(ModelForm):
    class Meta:
        model = MealPlan
        fields = []  # this is called "emptying the fields"
