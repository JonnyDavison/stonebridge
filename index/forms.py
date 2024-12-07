from django import forms
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Submit
from django_summernote.widgets import SummernoteWidget
from .models import ContactSubmission, About, Service



class ContactForm(forms.ModelForm):
    class Meta:
        model = ContactSubmission
        fields = ['name', 'email', 'subject', 'message']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_method = 'post'
        self.helper.form_class = 'space-y-4'
        self.helper.label_class = 'block text-sm font-medium text-color1'
        self.helper.field_class = 'mt-1 block w-full rounded-md border-color1 shadow-sm focus:border-color1 focus:ring focus:border-color1 focus:ring-opacity-50'
        self.helper.layout = Layout(
            'name',
            'email',
            'subject',
            'message',
            Submit('submit', 'Send Message', css_class='w-full bg-custom-color1 hover:bg-custom-color5 text-white font-bold py-2 px-4 rounded-md transition duration-300')
        )
        

class AboutForm(forms.ModelForm):
    class Meta:
        model = About
        fields = ['title', 'sub_title','content', 'image', 'is_active']
        widgets = {
            'content': SummernoteWidget(),
        }
        
class ServiceForm(forms.ModelForm):
    class Meta:
        model = Service
        fields = ['name', 'sub_title', 'description', 'image', 'is_active', 'price', 'order']
        widgets = {
            'description': SummernoteWidget(),
        }