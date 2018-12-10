from .models import Product, Capital, Categories, SingleDayTransaction
from rest_framework import serializers
from django.contrib.auth.models import User

class UserSerializer(serializers.ModelSerializer):
	class Meta:
		model = User
		fields = ('id', 'username', 'email')

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ('id', 'user', 'no_of_sales', 'category', 'cost_amt', 'sales_amt', 'product_name', 'quantity', 'out_of_stock', 'credit', 'created', 'modified', 'creditor_name')

class CapitalSerializer(serializers.ModelSerializer):
    class Meta:
        model = Capital
        fields = ('amt', 'user')

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Categories
        fields = ('category', 'id')

class SingleDayTransactionSerializer(serializers.ModelSerializer):
    class Meta:
        model = SingleDayTransaction
        fields = ('total_sales','date')