from django.db import models
from orders.models import Order
from store.models import Product, Category
# Create your models here.

class manage(models.Model):
    orders = models.ForeignKey(Order, on_delete=models.CASCADE, related_name='ad_order')
    categories = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='ad_cate')
    products = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='ad_product')
    name = models.CharField(max_length=50)
    # class Meta:
    #     ordering = ('order',)
    #     verbose_name = 'admin'
    #     verbose_name_plural = 'admins'

class CreateCate(models.Model):
    name = models.CharField(max_length=100)
    slug = models.SlugField(unique=True, max_length=100, db_index=True, null=True)
    class Meta:
       ordering = [ 'name', 'slug']

class PostCate(models.Model):
    name = models.CharField(max_length=100)
    class Meta:
        ordering = [ 'name',]

 