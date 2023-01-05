from django import forms
from .models import manage, PostCate, CreateCate

class PostForm(forms.ModelForm):
    class Meta:
        model = manage
        fields = ('orders', 'products', 'categories',)

class CreateCategory(forms.ModelForm):
    class Meta:
        model = CreateCate
        fields = ('name', 'slug')
class PostCategory(forms.ModelForm):
    class Meta:
        model = PostCate
        fields = ('name', )