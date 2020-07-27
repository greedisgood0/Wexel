from django.urls import path, reverse_lazy
from sellers import views
from django.contrib.auth import views as auth_views

app_name = 'sellers'

urlpatterns = [
    path('register/', views.UserCreateView.as_view(), name='register'),
    path('login/', auth_views.LoginView.as_view(template_name='login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(next_page='sellers:thanks'), name='logout'),
    path('thanks/', views.thanks, name='thanks'),
    path('success/', views.ThanksView.as_view(), name='success'),
    path('profile/', views.UserProfileView.as_view(), name='profile'),

]