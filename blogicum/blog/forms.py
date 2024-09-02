from django.forms.widgets import DateTimeInput
from django.forms import ModelForm
from django.utils import timezone

from .models import Post, Comment


class PostForm(ModelForm):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['pub_date'].initial = timezone.localtime(
            timezone.now()
        ).strftime('%Y-%m-%dT%H:%M')

    class Meta:
        model = Post
        fields = {
            'title',
            'text',
            'image',
            'location',
            'category',
            'pub_date',
        }
        widgets = {
            'pub_date': DateTimeInput(
                format='%Y-%m-%dT%H:%M', attrs={'type': 'datetime-local'},
            )
        }


class CommentForm(ModelForm):

    class Meta:
        model = Comment
        fields = ('text', )
