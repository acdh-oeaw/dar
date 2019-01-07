from django import forms
from dal import autocomplete
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit, Layout, Fieldset, Div, MultiField, HTML
from crispy_forms.bootstrap import *

from .models import WebApp


class WebAppForm(forms.ModelForm):

    class Meta:
        model = WebApp
        fields = "__all__"

    def __init__(self, *args, **kwargs):
        super(WebAppForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_tag = True
        self.helper.form_class = 'form-horizontal'
        self.helper.label_class = 'col-md-3'
        self.helper.field_class = 'col-md-9'
        self.helper.add_input(Submit('submit', 'save'),)


class GenericFilterFormHelper(FormHelper):

    def __init__(self, *args, **kwargs):
        super(GenericFilterFormHelper, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.form_class = 'genericFilterForm'
        self.form_method = 'GET'
        self.helper.form_tag = False
        self.add_input(Submit('Filter', 'Search'))


class WebAppFilterFormHelper(FormHelper):
    def __init__(self, *args, **kwargs):
        super(WebAppFilterFormHelper, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.form_class = 'genericFilterForm'
        self.form_method = 'GET'
        self.helper.form_tag = False
        self.add_input(Submit('Filter', 'Search'))
        self.layout = Layout(
            Accordion(
                AccordionGroup(
                    'Basic',
                    'title',
                    'subtitle',
                    css_id="more"
                    ),
                AccordionGroup(
                    'Advanced',
                    'app_type',
                    'base_tech',
                    'framework',
                    'created_at',
                    css_id="datierung"
                    ),
                )
            )
