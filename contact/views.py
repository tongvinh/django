from django.http import HttpResponse
from django.shortcuts import render
from .forms import Contact_Form
from .models import ContactForm

# Create your views here.
def contact(request):
    cf = Contact_Form
    return render(request, 'contact/contact.html', {'cf': cf})


def saveContact(request):
    if request.method == 'POST':
        cf = Contact_Form(request.POST)
        if cf.is_valid():
            saveCF = ContactForm(username=cf.cleaned_data['username'],
                                 email=cf.cleaned_data['email'],
                                 body=cf.cleaned_data['body'])
            saveCF.save()
            return HttpResponse('save success')
    else:
        return HttpResponse('not POST')

