from django import forms
from .models import Memo

CHOICE_FIELD_RECODE_NUMBERS = (
    ('10', '10件'),
    ('15', '15件'),
    ('30', '30件'),
)

class PostForm(forms.ModelForm):
    class Meta:
        model = Memo
        fields = ['content']
        widgets = {
            'content': forms.Textarea
        }

class RecordNumberForm(forms.Form):
    record_number = forms.ChoiceField(widget=forms.Select(attrs={'onchange': 'submit(this.form)'}), choices=CHOICE_FIELD_RECODE_NUMBERS)
