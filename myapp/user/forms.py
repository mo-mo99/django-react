from pyexpat import model
from attr import fields
from django import forms
from .models import Content


class Content_form(forms.ModelForm):
    class Meta:
        model = Content
        fields = ("caption", "video")