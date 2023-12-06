from django import forms
from utils.models import ContactUs

class ContactUs_Msg_Form(forms.ModelForm):
    class Meta:
        model = ContactUs
        fields = ['name', 'email', 'phone_no', 'message', 'by_login_user','is_replyed','is_ignored']

    def __init__(self, *args, **kwargs):
        super(ContactUs_Msg_Form, self).__init__(*args, **kwargs)
        self.fields['name'].widget.attrs['readonly'] = True
        self.fields['email'].widget.attrs['readonly'] = True
        self.fields['phone_no'].widget.attrs['readonly'] = True
        self.fields['message'].widget.attrs['readonly'] = True

    def clean_name(self):
        if self.instance and self.cleaned_data['name'] != self.instance.name:
            raise forms.ValidationError("Name cannot be edited.")
        return self.cleaned_data['name']

    def clean_email(self):
        if self.instance and self.cleaned_data['email'] != self.instance.email:
            raise forms.ValidationError("Email cannot be edited.")
        return self.cleaned_data['email']

    def clean_phone_no(self):
        if self.instance and self.cleaned_data['phone_no'] != self.instance.phone_no:
            raise forms.ValidationError("Phone number cannot be edited.")
        return self.cleaned_data['phone_no']
    
    def clean_message(self):
        if self.instance and self.cleaned_data['message'] != self.instance.message:
            raise forms.ValidationError("message cannot be edited.")
        return self.cleaned_data['message']