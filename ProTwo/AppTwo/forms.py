from django import forms
from AppTwo.models import User

class Newform(forms.ModelForm):
    '''Firstname=forms.CharField()
    Lastname=forms.CharField()
    Email=forms.EmailField()'''
    class Meta():
        model=User
        fields= "__all__"


