from django.contrib.auth.forms import UserCreationForm
from sellers.models import SellerProfile


class UserProfileForm(UserCreationForm):
    class Meta:
        model = SellerProfile
        fields = ('username', 'first_name', 'last_name', 'password1', 'password2')
