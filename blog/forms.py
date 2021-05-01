from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Post

LOCATION_CHOICES = [
    ('Mumbai', 'Mumbai'),
    ('Chennai', 'Chennai'),
    ('Kolkata', 'Kolkata'),
    ('New Delhi', 'New Delhi')
]
GENDER_CHOICES = [
    ('Male', 'Male'),
    ('Female', 'Female'),
]
GENRE_CHOICES = [
    ('Education', 'Education'),
    ('Tech', 'Tech'),
    ('Politics', 'Politics'),
]

class PostForm(forms.ModelForm):
    gender = forms.ChoiceField(widget=forms.RadioSelect,choices=GENDER_CHOICES)
    genre = forms.MultipleChoiceField(widget=forms.CheckboxSelectMultiple,choices=GENRE_CHOICES)
    class Meta:   
        model = Post   
        fields = ['title', 'content', 'city', 'gender', 'genre']
        
