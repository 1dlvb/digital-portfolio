from django.shortcuts import render, redirect

from .models import Portfolio
from .forms import RegistrationForm


# Create your views here.
def get_all_portfolios(request):
    portfolios = Portfolio.objects.all().order_by("id")
    return render(request, "portfolio/main_page.html", {
        "portfolios": portfolios,
    })


def registration_new_user(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            user = form.save(commit='False')
            user.save()
            return redirect('post_detail', pk=user.pk)
    else:
        form = RegistrationForm()
    return render(request, 'portfolio/registration.html', {'form': form})