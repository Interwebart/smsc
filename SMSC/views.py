from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required

from SMSC.models import CellNumbers
from SMSC.forms import NameForm, DocumentForm


# Create your views here.
@login_required
def index(request):
    return render(request, 'smsc/index.html')

@login_required
def account(request):
    return render(request, 'smsc/account.html')

@login_required
def billing(request):
    return render(request, 'smsc/billing.html')

@login_required
def submit(request):
    return render(request, 'smsc/submit.html')

@login_required
def ndb(request):
    Numbers=CellNumbers.objects.all()
    context = {'Numbers': Numbers, 'NameForm': NameForm}
    return render(request, 'smsc/ndb.html', context)

@login_required


def upload(request):
    if request.method == 'POST':
        form = DocumentForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('ndb')
    else:
        form = DocumentForm()
    return render(request, 'smsc/upload.html', {
        'form': form
    })








