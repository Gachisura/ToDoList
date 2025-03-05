from django.urls import path
from .views import UserReg, UserLogin

urlpatterns = [
    path('api/users/register', UserReg.as_view(), name='user-reg'),
    path('api/users/login', UserLogin.as_view(), name='user-login'),
]