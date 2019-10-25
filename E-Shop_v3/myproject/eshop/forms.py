from django import forms
from . models import Item
class SizeForm(forms.ModelForm):
    class Meta:
        model = Item
        fields = ('size',)