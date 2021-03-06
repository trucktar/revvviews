from django.conf import settings
from django.conf.urls.static import static
from django.urls import path

from revvviews.apps.main import views

urlpatterns = [
    path('', views.redirect_to_projects, name='home'),
    path('projects/', views.ProjectsView.as_view(), name='projects'),
    path('projects/<title>/', views.ProjectView.as_view(), name='project'),
    path('projects/<title>/review',
         views.ProjectSubmitView.as_view(),
         name='review'),
    path('search/', views.SearchView.as_view(), name='search'),
    path('register/', views.RegistrationView.as_view(), name='register'),
    path('login/', views.LoginView.as_view(), name='login'),
    path('logout/', views.logout_then_stay, name='logout'),
    path('submit/', views.ProjectSubmitView.as_view(), name='submit'),
    path('<username>/', views.ProfileView.as_view(), name='profile'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
