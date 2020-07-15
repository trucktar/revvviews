from django.forms import Form, ModelForm

from revvviews.apps.main.models import Project, Review


class ProjectSubmitForm(ModelForm):
    class Meta:
        model = Project
        fields = ['screenshot', 'title', 'description', 'live_link']
        field_order = fields


class ProjectReviewForm(ModelForm):
    class Meta:
        model = Review
        fields = ['design', 'usability', 'content']
