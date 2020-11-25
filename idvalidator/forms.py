from django import forms

from idvalidator.models import Contact


class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        exclude = ('created_at',)
        widgets = {
            'name': forms.TextInput(attrs={'placeholder': 'Jane Doe', }),
            'email': forms.EmailInput(attrs={'placeholder': 'janedoe@example.com', }),
            'business_id': forms.TextInput(attrs={'placeholder': '12345678', }),
        }
