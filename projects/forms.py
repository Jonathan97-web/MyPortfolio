from .models import Comment, Project
from profiles.models import Profile
from django import forms


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('body',)


class CreateProjectForm(forms.ModelForm):

    class Meta:
        model = Project
        fields = ('title', 'content', 'image', 'deployed_url', 'source_code')
