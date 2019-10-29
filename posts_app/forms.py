from django import forms
from posts_app.models import postsModel,replyModel

class PostsForm(forms.ModelForm):
    log = forms.CharField(widget=forms.Textarea(attrs={'rows':'5','cols':'100'}))
    class Meta():
        model = postsModel
        fields =['datetime','name','id','log']

class ReplyForm(forms.ModelForm):
    reply = forms.CharField(widget=forms.Textarea(attrs={'rows':'5','cols':'100'}))
    class Meta():
        model = replyModel
        fields = ['name','replyTo', 'datetime','reply']
