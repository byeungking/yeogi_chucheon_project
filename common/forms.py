from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm


class CustomLoginForm(AuthenticationForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['username'].widget.attrs.update({'class': 'form-control mb-2', 'placeholder': '사용자 이름'})
        self.fields['password'].widget.attrs.update({'class': 'form-control mb-2', 'placeholder': '비밀번호'})

class CustomSignUpForm(UserCreationForm):
    email = forms.EmailField(label="이메일", required=True)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['username'].widget.attrs.update({'class': 'form-control mb-2', 'placeholder': '사용자 이름'})
        self.fields['email'].widget.attrs.update({'class': 'form-control mb-2', 'placeholder': '이메일'})
        self.fields['password1'].widget.attrs.update({'class': 'form-control mb-2', 'placeholder': '비밀번호'})
        self.fields['password2'].widget.attrs.update({'class': 'form-control mb-2', 'placeholder': '비밀번호 확인'})

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']