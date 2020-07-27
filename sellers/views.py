from django.shortcuts import render
from django.views import generic
from sellers import models, forms
from django.urls import reverse_lazy
from products import models


def index(request):
    return render(request, 'index.html')


def thanks(request):
    return render(request, 'thanks.html')


class ThanksView(generic.TemplateView):
    template_name = 'success.html'


class UserCreateView(generic.CreateView):
    model = models.SellerProfile
    form_class = forms.UserProfileForm
    template_name = 'seller_register.html'
    success_url = reverse_lazy('index')

class ProductListView(generic.ListView):
    model = models.Product
    context_object_name = 'products'
    template_name = 'seller_profile.html'

class UserProfileView(generic.DetailView):
    model = models.SellerProfile
    context_object_name = 'seller'
    template_name = 'seller_profile.html'
