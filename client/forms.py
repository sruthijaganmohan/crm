from django import forms
from .models import Client, Comment, Contact

class AddClientForm(forms.ModelForm):
    class Meta:
        model = Client
        fields = ('name', 'email', 'description')

    def __init__(self, *args, **kwargs):
        super(AddClientForm, self).__init__(*args, **kwargs)

        self.fields['name'].widget.attrs['class'] = 'form-control'
        self.fields['name'].widget.attrs['placeholder'] = 'name'
        self.fields['name'].label = ''

        self.fields['email'].widget.attrs['class'] = 'form-control'
        self.fields['email'].widget.attrs['placeholder'] = 'email'
        self.fields['email'].label = ''

        self.fields['description'].widget.attrs['class'] = 'form-control'
        self.fields['description'].widget.attrs['placeholder'] = 'description'
        self.fields['description'].widget.attrs['rows'] = 3
        self.fields['description'].label = ''

class AddCommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('content',)

    def __init__(self, *args, **kwargs):
        super(AddCommentForm, self).__init__(*args, **kwargs)

        self.fields['content'].widget.attrs['class'] = 'form-control'
        self.fields['content'].widget.attrs['placeholder'] = 'comment'
        self.fields['content'].widget.attrs['rows'] = 2
        self.fields['content'].label = ''

class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = ('subject', 'content', )

    def __init__(self, *args, **kwargs):
        super(ContactForm, self).__init__(*args, **kwargs)

        self.fields['subject'].widget.attrs['class'] = 'form-control'
        self.fields['subject'].widget.attrs['placeholder'] = 'subject'
        self.fields['subject'].label = ''

        self.fields['content'].widget.attrs['class'] = 'form-control'
        self.fields['content'].widget.attrs['placeholder'] = 'content'
        self.fields['content'].widget.attrs['rows'] = 6
        self.fields['content'].label = ''