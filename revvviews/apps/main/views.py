from django.contrib.auth.views import LoginView as BaseLoginView
from django.contrib.auth.views import LogoutView
from django.shortcuts import redirect, render, resolve_url, reverse
from django.views.generic.base import TemplateView, View
from django_registration.backends.one_step.views import \
    RegistrationView as BaseRegistrationView

from revvviews.apps.main.models import Profile, Project, Review


def logout_then_stay(request):
    """Log out an authenticated user then redirect to the same page."""
    if request.user.is_authenticated:
        current_page = request.META.get('HTTP_REFERER', '/')
        return LogoutView.as_view(next_page=current_page)(request)


def redirect_to_projects(request):
    return redirect(reverse('projects'))


class RegistrationView(BaseRegistrationView):
    template_name = 'auth/register.html'

    def get_success_url(self):
        return resolve_url('home')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['registration_form'] = context.pop('form')

        return context


class LoginView(BaseLoginView):
    template_name = 'auth/login.html'

    def get_success_url(self):
        LOGIN_REDIRECT_URL = '/'
        return resolve_url(LOGIN_REDIRECT_URL)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['login_form'] = context.pop('form')

        return context


class ProfileView(View):
    def get(self, request, *args, **kwargs):
        username = kwargs.get('username')

        if username == 'favicon.ico':
            return redirect_to_projects(request)

        return render(
            request,
            'profile.html',
            context={
                'profile': Profile.get_by_username(username),
            },
        )


class ProjectsView(View):
    def get(self, request, *args, **kwargs):
        return render(
            request,
            'projects.html',
            context={
                'projects': Project.objects.all(),
            },
        )


class SearchView(View):
    def get(self, request, *args, **kwargs):
        search_term = request.GET.get('project')
        return render(
            request,
            'projects.html',
            context={
                'search_term': search_term,
                'projects': Project.search_project(search_term),
            },
        )


class ProjectView(View):
    def get(self, request, *args, **kwargs):
        project_title = kwargs.get('title')
        return render(
            request,
            'project.html',
            context={
                'project': Project.objects.get(title=project_title),
            },
        )
