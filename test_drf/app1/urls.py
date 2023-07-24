from django.urls import path
from .views import RegistrationView, LoginAPI

urlpatterns = [
    # path('register/',RegisterAPI.as_view(),name='register'),
    path('register/',RegistrationView.as_view(),name='register'),
    path('login/',LoginAPI.as_view(),name='login'),

]