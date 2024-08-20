from django.contrib import admin
from django.urls import path

from customers.views import views

urlpatterns = [
    path('customers/', views.CustomerListView.as_view(), name='customers'),
    path('customer-details/<slug:customer_slug>/', views.CustomerDetailView.as_view(), name='customer_details'),
    path('add-customer/', views.CustomerCreateView.as_view(), name='add_customer'),
    path('edit-customer/<slug:customer_slug>/', views.CustomerUpdateView.as_view(), name='edit_customer'),
    path('delete-customer/<slug:customer_slug>/', views.CustomerDeleteView.as_view(), name='delete_customer'),



]
