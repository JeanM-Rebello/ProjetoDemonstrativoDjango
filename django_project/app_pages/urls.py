from django.urls import path
from django.contrib.auth.views import LogoutView
from app_pages.views import(
    HomePageView
)

app_name="pages"

urlpatterns = [
    path('', HomePageView.as_view(), name='home'),
]
