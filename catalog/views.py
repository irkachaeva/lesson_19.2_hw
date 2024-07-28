from django.shortcuts import render, get_object_or_404
from catalog.models import Product


def product_list(request):
    products = Product.objects.all()
    context = {"products": products}
    return render(request, 'product_detail.html', context)


def contacts(request):
    return render(request, 'contacts.html')




def product_detail(request, pk):
    context = {'object': get_object_or_404(Product, pk=pk)}
    return render(request, 'product_detail.html', context)


