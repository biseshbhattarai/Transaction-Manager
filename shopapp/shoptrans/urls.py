from django.urls import path
from . import views
from .views import  CreateTransaction, ProductUpdateView, ProductApiView, CapitalApiView, CategoryApiView, ProductDetailView

urlpatterns = [

    path('',views.main, name="main"),
    path('<int:pk>/', views.transaction, name="product"),
    path('<int:pk>/update/', ProductUpdateView.as_view(), name="update"),
    path('add/', CreateTransaction.as_view(), name="add"),
    path('dashboard/', views.dashboard_view, name="dashboard"),
    path('products/', ProductApiView.as_view(), name="api-product"),
    path('product/<int:pk>/', ProductDetailView.as_view(), name="api-detail"),
    path('capital/', CapitalApiView.as_view(), name="api-capital"),
    path('category/', CategoryApiView.as_view(), name="api-category")


]
