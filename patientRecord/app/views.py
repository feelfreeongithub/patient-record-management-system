from django.shortcuts import render, redirect,HttpResponse
from django.core.mail import send_mail
from .models import Patient
from .forms import PatientForm
from django.contrib import messages
from django.db.models import Q
from django.core.paginator import Paginator

# Create your views here.


def Home(request):
    data=Patient.objects.all()
    if 'q' in request.GET:
        q=request.GET['q']
        data=Patient.objects.filter(Q(full_name__icontains=q)|Q(mobile_no__icontains=q)|Q(email__icontains=q))
    paginator=Paginator(data,1)
    page_number=request.GET.get('page',1)
    data=paginator.get_page(page_number)    
    return render(request, 'Home.html', {'data': data})

# Add Patient


def addpatient(request):
    form = PatientForm
    if request.method =='POST':
        saveForm = PatientForm(request.POST)
        if saveForm.is_valid():
            saveForm.save()
            messages.success(request,'Data has been added.')
    return render(request,'add-patient.html',{'form': form})

# Update Patient


def updatepatientdata(request, id):
    patient = Patient.objects.get(id=id)
    if request.method == 'POST':
        saveForm = PatientForm(request.POST, instance=patient)
        if saveForm.is_valid():
            saveForm.save()
            messages.success(request, 'Data has been updated.')
    form = PatientForm(instance=patient)
    return render(request, 'update-patient data.html', {'form': form})

# Delete Data


def deletepatientdata(request, id):
    Patient.objects.filter(id=id).delete()
    return redirect('/')

#Send Email

def SendEmail(request,id):
    patient=Patient.objects.get(id=id)
    send_mail(
        'Next Visit Reminder',
        'your next visit is on'+ str(patient.next_visit_date),
        'admin@example.com',
        [patient.email],
        fail_silently=False,
    )
    messages.success(request,'Mail has been sent.')  
    return redirect('/')


     
    

