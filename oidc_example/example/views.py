from django.shortcuts import render
from django.contrib.auth.decorators import login_required


def home(request):
    return render(request, 'example/home.html')


@login_required
def logged(request):
    context = {
        'user': request.user,
        'extra_data': request.user.social_auth.get(provider="epita").extra_data,
    }
    return render(request, 'example/logged.html', context=context)
