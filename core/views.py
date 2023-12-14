from django.shortcuts import render

from core.models import *


# Create your views here.

def index(request):
    return render(request, 'core/index.html', )


def contact(request):
    if request.method == 'POST':
        contact = Contact_us(
            name=request.POST.get('name'),
            subject=request.POST.get('subject'),
            email=request.POST.get('email'),
            message=request.POST.get('message'),
        )
        contact.save()
    return render(request, 'core/contact.html')



def about(request):
    return render(request,'core/about.html')



def yoga(request):
    return render(request,'core/yoga.html')



def meeting(request):
    return render(request,'core/meeting.html', {'name': request.user.username})



def disorders(request):
    return render(request,'core/disorders.html')


def anxiety(request):
    return render(request,'core/anxiety.html')


def mood(request):
    return render(request,'core/mood.html')


def psychotic(request):
    return render(request,'core/psychotic.html')


def eating(request):
    return render(request,'core/eating.html')


def personality(request):
    return render(request,'core/personality.html')


def neurodevelopment(request):
    return render(request,'core/neurodevelopment.html')


def dissociative(request):
    return render(request,'core/dissociative.html')


def trauma(request):
    return render(request,'core/trauma.html')


def sleep(request):
    return render(request,'core/sleep.html')



def Substance_Disorders(request):
    return render(request,'core/Substance_Disorders.html')



def neurocoginitive(request):
    return render(request,'core/neurocoginitive.html')



def somatoform(request):
    return render(request,'core/somatoform.html')