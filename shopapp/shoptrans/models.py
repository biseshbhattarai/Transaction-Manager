from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from django.utils import timezone
# class Cost(models.Model):
#     cost_amt = models.CharField(max_length=22222)
#     sale = models.ForeignKey(Sale, on_delete=models.CASCADE)

#     def __str__(self):
#         return self.cost_amt

# class Sales(models.Model):
#     sales_amt = models.CharField(max_length=22222)
    

#     def __str__(self):
#         return self.sales_amt

class Categories(models.Model):
    category = models.CharField(max_length=222)
    

    def __str__(self):
        return self.category
    
class Product(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    no_of_sales = models.IntegerField(default=0)
    category = models.ForeignKey(Categories, on_delete=models.CASCADE)
    cost_amt = models.IntegerField(default=0)
    sales_amt = models.IntegerField(default=0)
    product_name = models.CharField(max_length=2222)
    quantity = models.IntegerField(default=0)
    out_of_stock = models.BooleanField(default=False)
    credit = models.BooleanField(default=False)
    bought = models.BooleanField(default=False)
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)

    class Meta:
        get_latest_by = 'modified'
    
    # no_of_credit = models.IntegerField(default=0)
    def __int__ (self):
        return int(self.quantity)
    
    def sales(arg, value):
        return arg* value

    def remaining_stock(arg, value):
        if arg >=  value:
            Product.out_of_stock = True
            return Product.out_of_stock

    def profit(arg, value):
        return ((arg - value) / value ) * 100
        
    
    def loss(arg, value):
        return ((arg - value) / arg) * 100
        

    def get_absolute_url(self):
        return reverse('main')

  
    def expense(arg, value):
        return arg * value

    def check_for_first_added(arg):
        if arg > 0:
            Product.bought = True
            return Product.bought


    

class Capital(models.Model):
    amt = models.IntegerField(default=0)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __int__ (self):
        return self.amt

    def remaining_capital(arg, value):
        return arg - value 