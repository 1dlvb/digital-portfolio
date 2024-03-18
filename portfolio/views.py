from django.shortcuts import render
from .models import Portfolio


# Create your views here.
def get_all_portfolios(request):
    portfolios = Portfolio.objects.all().order_by("id")
    return render(request, "portfolio/main_page.html", {
        "portfolios": portfolios,
    })
