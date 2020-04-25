from django import forms
from .models import Post, Profile, Comment
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm


class DateInput(forms.DateInput):
    input_type = 'date'


class PostCreateForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = (
            'title',
            'url_address',
            'body',
            'status',
            'restrict_comment',

        )


class PostEditForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = (
            'title',
            'url_address',
            'body',
            'status',
            'restrict_comment',
        )


class UserLoginForm(forms.Form):
    username = forms.CharField(label="")
    password = forms.CharField(label="", widget=forms.PasswordInput)


class UserRegistrationForm(UserCreationForm):
    email = forms.EmailField()
    username = forms.CharField(help_text=" Space telh theih loh!!! "
                                         "(No white space!) Required. 150 characters or fewer. Letters,"
                                         " digits and @/./+/-/_ "
                                         "only.")
    # password = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder': 'Enter Password Here..'}))
    # confirm_password = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder': 'Confirm Password..'}))

    class Meta:
        model = User
        fields = (
            'username',
            # 'first_name',
            # 'last_name',
            'email',
        )        # password = self.cleaned.data.get('password')

        # def clean_confirm_password(self):
        #     confirm_password = self.cleaned_data.get('confirm_password')
        #     if password != confirm_password:
        #         raise forms.ValidationError("Password Mismatch")
        #     return confirm_password


class UserEditForm(forms.ModelForm):
    # username = forms.CharField(widget=forms.TextInput(attrs={'readonly':'readonly'}))
    username = forms.CharField(help_text=" Space telh theih loh!!! "
                                         "(No white space!) Required. 150 characters or fewer. Letters,"
                                         " digits and @/./+/-/_ "
                                         "only.")

    class Meta:
        model = User
        fields = (
            'username',
            'first_name',
            'last_name',
            'email',
        )


class ProfileEditForm(forms.ModelForm):
    class Meta:
        model = Profile
        widgets = {
            'dob': DateInput()
        }
        exclude = ('user',)
        # fields = (
        #     'dob'
        #     'photo',
        # )


class CommentForm(forms.ModelForm):
    content = forms.CharField(label="", widget=forms.Textarea(attrs={'class': 'form-control',
                                                                     'placeholder': 'Text goes here...',
                                                                     'rows': '4', 'cols': '50'}))

    class Meta:
        model = Comment
        fields = ('content',)



