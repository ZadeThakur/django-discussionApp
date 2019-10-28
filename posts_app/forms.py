from django import forms
from posts_app.models import postsModel


class PostsForm(forms.ModelForm):
    log = forms.CharField(widget=forms.Textarea(attrs={'rows':'5','cols':'100'}))
    class Meta():
        model = postsModel
        fields = '__all__'