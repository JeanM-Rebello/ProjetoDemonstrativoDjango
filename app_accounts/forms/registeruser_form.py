from django import forms
from django.contrib.auth.forms import UserCreationForm
from app_accounts.models import CustomUser

class UserRegisterForm(UserCreationForm):
    email = forms.EmailField(required=True)
    
    username = forms.TimeField(
        widget=forms.TextInput(attrs={
            'class': 'form-control'
        }),
    )
    
    birth_date = forms.DateField(
        widget=forms.DateInput(attrs={
            'type': 'date',
            'placeholder': 'Selecione sua data de nascimento'
        }),
        required=True
    )

    class Meta:
        model = CustomUser
        fields = ['username', 'email', 'birth_date' ,'password1', 'password2']

    def clean(self):
        cleaned_data = super().clean()
        password1 = cleaned_data.get('password1')
        password2 = cleaned_data.get('password2')

        if password1 != password2:
            raise forms.ValidationError("As senhas não coincidem.")
        return cleaned_data
    
    def clean_email(self):
        email = self.cleaned_data.get('email')
        if CustomUser.objects.filter(email=email).exists():
            raise forms.ValidationError("Este e-mail já está em uso. Por favor, use outro.")
        return email
    
    def clean_birth_date(self):
        pass