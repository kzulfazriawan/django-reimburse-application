from django import forms
from .models import Reimburse


class ReimburseUploadForm(forms.ModelForm):
    class Meta:
        model = Reimburse
        fields = ('date', 'document_attach', 'description')
