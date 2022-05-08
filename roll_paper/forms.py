# forms.py
from django import forms
from .models import RollPaper

class RollPaperForm(forms.ModelForm):
    title = forms.CharField(
        label='제목',
        widget=forms.TextInput(
            attrs={
                'class': 'form-control letter-title',
            }
        )
    )
    content = forms.CharField(
        label='',
        widget=forms.Textarea(
            attrs={
                'class': 'form-control letter-content',
            }
        )
    )
    
    class Meta:
        model = RollPaper
        fields = ('title', 'content',)

