from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.views.generic import ListView, UpdateView, DetailView, CreateView, DeleteView

from .forms import ProductForm
from .models import Product
from django.urls import reverse_lazy


# Create your views here.

class IndexView(ListView):
    model = Product
    template_name = 'djangoapp/index.html'
    ordering = ['-id']


class MonitorView(ListView):
    model = Product
    template_name = 'djangoapp/products_monitor.html'
    ordering = ['-id']


class ProductUpdateView(UpdateView):
    model = Product
    form_class = ProductForm
    template_name = 'djangoapp/product_edit.html'


class ProductDetailView(DetailView):
    model = Product
    template_name = 'djangoapp/detail.html'


class ProductAddView(CreateView):
    model = Product
    form_class = ProductForm
    template_name = 'djangoapp/product_edit.html'
    success_url = reverse_lazy('monitor')


class ProductDeleteView(DeleteView):
    model = Product
    template_name = 'djangoapp/confirm_delete.html'
    success_url = reverse_lazy('monitor')

'''
# called by "update" button pressing
def ProductUpdateView(request, product_id):
    # dictionary for initial data with
    # field names as keys
    context = {}

    # fetch the object related to passed id
    product = get_object_or_404(Product, id=product_id)

    # pass the object as instance in form
    form = ProductForm(request.POST or None, instance=product)

    # save the data from the form and
    # redirect to detail_view
    if form.is_valid():
        form.save()
        return HttpResponseRedirect("/" + product_id)

    # add form dictionary to context
    context["form"] = form
    return render(request, 'djangoapp/detail.html', {'product': product})
'''


