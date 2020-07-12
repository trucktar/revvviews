from django.contrib.auth.views import LogoutView
from django.shortcuts import redirect, render, reverse
from django.views import View

from revvviews.apps.main.models import Profile, Project, Review


def logout_then_stay(request):
    """Log out an authenticated user then redirect to the same page."""
    current_page = request.META.get('HTTP_REFERER')
    return LogoutView.as_view(next_page=current_page)(request)


def redirect_to_projects(request):
    return redirect(reverse('projects'))


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
