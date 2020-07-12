from django.shortcuts import render
from django.contrib.auth.views import LogoutView



def logout_then_stay(request):
    """Log out an authenticated user then redirect to the same page."""
    current_page = request.META.get('HTTP_REFERER')
    return LogoutView.as_view(next_page=current_page)(request)

