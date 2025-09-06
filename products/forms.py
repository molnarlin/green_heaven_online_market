from django import forms
from .widgets import CustomClearableFileInput
from .models import Product, Category


class ProductForm(forms.ModelForm):

    light = forms.CharField(
        max_length=100,
        required=False,
        widget=forms.TextInput(
            attrs={
                'class': 'form-control border-black rounded-0',
                'placeholder': 'Light requirements'
            }
        )
    )
    water = forms.CharField(
        max_length=300,
        required=False,
        widget=forms.Textarea(
            attrs={
                'class': 'form-control border-black rounded-0',
                'rows': 3,
                'placeholder': 'Watering instructions'
            }
        )
    )
    temperature = forms.CharField(
        max_length=100,
        required=False,
        widget=forms.TextInput(
            attrs={
                'class': 'form-control border-black rounded-0',
                'placeholder': 'Ideal temperature'
            }
        )
    )
    humidity = forms.CharField(
        max_length=100,
        required=False,
        widget=forms.TextInput(
            attrs={
                'class': 'form-control border-black rounded-0',
                'placeholder': 'Humidity level'
            }
        )
    )
    has_color = forms.BooleanField(
        required=False,
        widget=forms.CheckboxInput(
            attrs={
                'class': 'form-check-input'
            }
        )
    )
    rating = forms.DecimalField(
        max_digits=6,
        decimal_places=2,
        required=False,
        widget=forms.NumberInput(
            attrs={
                'class': 'form-control border-black rounded-0',
                'placeholder': 'Rating (1-5)'
            }
        )
    )
    fertilizer = forms.CharField(
        max_length=300,
        required=False,
        widget=forms.Textarea(
            attrs={
                'class': 'form-control border-black rounded-0',
                'placeholder': 'Fertilizer requirements'
            }
        )
    )
    pests = forms.CharField(
        max_length=300,
        required=False,
        widget=forms.Textarea(
            attrs={
                'class': 'form-control border-black rounded-0',
                'placeholder': 'Pest control instructions'
            }
        )
    )
    pruning = forms.CharField(
        max_length=300,
        required=False,
        widget=forms.Textarea(
            attrs={
                'class': 'form-control border-black rounded-0',
                'placeholder': 'Pruning instructions'
            }
        )
    )
    repotting = forms.CharField(
        max_length=300,
        required=False,
        widget=forms.Textarea(
            attrs={
                'class': 'form-control border-black rounded-0',
                'placeholder': 'Repotting instructions'
            }
        )
    )
    delivery = forms.CharField(
        max_length=300,
        required=False,
        widget=forms.Textarea(
            attrs={
                'class': 'form-control border-black rounded-0',
                'placeholder': 'Delivery information'
            }
        )
    )
    planting = forms.CharField(
        max_length=300,
        required=False,
        widget=forms.Textarea(
            attrs={
                'class': 'form-control border-black rounded-0',
                'placeholder': 'Planting instructions'
            }
        )
    )
    harvesting = forms.CharField(
        max_length=300,
        required=False,
        widget=forms.Textarea(
            attrs={
                'class': 'form-control border-black rounded-0',
                'placeholder': 'Harvesting instructions'
            }
        )
    )
    size = forms.CharField(
        max_length=300,
        required=False,
        widget=forms.Textarea(
            attrs={
                'class': 'form-control border-black rounded-0',
                'placeholder': 'Size information'
            }
        )
    )
    image = forms.ImageField(
            label='Image',
            required=False,
            widget=CustomClearableFileInput
        )

    class Meta:
        model = Product
        fields = ['name', 'sku', 'price', 'image', 'description', 'category',
                  'light', 'water', 'temperature', 'humidity', 'has_color',
                  'rating', 'fertilizer', 'pests', 'pruning', 'repotting',
                  'delivery', 'planting', 'harvesting', 'size']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        care_info = self.instance.care_info or {}
        for field in ['light', 'water', 'temperature', 'humidity']:
            self.fields[field].initial = care_info.get(field, '')

        self.fields.pop('image_url', None)

        categories = Category.objects.all()
        friendly_names = [(c.id, c.get_friendly_name()) for c in categories]
        self.fields['category'].choices = friendly_names

        for field_name, field in self.fields.items():
            existing_classes = field.widget.attrs.get('class', '')
            field.widget.attrs['class'] = (
                f"{existing_classes} border-black rounded-0"
            )

    def save(self, commit=True):
        instance = super().save(commit=False)
        instance.care_info = {
            'light': self.cleaned_data.get('light', ''),
            'water': self.cleaned_data.get('water', ''),
            'temperature': self.cleaned_data.get('temperature', ''),
            'humidity': self.cleaned_data.get('humidity', ''),
        }
        if commit:
            instance.save()
        return instance
