from django import forms
from jazzmin.templatetags.jazzmin import User

from customers.models import Customer
class CustomerForm(forms.ModelForm):
    class Meta:
        model = Customer
        fields = '__all__'

class LoginForm(forms.Form):
    email = forms.EmailField(required=True)
    password = forms.CharField(required=True)
    #
    # def clean_username(self):
    #     username = self.data.get('username')
    #     if not User.objects.filter(username=username).exists():
    #         raise forms.ValidationError(f'That user {username} not found')
    #     return username


class RegisterForm(forms.ModelForm):
    confirm_password = forms.CharField(max_length=255)
    username = forms.CharField(max_length=100, required=False)


    class Meta:
        model = User
        fields = ('username', 'email', 'password')

    def clean_username(self):
        email = self.data.get('email')
        if User.objects.filter(username=email).exists():
            raise forms.ValidationError(f'This {email} is already exists')
        return email

    def clean_password(self):
        password = self.data.get('password')
        confirm_password = self.data.get('confirm_password')
        if password != confirm_password:
            raise forms.ValidationError('Passwords do not match')
        return self.cleaned_data['password']

    def save(self, commit=True):
        user = super(RegisterForm, self).save(commit=False)
        user.set_password(self.cleaned_data['password'])
        user.is_active = True
        user.is_superuser = True
        user.is_staff = True

        if commit:
            user.save()

        return user
