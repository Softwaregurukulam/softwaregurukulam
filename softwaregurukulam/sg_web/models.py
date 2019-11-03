from django.db import models
from autoslug import AutoSlugField
from django import forms
from django.core.exceptions import ValidationError
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class UserCreateForm(UserCreationForm):
    email = forms.EmailField(required=True,
                         label='Email',
                         error_messages={'exists': 'Oops'})

    class Meta:
        model = User
        fields = ("username", "email", "password1", "password2")
        
    def save(self, commit=True):
        user = super(UserCreateForm, self).save(commit=False)
        user.email = self.cleaned_data["email"]
        if commit:
            user.save()
        return user

    def clean_email(self):
        if User.objects.filter(email=self.cleaned_data['email']).exists():
            raise ValidationError(self.fields['email'].error_messages['exists'])
        return self.cleaned_data['email']
    
class Category(models.Model):
    name = models.CharField(max_length=128, unique=True)
    description = models.CharField(max_length=256, blank=True)
    views = models.IntegerField(default=0)
    slug = AutoSlugField(populate_from='name', unique=True)
    status = models.BooleanField(default=True)
    created_at = models.DateTimeField(null=True, auto_now_add=True)
    updated_at = models.DateTimeField(null=True, auto_now=True)

    def __str__(self):
        return self.name

class Course(models.Model):
    category = models.ForeignKey(Category)
    title = models.CharField(max_length=128)
    url = models.URLField()
    summary = models.CharField(max_length=256, blank=True)
    phone = models.CharField(max_length=15)
    startingdate = models.DateField(auto_now=False, 
                                    auto_now_add=False, 
                                    null=True, blank=True)
    hascertification = models.BooleanField(default=False)
    status = models.BooleanField(default=True)
    views = models.IntegerField(default=0)
    
    def __str__(self):
        return self.title
    