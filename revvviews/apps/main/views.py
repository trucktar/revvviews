from django.shortcuts import render


def index(request):
    return render(
        request,
        'index.html',
        context={'message': 'Systems up and running!'},
    )
