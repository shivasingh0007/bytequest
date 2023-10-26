from django.contrib import admin
from django.urls import path
from proapp import views
# from .views import CategoryCreate

urlpatterns = [
    # path('admin/', admin.site.urls),
    path('register/', views.UserCreateView.as_view(), name='user-register'),
    path('category',views.CategoryCreate.as_view(),name="category-create"),
    path('category/<int:pk>',views.CategoryUpdateDestroy.as_view(),name='category-destroy'),
    path('product',views.ProductsCreate.as_view(),name="product-create"),
    path('product/<int:pk>',views.ProductsUpdateDestroy.as_view(),name='product-destroy')
]
