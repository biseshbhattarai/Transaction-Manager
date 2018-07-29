from .models import Product, Capital, Categories
from rest_framework import serializers

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ('id', 'user', 'no_of_sales', 'category', 'cost_amt', 'sales_amt', 'product_name', 'quantity', 'out_of_stock', 'credit', 'created', 'modified')

class CapitalSerializer(serializers.ModelSerializer):
    class Meta:
        model = Capital
        fields = ('amt', 'user')

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Categories
        fields = ('category',)