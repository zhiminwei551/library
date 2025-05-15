# library/forms.py
from django import forms
from .models import Student, Administrator, Book

class LoginForm(forms.Form):
    ACCOUNT_TYPE_CHOICES = [
        ('student', '学生账户'),
        ('admin', '管理员账户'),
    ]
    account_type = forms.ChoiceField(
        choices=ACCOUNT_TYPE_CHOICES,
        widget=forms.RadioSelect,
        label="账户类型"
    )
    account = forms.CharField(
        max_length=20,
        label="账户号",
        widget=forms.TextInput(attrs={'maxlength': 20, 'class': 'form-control'})
    )
    password = forms.CharField(
        max_length=20,
        label="密码",
        widget=forms.PasswordInput(attrs={'maxlength': 20, 'class': 'form-control'})
    )

class RegisterForm(forms.Form):
    account = forms.CharField(
        max_length=20,
        label="账户号",
        widget=forms.TextInput(attrs={'maxlength': 20, 'class': 'form-control'})
    )
    password = forms.CharField(
        max_length=20,
        label="密码",
        widget=forms.PasswordInput(attrs={'maxlength': 20, 'class': 'form-control'})
    )
    name = forms.CharField(
        max_length=20,
        label="姓名",
        widget=forms.TextInput(attrs={'maxlength': 20, 'class': 'form-control'})
    )
    email = forms.EmailField(
        max_length=30,
        label="邮箱",
        required=False,
        widget=forms.EmailInput(attrs={'maxlength': 30, 'class': 'form-control'})
    )
    phone = forms.CharField(
        max_length=20,
        label="电话",
        required=False,
        widget=forms.TextInput(attrs={'maxlength': 20, 'class': 'form-control'})
    )

class ProfileForm(forms.ModelForm):
    password = forms.CharField(
        max_length=20,
        label="新密码",
        required=False,
        widget=forms.PasswordInput(attrs={'maxlength': 20, 'class': 'form-control'})
    )
    
    class Meta:
        model = Student
        fields = ['student_name', 'student_email', 'student_phone']
        labels = {
            'student_name': '姓名',
            'student_email': '邮箱',
            'student_phone': '电话',
        }
        widgets = {
            'student_name': forms.TextInput(attrs={'maxlength': 20, 'class': 'form-control'}),
            'student_email': forms.EmailInput(attrs={'maxlength': 30, 'class': 'form-control'}),
            'student_phone': forms.TextInput(attrs={'maxlength': 20, 'class': 'form-control'}),
        }

class AdminRegisterForm(forms.Form):
    account = forms.CharField(
        max_length=20,
        label="管理员账户号",
        widget=forms.TextInput(attrs={'maxlength': 20, 'class': 'form-control'})
    )
    password = forms.CharField(
        max_length=20,
        label="密码",
        widget=forms.PasswordInput(attrs={'maxlength': 20, 'class': 'form-control'})
    )
    name = forms.CharField(
        max_length=20,
        label="姓名",
        widget=forms.TextInput(attrs={'maxlength': 20, 'class': 'form-control'})
    )
    email = forms.EmailField(
        max_length=30,
        label="邮箱",
        required=False,
        widget=forms.EmailInput(attrs={'maxlength': 30, 'class': 'form-control'})
    )
    phone = forms.CharField(
        max_length=20,
        label="电话",
        required=False,
        widget=forms.TextInput(attrs={'maxlength': 20, 'class': 'form-control'})
    )

class BookForm(forms.Form):
    book_title = forms.CharField(
        max_length=50,
        label="图书标题",
        widget=forms.TextInput(attrs={'maxlength': 50, 'class': 'form-control'})
    )
    book_author = forms.CharField(
        max_length=20,
        label="作者",
        widget=forms.TextInput(attrs={'maxlength': 20, 'class': 'form-control'})
    )
    book_publisher = forms.CharField(
        max_length=20,
        label="出版社",
        required=False,
        widget=forms.TextInput(attrs={'maxlength': 20, 'class': 'form-control'})
    )
    book_year = forms.IntegerField(
        label="出版年份",
        required=False,
        widget=forms.NumberInput(attrs={'class': 'form-control'})
    )
    isbn = forms.CharField(
        max_length=13,
        label="ISBN",
        required=False,
        widget=forms.TextInput(attrs={'maxlength': 13, 'class': 'form-control'})
    )
    book_state = forms.CharField(
        max_length=5,
        label="借阅状态",
        required=False,
        widget=forms.TextInput(attrs={'maxlength': 5, 'class': 'form-control'})
    )

class AdminAddStudentForm(forms.Form):
    account = forms.CharField(
        max_length=20,
        label="学生账户号",
        widget=forms.TextInput(attrs={'maxlength': 20, 'class': 'form-control'})
    )
    password = forms.CharField(
        max_length=20,
        label="密码",
        widget=forms.PasswordInput(attrs={'maxlength': 20, 'class': 'form-control'})
    )
    name = forms.CharField(
        max_length=20,
        label="姓名",
        widget=forms.TextInput(attrs={'maxlength': 20, 'class': 'form-control'})
    )
    email = forms.EmailField(
        max_length=30,
        label="邮箱",
        required=False,
        widget=forms.EmailInput(attrs={'maxlength': 30, 'class': 'form-control'})
    )
    phone = forms.CharField(
        max_length=20,
        label="电话",
        required=False,
        widget=forms.TextInput(attrs={'maxlength': 20, 'class': 'form-control'})
    )

class AdminEditStudentForm(forms.Form):
    name = forms.CharField(
        max_length=20,
        label="姓名",
        widget=forms.TextInput(attrs={'maxlength': 20, 'class': 'form-control'})
    )
    email = forms.EmailField(
        max_length=30,
        label="邮箱",
        required=False,
        widget=forms.EmailInput(attrs={'maxlength': 30, 'class': 'form-control'})
    )
    phone = forms.CharField(
        max_length=20,
        label="电话",
        required=False,
        widget=forms.TextInput(attrs={'maxlength': 20, 'class': 'form-control'})
    )
