from django import forms
#from .models import Authors

from usersApp.models import Authors



class NewBookForm(forms.Form):

    BookId=forms.IntegerField(label="Book ID:",widget=forms.TextInput(attrs={'class':'form-control col-lg-4 '}))
    BookName=forms.CharField(widget=forms.TextInput(attrs={'class':'form-control col-lg-4 '}))
    PageNumbers=forms.IntegerField(widget=forms.TextInput(attrs={'class':'form-control col-lg-4 '}))
    Price=forms.IntegerField(widget=forms.TextInput(attrs={'class':'form-control col-lg-4 '}))
    botcatcher=forms.CharField(required=False, widget=forms.HiddenInput(attrs={'class':'form-control col-lg-4 '}))
    #Author=forms.ModelMultipleChoiceField(queryset=Authors.objects.all())

def clean_botcatcher(self):
    botcatcher=self.cleaned_data['botcatcher']
    if len(botcatcher) > 0 :
        raise forms.ValidationError
    return botcatcher
