from django import forms
from .models import Application, Status


class StatusForm(forms.ModelForm):
    class Meta:
        model = Status
        fields = ['Applied', 'Interviewing', 'Previous Application']