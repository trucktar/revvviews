from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth.views import LoginView
from django.urls import path
from django_registration.backends.one_step.views import RegistrationView

from revvviews.apps.main import views

urlpatterns = [
    path('register/',
         RegistrationView.as_view(
             template_name='register.html',
             success_url='/',
         ),
         name='register'),
    path('login/', LoginView.as_view(template_name='login.html'),
         name='login'),
    path('logout/', views.logout_then_stay, name='logout'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
