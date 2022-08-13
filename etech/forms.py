from django import forms
from django.core.validators import FileExtensionValidator

from .models import Image, Portfolio


class PortfolioForm(forms.ModelForm):
    class Meta:
        model = Portfolio
        fields = (
            'title',
            'category',
            'client',
            'project_date',
            'project_url',
            'text',
            'published',
        )
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Layihənin adı.'}),
            'category': forms.Select(attrs={'class': 'form-control', 'placeholder': 'Kateqoriya.'}),
            'client': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Müştəri.'}),
            'project_date': forms.DateInput(attrs={'class': 'form-control', 'placeholder': 'Təhvil tarixi. (GÜN.AY.İL)'}),
            'project_url': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Layihə url.'}),
            'text': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Layihə haqqında məlumat.'}),
        }


class ImageForm(forms.ModelForm):
    image = forms.ImageField(
        label="Image",
        widget=forms.ClearableFileInput(attrs={"multiple": True, 'placeholder': 'Şəkil'}),
    )

    class Meta:
        model = Image
        fields = ("image",)
