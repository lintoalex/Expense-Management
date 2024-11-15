from django import forms

from expensemanagement.models import UserManagement,ExpenseManagement

from django.contrib.auth.forms import UserCreationForm

class RegisterForm(forms.Form):

    username=forms.CharField(widget=forms.TextInput(attrs={"class":"form-control mb-3"}))

    password=forms.CharField(widget=forms.PasswordInput(attrs={"class":"form-control mb-3"}))

class SigninForm(UserCreationForm):

    password1=forms.CharField(widget=forms.PasswordInput(attrs={"class":"form-control mb-3"}))

    password2=forms.CharField(widget=forms.PasswordInput(attrs={"class":"form-control mb-3"}))

    class Meta:

        model=UserManagement

        fields=["username","email","password1","password2","phone"]

        widgets={
            "username":forms.TextInput(attrs={"class":"form-control mb-3"}),
            "email":forms.EmailInput(attrs={"class":"form-control mb-3"}),
            "phone":forms.NumberInput(attrs={"class":"form-control mb-3"}),
        }

class ExpenseAddForm(forms.ModelForm):

    class Meta:

        model=ExpenseManagement

        fields="__all__"

        widgets={
            "title":forms.TextInput(attrs={"class":"form-control mb-3"}),
            "category_option":forms.Select(attrs={"class":"form-control form-select mb-3"}),
            "amount":forms.NumberInput(attrs={"class":"form-control mb-3"}),
            "payment_option":forms.Select(attrs={"class":"form-control mb-3"})
        }