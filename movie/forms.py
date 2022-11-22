# models/forms.py

# from django.forms import ModelForm, Form, Textarea
from django import forms
from .models import Movie, Review

class ReviewForm(forms.ModelForm):
   def __init__(self, *args, **kwargs):
      super(forms.ModelForm, self).__init__(*args, **kwargs)
      self.fields['text'].widget.attrs.update( {'class': 'form-control'})
      self.fields['watchAgain'].widget.attrs.update({'class': 'form-check-input'})
 
   class Meta:
      model = Review
      fields = ['text','watchAgain']
      labels = {
         'watchAgain': ('Watch Again')
      }
      widgets = {
         'text': forms.Textarea(attrs={'rows': 4}),
      }
 
class MovieForm(forms.Form):
   title = forms.CharField()
   description = forms.CharField()
   url = forms.URLField()
   class Meta:
      model = Movie 
      fields = [ 'title', 'description', 'url']
      labels = {
         'title': ('Movie title'),
         'description': ('The description'),
         'url': ('External movie URL'),
      }

# class ContactForm(Form):
#     name = forms.CharField()
#     message = forms.CharField(widget=forms.Textarea)

#     def send_email(self):
#         # send email using the self.cleaned_data dictionary
#         pass
