from django.urls import path
from . import views

urlpatterns = [
    path('', views.get_all_portfolios, name='get_all_portfolios'),
    path('registration/', views.registration_new_user)
]