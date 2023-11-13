from django.contrib.auth.forms import UserCreationForm
from .models import TrackerUser
from .models import Friend_Request
from django import forms

class TrackerUserCreationForm(UserCreationForm):

    class Meta(UserCreationForm.Meta):
        model = TrackerUser
        fields = UserCreationForm.Meta.fields + ('email', 'height', 'weight', 'age', 'gender')

class FriendRequestForm(forms.ModelForm):
     class Meta:
        model = Friend_Request
        fields = []  # No need for fields, as the form will be created programmatically