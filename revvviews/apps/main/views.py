from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import LoginView as BaseLoginView
from django.contrib.auth.views import LogoutView
from django.http import JsonResponse
from django.shortcuts import redirect, render, resolve_url, reverse
from django.views.generic.base import TemplateView, View
from django_registration.backends.one_step.views import \
    RegistrationView as BaseRegistrationView

from revvviews.apps.main.forms import ProjectReviewForm, ProjectSubmitForm
from revvviews.apps.main.models import Profile, Project, Review


def logout_then_stay(request):
    """Log out an authenticated user then redirect to the same page."""
    if not request.user.is_authenticated:
        return redirect(reverse('home'))

    current_page = resolve_url(request.META.get('HTTP_REFERER'))
    return LogoutView.as_view(next_page=current_page)(request)


def redirect_to_projects(request):
    return redirect(reverse('projects'))


class AJAXOnlyResponseMixin:
    def form_invalid(self, form):
        super().form_invalid(form)
        form_errors = {
            'non_field_errors': form.non_field_errors(),
            **{
                field.name: [error for error in field.errors]
                for field in form.visible_fields()
            }
        }
        return JsonResponse(form_errors, status=400)


class RegistrationView(AJAXOnlyResponseMixin, BaseRegistrationView):
    def get_success_url(self, user=None):
        current_user = self.request.user
        return reverse('profile', args=[current_user.username])


class LoginView(AJAXOnlyResponseMixin, BaseLoginView):
    def get_success_url(self):
        current_page = self.request.META.get('HTTP_REFERER')
        return resolve_url(current_page)


class ProfileView(View):
    def get(self, request, *args, **kwargs):
        username = kwargs.get('username')
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


class ProjectSubmitView(LoginRequiredMixin, View):
    def get(self, request, *args, **kwargs):
        return render(
            request,
            'submit.html',
            context={
                'submit_form': ProjectSubmitForm(),
            },
        )

    def post(self, request, *args, **kwargs):
        project = Project(profile=request.user.profile)
        submit_form = ProjectSubmitForm(
            request.POST,
            request.FILES,
            instance=project,
        )
        submit_form.save()
        return redirect(reverse('submit'))
