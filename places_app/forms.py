from django import forms
from .models import Place

class PlaceForm(forms.ModelForm):
    class Meta:
        model = Place
        fields = ['name', 'description', 'place_type', 'location', 'rating', 'image']
        widgets = {
            'description': forms.Textarea(attrs={'rows': 4, 'placeholder': 'Опишіть це місце...'}),
            'rating': forms.NumberInput(attrs={'min': 1, 'max': 5, 'class': 'rating-input'}),
            'name': forms.TextInput(attrs={'placeholder': 'Назва місця'}),
            'location': forms.TextInput(attrs={'placeholder': 'Адреса або локація'}),
        }
        labels = {
            'name': 'Назва місця',
            'description': 'Опис',
            'place_type': 'Тип місця',
            'location': 'Локація',
            'rating': 'Рейтинг (1-5)',
            'image': 'Зображення',
        }

    def clean_name(self):
        name = self.cleaned_data.get('name')
        if not name or not name.strip():
            raise forms.ValidationError("Назва не може бути порожньою")
        return name.strip()

    def clean_rating(self):
        rating = self.cleaned_data.get('rating')
        if rating < 1 or rating > 5:
            raise forms.ValidationError("Рейтинг від 1 до 5!!")
        return rating