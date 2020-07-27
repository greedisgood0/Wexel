from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import generic
from django import template
from products import models, forms

register = template.Library()

class ProductCreateView(generic.CreateView):
    model = models.Product
    form_class = forms.ProductForm
    template_name = 'product_create.html'
    extra_context = {'product_form': form_class}
    success_url = reverse_lazy('index')
    def form_valid(self, form):
         form.instance.seller = self.request.user.sellerprofile
         form.save(commit=True)
         return super(ProductCreateView, self).form_valid(form)


class ProductListView(generic.ListView):
    model = models.Product
    context_object_name = 'products'
    template_name = 'index.html'


class ProductDetailView(generic.DetailView):
    model = models.Product
    context_object_name = 'products'
    template_name = 'product_detail.html'


class ProductUpdateView(generic.UpdateView):
    model = models.Product
    form_class = forms.ProductForm
    template_name = 'product_update.html'
    success_url = reverse_lazy('Products:all')


class ProductDeleteView(generic.DeleteView):
    model = models.Product
    template_name = 'product_delete.html'
    success_url = reverse_lazy('Products:all')

def index(request):
    return render(request, 'index.html')



