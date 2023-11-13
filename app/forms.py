from django import forms
from django.forms import ModelForm
from accounts.models import TrackerUser
from app.models import Food, Exercise, FoodIntsance, Time
from django.shortcuts import render
from .models import Exercise, Time
from datetime import timedelta  # Correct the import
from .models import Exercise, timezone
class ExerciseForm(forms.Form):
    exercise = forms.ModelChoiceField(queryset=Exercise.objects.all())  
    times = forms.ModelChoiceField(queryset=Time.objects.all())
    date = forms.DateField()
    duration = forms.CharField(max_length=8, help_text='Enter duration in HH:MM:SS format')

    def clean_duration(self):
        duration = self.cleaned_data['duration']
        try:
            hours, minutes, seconds = map(int, duration.split(':'))
            return timezone.timedelta(hours=hours, minutes=minutes, seconds=seconds)
        except ValueError:
            raise forms.ValidationError('Invalid duration format. Use HH:MM:SS.')

class FoodForm(forms.Form):

        food = forms.ModelChoiceField(queryset=Food.objects.all())
        times = forms.ModelChoiceField(queryset=Time.objects.all())
        date = forms.DateField()

