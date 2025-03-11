from . import views
from django.urls import path

urlpatterns = [
    path('', views.ProductsList.as_view(), name='products_list'),
    path('add/', views.CreateProduct.as_view(), name='product_add'),
]