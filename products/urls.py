from django.urls import path
from . import views

urlpatterns = [
    # Product listing and detail views
    path('', views.all_products, name='products'),
    path('<int:product_id>/', views.product_detail, name='product_detail'),
    path('categories/', views.all_categories, name='all_categories'),
    path('category/<slug:category_slug>/', views.category_products, name='category_products'),

    # Product management
    path('add/', views.add_product, name='add_product'),
    path('edit/<int:product_id>/', views.edit_product, name='edit_product'),
    path('delete/<int:product_id>/', views.delete_product, name='delete_product'),

    # Product images
    path('add_image/<int:product_id>/', views.add_product_image, name='add_product_image'),
    path('delete_image/<int:image_id>/', views.delete_product_image, name='delete_product_image'),


    # API endpoints (if needed)
    # path('api/products/', views.product_list_api, name='product_list_api'),
    # path('api/products/<int:product_id>/', views.product_detail_api, name='product_detail_api'),
]
