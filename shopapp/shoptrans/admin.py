from django.contrib import admin
from .models import Product, Categories, Capital, SingleDayTransaction
# Register your models here.
admin.site.register(Product)
admin.site.register(SingleDayTransaction)

admin.site.register(Categories)
admin.site.register(Capital)
