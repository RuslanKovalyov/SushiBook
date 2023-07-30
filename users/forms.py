from django.contrib.auth.forms import UserCreationForm
from django.http import request
from users.models import CustomUser

class RegisterForm(UserCreationForm):
    class Meta:
        model = CustomUser
        fields = ['email', 'password1', 'password2']


from django import forms
from .models import CustomUser, Post, Profile, PostLike

# bootstrap ? attrs={'class': 'form-control'}
class UpdateCustomUserForm(forms.ModelForm):
    email = forms.EmailField(required=True,
                             widget=forms.TextInput(attrs={'class': 'form-control'}))

    class Meta:
        model = CustomUser
        fields = ['email',]

from django_countries.fields import CountryField
#from phonenumber_field.formfields import PhoneNumberField

class UpdateProfileForm(forms.ModelForm):
    #avatar = forms.ImageField(widget=forms.FileInput(attrs={'class': 'form-control-file'}))
    #bio = forms.CharField(widget=forms.Textarea(attrs={'class': 'form-control', 'rows': 5}))
    first_name = forms.CharField(max_length=100,
                               required=True,
                               widget=forms.TextInput(attrs={'class': 'form-control'}))
    last_name = forms.CharField(max_length=100,
                               required=True,
                               widget=forms.TextInput(attrs={'class': 'form-control'}))
    
    country = CountryField().formfield()
    city = forms.CharField(max_length=100,
                               required=False,
                               widget=forms.TextInput(attrs={'class': 'form-control'}))

    phone = forms.CharField(max_length=16, required=False,)
    #phone = PhoneNumberField()



    avatar = forms.ImageField(widget=forms.FileInput(attrs={'class': 'form-control-file'}))

    profile_background = forms.ImageField(widget=forms.FileInput(attrs={'class': 'form-control-file'}))


    current_position = forms.CharField(max_length=255,
                            required=False,
                            widget=forms.TextInput(attrs={'class': 'form-control'}))
    
    credo = forms.CharField(max_length=255,
                            required=False,
                            widget=forms.TextInput(attrs={'class': 'form-control'}))
    
    #avatar = forms.ImageField(widget=forms.FileInput(attrs={'class': 'form-control-file'}))

    YEARS= [x for x in range(1940,2021)]
    date_of_birth = forms.DateField(label='What is your birth date?',
                                    widget=forms.SelectDateWidget(years=YEARS))



    class Meta:
        model = Profile
        fields = ['first_name', 'last_name', 'date_of_birth','avatar', 'country', 'city', 'phone', 'profile_background', 'current_position', 'credo',]
    
class CreatePostForm(forms.ModelForm):

    class Meta:
        model = Post
        fields = ['picture','story','title', ]

class RenewPostForm(forms.ModelForm):
    #title = forms.CharField(max_length=200, help_text="Post title.")

    class Meta:
        model = Post
        fields = ['title', 'story',]
        #picture not work!

class LikePostForm(forms.ModelForm):

    class Meta:
        model = PostLike
        fields = ['user','post', ]