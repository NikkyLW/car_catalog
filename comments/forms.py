from django import forms

from comments.models import Comment

class CommentCreate(forms.ModelForm):

    class Meta:
        model = Comment
        fields = ['content']

    content = forms.CharField()