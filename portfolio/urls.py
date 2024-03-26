from django.urls import path
from . import views

urlpatterns = [
    path('', views.get_all_portfolios, name='get_all_portfolios'),
    path("rating", views.get_rating, name='get_rating'),
    path('registration', views.registration),
    path("register-done", views.registration),

]
