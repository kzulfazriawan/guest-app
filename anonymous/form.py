from django import forms as _
from .models import Guest


class FormCreate(_.ModelForm):
    class Meta:
        model = Guest
