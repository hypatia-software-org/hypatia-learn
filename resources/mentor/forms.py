from django import forms

from civicrm_api import api


class NameForm(forms.Form):
    name = forms.CharField(label='Name', max_length=100)
    pronouns = forms.CharField(label='Pronouns', max_length=100)
    bio = forms.CharField(label='About', widget=forms.Textarea)
    hobbies = forms.CharField(label='Hobbies', max_length=100)
    skills = forms.ChoiceField(
        label='Skills',
        widget=forms.CheckboxSelectMultiple)

    def __init__(self, *args, **kwargs):
        super(NameForm, self).__init__(*args, **kwargs)
        civi_api = api.CivicrmApi()
        tags = civi_api.get_tags()
        tag_choices = []
        for tag in tags['values'].values():
            tag_choices.append([tag['name'], tag['name']])

        self.fields['skills'].choices = tag_choices
        self.fields['skills'].empty_label = ''
