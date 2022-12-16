from django.urls import path
from .views import product_list, product_detail, product_category_list, fresh_products, contact, subscribe, search_products, searched_products

app_name = 'shop'

urlpatterns = [
    path('', product_list, name='product_list'),
    path('shop/', product_category_list, name='category'),
    path('shop/<slug:category_slug>', product_category_list, name='category'),
    path('shop/<slug:product_slug>/', product_detail, name='product'),
    path('shop/fresh-products/', fresh_products, name='fresh'),
    path('contact/', contact, name='contact'),
    path('subscribe/', subscribe, name='subscribe'),
    path('search-product/', search_products, name='search_list'),
    path('search/product/', searched_products, name='searched_products')
]
