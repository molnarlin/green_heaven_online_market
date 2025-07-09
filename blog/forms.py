from .models import Comment
from django import forms
from .widgets import CustomClearableFileInput
from .models import Post


class ArticleForm(forms.ModelForm):

    class Meta:
        model = Post
        exclude = ['image_url']
        fields = '__all__'

    image = forms.ImageField(
        label='Image',
        required=False,
        widget=CustomClearableFileInput
    )

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields.pop('image_url', None)

        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'border-black rounded-0'


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('body',)
        labels = {
            'body': ''  # Set to an empty string to remove "Body:"
        }
