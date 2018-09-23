from django import forms
from django.forms import ModelForm
from SMSC.models import CellNumbers, UploadFile
from .models import Account, Sends

import openpyxl

Numbers=CellNumbers.objects.all()
x=[]
context = {'Numbers': Numbers}
for CellNumbers in Numbers:
    x.append(CellNumbers.phone_number)
z=(", ".join(x))


class NameForm(ModelForm):
    class Meta:
        model=Sends
        fields=['NumberField', 'MessageField']
    # your_name1 = forms.CharField(widget=forms.Textarea(attrs={'class' : 'btn btn-danger'}), initial=z, label='Номера Рассылки')
    # importFile= forms.FileField()

class DocumentForm(forms.ModelForm):
        class meta:
            model = UploadFile.document
            fields = ('description', 'document',)

class AccountForm(ModelForm):
    class Meta:
        model=Account
        fields=['AccLogin', 'AccName', 'AccOrg', 'AccMail']

    def __init__(self, *args, **kwargs):
        super(AccountForm, self).__init__(*args, **kwargs)
        self.fields['AccMail'].widget.attrs.update({'class' : 'btn'})