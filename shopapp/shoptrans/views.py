from django.shortcuts import render
from .models import Product, Capital, Categories
from .serializer import ProductSerializer, CapitalSerializer, CategorySerializer
from django.views.generic.edit import CreateView, UpdateView
from django.contrib.auth.models import User
from django.db.models import Q
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from rest_framework import generics

def main(request):
    capitals = Capital.objects.all()
    products = Product.objects.all()
    query = request.GET.get("q")
    if query:
        products = products.filter(
            Q(product_name__icontains=query)
        ).distinct()
    paginator = Paginator(products, 12)
    page_request_var = 'page'
    page = request.GET.get(page_request_var)
    try:
        queryset = paginator.page(page)
    except PageNotAnInteger:
        queryset = paginator.page(1)
    except EmptyPage:
        queryset = paginator.page(paginator.num_pages)
    sales_amt = [product.sales_amt for product in Product.objects.all()]
    no_of_sales = [product.no_of_sales for product in Product.objects.all()]
    total_no_of_sales = sum(no_of_sales)
    total_sales = sum(sales_amt)


    final_sales = Product.sales(total_sales, total_no_of_sales)
    cost_amt = [product.cost_amt for product in Product.objects.all()]
    total_cost = sum(cost_amt)
    quantity = [product.quantity for product in Product.objects.all()]
    total_quantity = sum(quantity)
    print(total_quantity)
    # for product in Product.objects.all():
    #     out_of_stock = Product.remaining_stock(
    #         product.no_of_sales, product.quantity)
  
  
    return render(request, 'shoptrans/main.html', {
        'products': products,
        # 'not_bought':not_bought,
        "page_request_var": page_request_var,
        "object_list": queryset,
        # 'out_of_stock':out_of_stock
       
    })


def transaction(request, pk=None):
    product = Product.objects.get(pk=pk)
    capitals = Capital.objects.all()
    sales = Product.sales(product.sales_amt, product.no_of_sales)
    expenses = Product.expense(product.cost_amt, product.quantity)
    not_bought = Product.check_for_first_added(product.no_of_sales)
    if sales > expenses:
        profit = Product.profit(sales, expenses)
    elif sales < expenses:
        loss = Product.loss(expenses, sales)
        profit = 100 - loss
   
    out_of_stock = Product.remaining_stock(
        product.no_of_sales, product.quantity)
    sales = Product.sales(product.no_of_sales, product.sales_amt)
    remaining_quantity = product.quantity - product.no_of_sales
    context = {'product': product, 'sales': sales,
               "out_of_stock": out_of_stock, "profit": profit, 'remaining_quantity':remaining_quantity, 'not_bought':not_bought}
    return render(request, 'shoptrans/product.html', context)


class CreateTransaction(CreateView):
    model = Product
    fields = [
        'user',
        'no_of_sales',
        'cost_amt',
        'sales_amt',
        'category',
        'product_name',
        'quantity',
    ]


class ProductUpdateView(UpdateView):
    model = Product
    template_name_suffix = '_update_form'
    fields = [
        'no_of_sales',
        'credit'
    ]


def dashboard_view(request):
    transaction = Product.objects.latest()
    tuna = []
    for product in Product.objects.all():
        final_sales = Product.sales(product.sales_amt, product.no_of_sales)
        tuna.append(final_sales)
    total_sales =  sum(tuna)
    print(total_sales)
    bacon = []
    for product in Product.objects.all():
        final_cost = Product.expense(product.cost_amt, product.quantity)
        bacon.append(final_cost)
    total_cost = sum(bacon)
    print(total_cost)
    if total_sales > total_cost:
        profit = Product.profit(total_sales, total_cost)
        msg = 'Profit'
        print("profit")
    elif total_sales < total_cost:
        loss = Product.loss(total_cost, total_sales)
        profit = 100 - loss
        msg = 'Loss'
        
    for capital in request.user.capital_set.all():

        remaining = Capital.remaining_capital(
            capital.amt, total_cost)
    print(remaining)
    context = {
        'profit':profit,
        'remaining':remaining,
        'total_sales':total_sales,
        'total_cost':total_cost,
        'msg':msg,
        'transaction':transaction
        
    }
    return render(request, 'shoptrans/dashboard.html', context)


class ProductApiView(generics.ListAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer


class CapitalApiView(generics.ListAPIView):
    queryset = Capital.objects.all()
    serializer_class = CapitalSerializer

class CategoryApiView(generics.ListAPIView):
    queryset = Categories.objects.all()
    serializer_class = CategorySerializer

class ProductDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer