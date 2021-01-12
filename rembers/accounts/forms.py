from django import forms
from .models import UserProfileInfo


class PatchUserProfileForm(forms.ModelForm):

    class Meta:
        model = UserProfileInfo
        fields = ('name', 'phone_number', 'profile_picture', 'description', 'bank_name', 'bank_account')
