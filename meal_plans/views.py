from django.shortcuts import redirect
from django.shortcuts import render
from django.contrib.auth.decorators import login_required

# john added login required but it's just an extra? look up
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView

# above follows acronym crud!
from django.views.generic.list import ListView

# if you want to use a form use below
# from meal_plans.form import MealPlanForm, MealPlanDeleteForm

from meal_plans.models import MealPlan

# Create your views here.
# Create view: meal_plans/create
# form that allows user to enter name, date, and select teh recipes they want

# when the user saves the meal plan, their user object should be
# automatically saved to teh owner property of teh meal plan.
class MealPlanListView(LoginRequiredMixin, ListView):
    model = MealPlan
    template_name = "meal_plans/list.html"

    def get_queryset(self):
        return MealPlan.objects.filter(owner=self.request.user)


class MealPlanDetailView(LoginRequiredMixin, DetailView):
    model = MealPlan
    template_name = "meal_plans/detail.html"

    def get_queryset(self):
        return MealPlan.objects.filter(owner=self.request.user)


class MealPlanCreateView(LoginRequiredMixin, CreateView):
    model = MealPlan
    template_name = "meal_plans/new.html"
    fields = ["name", "date", "recipes"]
    success_url = reverse_lazy(
        "meal_plan_detail"
    )  # might not need this? unclear?

    def form_valid(self, form):
        plan = form.save(commit=False)  # prevents invalid data submission?
        plan.owner = self.request.user
        plan.save()
        form.save_m2m()  # saves many to many relationship
        return redirect("meal_plan_detail", pk=plan.id)
        # this is also accessing the database - one detail so meal_plan is singular


class MealPlanUpdateView(LoginRequiredMixin, UpdateView):
    model = MealPlan
    template_name = "meal_plans/edit.html"
    fields = ["name", "date", "owner", "recipes"]

    def get_queryset(self):
        return MealPlan.objects.filter(owner=self.request.user)
        # this filters responses and only gets MealPlan objects from owners

    def get_success_url(self) -> str:
        return reverse_lazy("meal_plan_detail", args=[self.object.id])


class MealPlanDeleteView(LoginRequiredMixin, DeleteView):
    model = MealPlan
    template_name = "meal_plans/delete.html"

    def get_queryset(self):
        return MealPlan.objects.filter(owner=self.request.user)

    # def form_valid(self, form):
    #     form.instance.author = self.request.user
    #     return super().form_valid(form)
