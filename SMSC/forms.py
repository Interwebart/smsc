from django import forms
from SMSC.models import CellNumbers, UploadFile

import openpyxl

Numbers=CellNumbers.objects.all()
x=[]
context = {'Numbers': Numbers}
for CellNumbers in Numbers:
    x.append(CellNumbers.phone_number)

z=(", ".join(x))


class NameForm(forms.Form):
    your_name1 = forms.CharField(widget=forms.Textarea, initial=z, label='Номера Рассылки')
    importFile= forms.FileField()

class DocumentForm(forms.ModelForm):
        class meta:
            model = UploadFile.document
            fields = ('description', 'document',)