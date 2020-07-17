from django.forms import Form, ModelForm, NumberInput

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
        widgets = {
            field: NumberInput(attrs={
                'min': 0,
                'max': 10,
                'type': 'range',
                'value': 0
            })
            for field in fields
        }
