from django.views.generic import DetailView, ListView
from .models import Tovar, Category
# from .forms import TovarForm, CategoryForm


class TovarListView(ListView):
    model = Tovar

class TovarDetailView(DetailView):
    model = Tovar

class CategoryListView(ListView):
    model = Category

class CategoryDetailView(DetailView):
    model = Category
