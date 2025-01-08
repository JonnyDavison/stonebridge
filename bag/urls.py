from django.urls import path
from . import views

urlpatterns = [
    path('', views.bag, name='bag'),  # View the shopping bag
    path('add/<item_id>/', views.add_to_bag, name='add_to_bag'),  # Add an item to the bag
    path('adjust/<item_id>/', views.adjust_bag, name='adjust_bag'),  # Adjust item quantity in the bag
    path('remove/<item_id>/', views.remove_from_bag, name='remove_from_bag'),  # Remove an item from the bag
]
