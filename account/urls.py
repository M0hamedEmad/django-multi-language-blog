from django.urls import path
from .views import LoginPage, RegisterView

app_name = 'account'

urlpatterns = [
    path('login/', LoginPage.as_view(), name='login'),
    path('register/', RegisterView.as_view(), name='register'),
]