from django.http import HttpResponse
from django.shortcuts import render
from .forms import Contact_Form

# Create your views here.
def contact(request):
    cf = Contact_Form
    return render(request, 'contact/contact.html', {'cf': cf})

def getContact(request):
    if request.method == 'POST':
        cf = Contact_Form(request.POST)
        if cf.is_valid():
            cf.save()
            return HttpResponse("Save success")
    else:
        return HttpResponse('Not POST')

