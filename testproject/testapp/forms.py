from django import forms


class TestForm(forms.Form):
    char_field = forms.CharField(max_length=30)
    integer_field = forms.IntegerField(min_value=5, max_value=10)
    date_field = forms.DateField()
