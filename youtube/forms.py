from django.forms.widgets import Textarea
from youtube.models import Video
from django import forms
from .models import Video

class loginView(forms.Form):
    username = forms.CharField(label="username",max_length=30,widget=forms.TextInput(attrs={'class' : 'formclass'}))
    password = forms.CharField(label="password",max_length=30,widget=forms.TextInput(attrs={'class' : 'formclass'}))

class registerView(forms.Form):
    username = forms.CharField(label="username" ,max_length=30,widget=forms.TextInput(attrs={'class' : 'formclass'}))
    password = forms.CharField(label="password" ,max_length=30,widget=forms.TextInput(attrs={'class' : 'formclass'}))
    email= forms.EmailField(max_length=254,widget=forms.TextInput(attrs={'class' : 'formclass'}))

class NewVideo(forms.ModelForm):
    class Meta:
        model=Video
        
        fields=('title','desc','videofile',)
        
        # widget=forms.TextInput(attrs={'class' : 'formclass'})
        widgets = {
            'title': Textarea(attrs={'class' : 'formclass'}),
            'desc': Textarea(attrs={'class' : 'formclass'}),
            
        }
        

class CommentForm(forms.Form):
    text = forms.CharField(label="text" ,max_length=300,widget=forms.TextInput(attrs={'class' : 'formclass'}))