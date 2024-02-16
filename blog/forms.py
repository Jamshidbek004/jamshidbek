from django import forms
from .models import Contact, Email, Comment


class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields ='__all__'
class emailForm(forms.ModelForm):
    class Meta:
        model = Email
        fields ='__all__'


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields =['user', 'body']