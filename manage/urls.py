from django.urls import path
from manage import views
app_name = 'manage'
urlpatterns = [
    path('', views.Manage.as_view(), name='manage'),
    path('store/', views.Store_List.as_view(), name='store_list'),
    path('store/<slug:slug>/', views.StoreDetail.as_view(),
         name='store_detail'),
    path('categories/', views.Manage_Product.as_view(), name='product_list'),
    path('cr_categories/', views.CateCreate.as_view(), name='create_category'),
    path('categories/<int:cate_id>', views.CateEdit.as_view(), name='post_category'),
    path('cate_del/<int:cate_id>', views.CateDel.as_view(), name='delete_category'),
]