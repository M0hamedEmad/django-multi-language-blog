from django.urls import path
from .views import LoginPage

app_name = 'account'

urlpatterns = [
    path('login/', LoginPage.as_view(), name='login')
]