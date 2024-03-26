from django.shortcuts import render
from .models import Portfolio, Achievement


# Create your views here.
def get_all_portfolios(request):
    portfolios = Portfolio.objects.all().order_by("id")
    achievements = Achievement.objects.all().order_by("id")

    return render(request, "portfolio/main_page.html", {
        "portfolios": portfolios,
        "achievements": achievements,
    })


def get_rating(request):
    portfolios = Portfolio.objects.all()
    achievements = Achievement.objects.all()

    portfolio_rating = 0
    current_portfolio = None
    normalization_coefficient = 10
    for a in achievements:
        if current_portfolio is None:
            portfolio_rating += a.level*normalization_coefficient
            current_portfolio = a.portfolio
            continue
        if current_portfolio == a.portfolio:
            portfolio_rating += a.level*normalization_coefficient
        else:
            portfolio_rating = a.level*normalization_coefficient
        a.portfolio.rating = portfolio_rating
        a.portfolio.save()
        current_portfolio = a.portfolio

    return render(request, "portfolio/rating_page.html", {
        "portfolios": portfolios.order_by("-rating"),
    })
