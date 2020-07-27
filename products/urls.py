from django.urls import path
from products import views

app_name = 'products'

urlpatterns = [
    path('add/', views.ProductCreateView.as_view(), name='add'),
    # path('all/', views.ProductListView.as_view(), name='all'),
    path('all/<int:pk>/', views.ProductDetailView.as_view(), name='detail'),
    path('edit/<int:pk>/', views.ProductUpdateView.as_view(), name='edit'),
    path('remove/<int:pk>/', views.ProductDeleteView.as_view(), name='remove'),
]
