from django import forms
from .models import Team

class TeamForm(forms.ModelForm):
    class Meta:
        model = Team
        fields = ['name', 'member1', 'member2', 'member3', 'member4']

    def __init__(self, *args, **kwargs):
        super(TeamForm, self).__init__(*args, **kwargs)

        self.fields['name'].widget.attrs['class'] = 'form-control'
        self.fields['name'].widget.attrs['placeholder'] = 'name'
        self.fields['name'].label = ''

        self.fields['member1'].widget.attrs['class'] = 'form-control'
        self.fields['member1'].widget.attrs['placeholder'] = 'member 1'
        self.fields['member1'].label = ''

        self.fields['member2'].widget.attrs['class'] = 'form-control'
        self.fields['member2'].widget.attrs['placeholder'] = 'member 2'
        self.fields['member2'].widget.attrs['rows'] = 3
        self.fields['member2'].label = ''

        self.fields['member3'].widget.attrs['class'] = 'form-control'
        self.fields['member3'].widget.attrs['placeholder'] = 'member 3'
        self.fields['member3'].label = ''

        self.fields['member4'].widget.attrs['class'] = 'form-control'
        self.fields['member4'].widget.attrs['placeholder'] = 'member 4'
        self.fields['member4'].label = ''
