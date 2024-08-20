from django.urls import path
from product import views
from product import auth
urlpatterns = [
    path('', views.ProductListView.as_view(), name='product_list'),
    path('<int:product_id>/', views.ProductDetailView.as_view(), name='product_detail'),
    path('create/', views.ProductCreateView.as_view(), name='product_create'),
    path('<int:product_id>/edit/', views.ProductUpdateView.as_view(), name='product_update'),
    path('<int:product_id>/delete/', views.ProductDeleteView.as_view(), name='product_delete'),
    # path('grid/<int:product_id>/', views.ProductGridView.as_view(), name='product_grid') ,

    path('login-page/', auth.login_page, name='login_page'),
    path('register-page/', auth.register_page, name='register_page'),
    path('logout_page/', auth.login_page, name='logout_page')
]