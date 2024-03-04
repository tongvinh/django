from django.http import HttpResponse
from django.shortcuts import render
from .forms import Contact_Form
from .models import ContactForm
from django.views import View

# Create your views here.
class Contact(View):

    def get(self, request):
        cf = Contact_Form
        return render(request, 'contact/contact.html', {'cf': cf})


    def post(self, request):
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

