from django import forms
from .models import Project

class ProjectForm(forms.ModelForm):
    class Meta:
        model = Project
        fields = ['Discipline', 'code', 'name', 'description', 'date_completed', 'link', 'background_color', 'text_color', 'icon']
        widgets = {
            'Discipline': forms.Select(attrs={'class': 'form-select'}),
            'code': forms.TextInput(attrs={'class': 'form-control'}),
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'description': forms.Textarea(attrs={'class': 'form-control', 'rows': 3}),
            'date_completed': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'link': forms.URLInput(attrs={'class': 'form-control'}),
            'background_color': forms.TextInput(attrs={'class': 'form-control', 'type': 'color'}),
            'text_color': forms.TextInput(attrs={'class': 'form-control', 'type': 'color'}),
            'icon': forms.TextInput(attrs={'class': 'form-control'}),
        }

from .models import Discipline

class DisciplineForm(forms.ModelForm):
    class Meta:
        model = Discipline
        fields = '__all__'