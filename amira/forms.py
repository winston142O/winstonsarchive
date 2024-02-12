from django import forms
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit
from django.utils import timezone

class SentenceForm(forms.Form):
    # Form fields
    sentence = forms.CharField(
        label='Sentence',
        max_length=500,
        widget=forms.TextInput(attrs={'class': 'form-control'})
    )
    date_added = forms.DateTimeField(widget=forms.HiddenInput(), initial=timezone.now)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        
        # Initialize Crispy Forms helper
        self.helper = FormHelper()
        
        # Form attributes
        self.helper.form_id = 'id-exampleForm'
        self.helper.form_class = 'blueForms'
        self.helper.form_method = 'post'
        self.helper.form_action = 'submit_survey'
        
        self.helper.add_input(Submit('submit', 'Submit', css_class='btn btn-outline-info'))
