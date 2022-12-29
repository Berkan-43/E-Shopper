from django import forms
from product.models import *

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('subject', 'comment', 'rate')