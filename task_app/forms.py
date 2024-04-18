from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Collect, Payment

class NewUserForm(UserCreationForm):
    email = forms.EmailField(required=True)
    FIO = forms.CharField(max_length=100, required=True, label='Your surname and name')

    class Meta:
        model = User
        fields = ('FIO','username', 'email', 'password1', 'password2')

    def save(self, commit=True):
        user = super(NewUserForm, self).save(commit=False)
        user.email = self.cleaned_data['email']
        user.FIO = self.cleaned_data['FIO']
        if commit:
            user.save()
        return user

class AddGroupDonationForm(forms.ModelForm):
    class Meta:
        model = Collect
        fields = ('FIO','name', 'occasion', 'description', 'current_amount', 'image', 'date_finish')

class AddAmountForm(forms.Form):
    amount = forms.IntegerField(label='Amount to add')
    FIO = forms.CharField(max_length=100, label='surname and name')

