from django.forms.widgets import ClearableFileInput
from django.utils.translation import gettext_lazy as _
from django.template.loader import render_to_string

class CustomClearableFileInput(ClearableFileInput):
    clear_checkbox_label = _('Remove')
    initial_text = _('Current Image')
    input_text = _('Change Image')
    template_name = 'products/custom_widget_templates/custom_clearable_file_input.html'

    def get_context(self, name, value, attrs):
        context = super().get_context(name, value, attrs)
        context['widget'].update({
            'is_initial': self.is_initial(value),
            'input_text': self.input_text,
            'initial_text': self.initial_text,
            'clear_checkbox_label': self.clear_checkbox_label,
        })
        return context

    def render(self, name, value, attrs=None, renderer=None):
        context = self.get_context(name, value, attrs)
        return render_to_string(self.template_name, context)

class MultipleImageInput(ClearableFileInput):
    allow_multiple_selected = True

class CustomMultipleImageInput(MultipleImageInput):
    template_name = 'products/custom_widget_templates/custom_multiple_file_input.html'
    clear_checkbox_label = _('Remove')
    initial_text = _('Current Images')
    input_text = _('Add Images')

    def get_context(self, name, value, attrs):
        context = super().get_context(name, value, attrs)
        context['widget'].update({
            'is_initial': self.is_initial(value),
            'input_text': self.input_text,
            'initial_text': self.initial_text,
            'clear_checkbox_label': self.clear_checkbox_label,
        })
        return context

    def render(self, name, value, attrs=None, renderer=None):
        context = self.get_context(name, value, attrs)
        return render_to_string(self.template_name, context)
