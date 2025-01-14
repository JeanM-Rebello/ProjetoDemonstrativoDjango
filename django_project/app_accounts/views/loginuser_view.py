from django.contrib.auth.views import LoginView
from app_accounts.forms import UserLoginForm

class UserLoginView(LoginView):
    template_name = 'accounts/login.html'
    authentication_form = UserLoginForm
