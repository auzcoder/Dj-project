from django import forms
from django.db.models import Model
from news.models import New

class LoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)

class AdminNewsUpdateForm(forms.ModelForm):
    class Meta:
        model = New
        fields = ('name', 'description', 'full_info', 'header_images', 'category', 'sub_category', 'status')
        # name = forms.CharField(max_length=200)
        # description = forms.CharField(max_length=200)
        widgets = {'name': forms.TextInput(
            attrs={'class': "form-control", 'type': "text", 'placeholder': "Post nomi"}
        ),
            'description': forms.TextInput(
                attrs={'class': "form-control", 'placeholder': "Ma\'lumot", 'type': "text"}
            ),
            'full_info': forms.Textarea(
                attrs={'class': "form-control"}
            ),
            # 'header_images': forms.FileInput(
            #      attrs={'class': 'custom-file-input', 'type': 'file'}
            #  ),
            'category': forms.TextInput(
                attrs={'class': "custom-select2 form-control", 'multiple': "multiple", 'style': 'width=100%'}
            ),

        }
