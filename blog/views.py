from django.core.paginator import Paginator
from django.shortcuts import render, redirect
from .models import Customer 
from  django.db.models import Q
from .forms import CustomerModelForm, ProductListModelForm

from blog.models import Product


# Create your views here.


def index(request):
    products = Product.objects.all()
    paginator = Paginator(products, 2)
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)
    context = {
        'page_obj': page_obj,
    }
    return render(request, 'blog/index.html', context)


def product_detail(request, pk):
    product = Product.objects.get(id=pk)
    context = {
        'product': product,
    }
    return render(request, 'blog/product-detail.html', context)

def customer_list(request):
    customers = Customer.objects.all()
    search_query = request.GET.get('search')
    paginator = Paginator(customers, 5)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    if search_query:
        page_obj = customers.filter(Q(full_name__icontains=search_query) | Q(email__icontains=search_query))
        
    context = {
          'page_obj': page_obj,
    }
    return render(request, 'blog/customers.html', context)

def customer_details(request, pk):
    customer = Customer.objects.get(id=pk)
    context = {
        'customer': customer
    }
    return render(request, 'blog\customers_details.html')    


def add_customer(request):
    customers = Customer.objects.all()
    form = CustomerModelForm()
    if request.method == 'POST':
        form = CustomerModelForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('customers')

    context = {
        'customers': customers,
        'form': form
    }
    return render(request, 'blog/add-customer.html', context)