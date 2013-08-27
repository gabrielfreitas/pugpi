from django import forms
from ckeditor.widgets import CKEditorWidget
from apps.core.models import Event


class EventForm(forms.ModelForm):
    class Meta:
        model = Event
        widgets = {'full_description': CKEditorWidget()}