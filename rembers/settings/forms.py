from django import forms
from .models import Settings


class PostSaveSettings(forms.ModelForm):

    class Meta:
        model = Settings
        fields = ('value',)
