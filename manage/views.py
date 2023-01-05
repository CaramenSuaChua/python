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
    model = manage
    def get(self, request):
        return render(request, 'manage/store_admin.html')

class Manage_Product(generic.ListView, ):
    template_name = 'manage/category_list.html'
    context_object_name = 'categories'
    queryset = Category.objects.all().annotate(num_products=Count('products'))

class Store_List(FilterView):
    model = Product
    queryset = Product.objects.all()
    paginate_by = 10
    filterset_class = ProductFilter
    context_object_name = 'products'
    template_name = 'manage/store_list.html'

class StoreDetail(generic.DetailView):
    model = Product
    templates_name = 'manage/store_detail.html'
    context_object_name = 'product'

class CateCreate(generic.CreateView):
    model = CreateCategory
    fields = ['name', 'slug',]
    templates_name ='manage/category_list.html'
    def post(self, request):
        form = CreateCate.objects.create()
        form.name = request.POST['name']
        form.save()
        print(form)
        # print(request.POST['name'])
        return render(request, 'manage/category_list.html', {'form' : form} )
    
class CateEdit(generic.UpdateView):
    model = PostCategory
    fields = ['name', ]
    success_url ="categories/" 
    template_name_suffix = '_update_form' 
    
    def post(self, request, cate_id):
        c =  Category.objects.get(pk=cate_id)
        c.name = request.POST[str(cate_id)]
        c.save()
        return render(request, 'manage/category_list.html', {'c': c})

class CateDel(generic.DeleteView):
    model = PostCategory
    fields = ['name', ]
    success_url ="/" 
    template_name_suffix = '_update_form' 
    
    def post(self, request, cate_id):
        c =  Category.objects.get(pk=cate_id).delete()
        return render(request, 'manage/category_list.html', {'c': c})

