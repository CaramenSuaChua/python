from django.shortcuts import render, get_object_or_404
from django.views import View, generic
from .models import manage, PostCate, CreateCate
from .forms import PostForm, PostCategory, CreateCategory
from django.http import HttpResponse
from store.models import Category, Product
from store.filters import ProductFilter
from django.db.models import Count
from django_filters.views import FilterView
# Create your views here.
class Manage(View):

    def get(self, request):
        return render(request, 'index.html')
