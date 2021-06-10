from youtube.models import Video
from django import forms
from .models import Video

class loginView(forms.Form):
    username = forms.CharField(label="username",max_length=30)
    password = forms.CharField(label="password",max_length=30)

class registerView(forms.Form):
    username = forms.CharField(label="username" ,max_length=30)
    password = forms.CharField(label="password" ,max_length=30)
    email= forms.EmailField(max_length=254)

class NewVideo(forms.ModelForm):
    class Meta:
        model=Video
        fields=('title','desc','videofile',)

class CommentForm(forms.Form):
    text = forms.CharField(label="text" ,max_length=300)