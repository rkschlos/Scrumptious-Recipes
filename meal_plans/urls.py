from django.urls import path

from meal_plans.views import (
    MealPlanListView,
    MealPlanCreateView,
    MealPlanDetailView,
    MealPlanUpdateView,
    MealPlanDeleteView,
)

# RecipeDetailView is a placeholder path

urlpatterns = [  # these names are arbitrary, just connecting view to url
    path(
        "",
        MealPlanListView.as_view(),
        name="meal_plan_list",
    ),
    path(
        "<int:pk>/",  # unique id for this specific meal plan
        MealPlanDetailView.as_view(),
        name="meal_plan_detail",
    ),
    path(
        "create/",
        MealPlanCreateView.as_view(),
        name="meal_plan_new",
    ),
    path(
        "<int:pk>/edit/",
        MealPlanUpdateView.as_view(),
        name="meal_plan_edit",
    ),
    path(
        "<int:pk>/delete/",
        MealPlanDeleteView.as_view(),
        name="meal_plan_delete",
    ),
]

# 5 paths it supports
# meal_plans/ (show a list of meal plans created by the user)
# meal_plans/create/ Show a form that allows a user to create a meal plan
# meal_plans/<int:pk>/   Show the details of one of the user's meal plans
# meal_plans/<int:pl>/edit/ Show an edit form to edit one of their meal plans
# meal_plans/<int:pk>/delete/    Show a form that allows a user to delete a meal plan
