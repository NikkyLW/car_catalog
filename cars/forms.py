from django import forms

from cars.models import Car

class CarCreate(forms.ModelForm):

    class Meta:
        model = Car
        fields = ['make', 'model', 'year', 'description']

    make = forms.CharField()
    model = forms.CharField()
    year = forms.CharField()
    description = forms.CharField()