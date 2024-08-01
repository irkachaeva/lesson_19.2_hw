from django.shortcuts import render, get_object_or_404
from catalog.models import Product
from django.views.generic import ListView, DetailView, TemplateView


class ProductListView(ListView):
    model = Product # Модель


class ProductDetailView(DetailView):
    model = Product # Модель


class ContactsView(TemplateView):
    template_name = 'contacts.html'



# def contacts(request):
#     return render(request, 'contacts.html')


# def product_list(request):
#     products = Product.objects.all()
#     context = {"products": products}
#     return render(request, 'product_list.html', context)


# def product_detail(request, pk):
#     product = get_object_or_404(Product, pk=pk)
#     context = {'product': product}
#     return render(request, 'product_detail.html', context)


