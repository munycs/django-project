from django import forms

class PostForm(forms.Form):
   image = forms.ImageField()
   text = forms.CharField(label="Title")
   description = forms.CharField(label="Description")
    