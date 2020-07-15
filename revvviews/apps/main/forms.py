from django.forms import Form, ModelForm

from revvviews.apps.main.models import Project, Review


class ProjectSubmitForm(ModelForm):
    model = Project
    fields = ['title', 'description', 'screenshot', 'live_link']


class ProjectReviewForm(ModelForm):
    model = Review
    fields = ['design', 'usability', 'content']
