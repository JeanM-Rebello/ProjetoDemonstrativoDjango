from django.urls import path
from django.contrib.auth.views import LogoutView
from app_accounts.views import(
    UserLoginView, UserRegisterView
)

app_name="accounts"

urlpatterns = [
    path('login/', UserLoginView.as_view(), name='login'),
    path('registrar/', UserRegisterView.as_view(), name='register'),
    path('logout/', LogoutView.as_view(), name='logout'),
]
