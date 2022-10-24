from django.forms import ModelForm
from .models import Review


class CommentForm(ModelForm):
    """Класс коментариев"""

    class Meta:
        model = Review
        fields = ('review',)
