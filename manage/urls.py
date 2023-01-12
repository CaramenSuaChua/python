from django.urls import path
from manage import views
app_name = 'manage'
urlpatterns = [
    path('', views.Manage.as_view(), name='manage'),
   
]