from django import forms
from .models import patient

class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = patient
        fields = [
            'patient_name',
            'dp',
            'father_name',
            'mother_name',
            'phone',
            'age'
        ]

