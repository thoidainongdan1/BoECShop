from django import forms
from django.contrib.auth.forms import UserCreationForm
from accounts.models import User
from .models import Profile

GENDER_CHOICES = (('M', 'Nam'), ('F', 'Nữ'))

class SignUpForm(UserCreationForm):

    birth_date = forms.DateField(help_text='Định dạng: YYYY-MM-DD', label=("Ngày sinh"))
    phone_number = forms.CharField(required=True, max_length=30, label=("Số điện thoại"))
    full_name = forms.CharField(required=True, label=("Họ tên"))
    gender = forms.ChoiceField(choices=GENDER_CHOICES, widget=forms.RadioSelect(), label=("Giới tính"))
    password1 = forms.CharField(widget=forms.PasswordInput, label=("Mật khẩu"))
    password2 = forms.CharField(widget=forms.PasswordInput, label=("Nhập lại mật khẩu"))
    email = forms.EmailField(widget=forms.EmailInput, label=("E-mail"))
    address = forms.CharField(required=False, label=("Địa chỉ"))

    class Meta:
        model = User
        fields = ('full_name', 'email', 'gender' , 'birth_date', 'phone_number', 'address', 'password1', 'password2',)