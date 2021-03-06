from django.contrib.auth import authenticate,login,logout
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from .models import Doctor, Patient, Appointment

from django.http import HttpResponse

# Create your views here.
def About(request):
    return render(request,'about.html')

def Home(request):
    return render(request,'home.html')

def Contact(request):
    return render(request,'contact.html')

def Index(request):
    if not request.user.is_staff:
        return redirect('login')
    return render(request,'index.html')

def Login(request):
    error=""
    if request.method=="POST":
        u=request.POST['uname']
        p=request.POST['pwd']
        user=authenticate(username=u, password=p)
        try:
            if user.is_staff:
                login(request,user)
                error="no"
            else:
                error="yes"
        except:
            error="yes"
    d={'error':error}
    return render(request,'login.html',d)

def Logout_admin(request):
    if not request.user.is_staff:
        return redirect('login')
    logout(request)
    return redirect('login')


def View_Doctor(request):
    if not request.user.is_staff:
        return redirect('login')
    doc=Doctor.objects.all()
    d={'doc':doc}
    return render(request,'view_doctor.html',d)


def Delete_Doctor(request,pid):
    if not request.user.is_staff:
        return redirect('login')
    doctor=Doctor.objects.get(id=pid)
    doctor.delete()

    return redirect('view_doctor')


def AddDoctor(request):
    error=""

    if not request.user.is_staff:
        return redirect('login')

    if request.method=="POST":
        n=request.POST['name']
        m=request.POST['mobile']
        sp=request.POST['special']

        try:
            Doctor.objects.create(Name=n, Mobile=m, Specialist=sp)
            error="no"
        except:
            error="yes"
    d={'error':error}
    return render(request,'add_doctor.html',d)

def View_Patient(request):
    if not request.user.is_staff:
        return redirect('login')
    doc=Patient.objects.all()
    d={'doc':doc}
    return render(request,'view_patient.html',d)

def Delete_Patient(request,pid):
    if not request.user.is_staff:
        return redirect('login')
    patient=Patient.objects.get(id=pid)
    patient.delete()

    return redirect('view_patient')

def AddPatient(request):
    error=""

    if not request.user.is_staff:
        return redirect('login')

    if request.method=="POST":
        n=request.POST['name']
        g=request.POST['gender']
        m=request.POST['mobile']
        sp=request.POST['address']

        try:
            Patient.objects.create(Name=n, Gender=g, Mobile=m, Address=sp)
            error="no"
        except:
            error="yes"
    d={'error':error}
    return render(request,'add_patient.html',d)

def AddAppointment(request):
    error=""

    if not request.user.is_staff:
        return redirect('login')

    doctor1=Doctor.objects.all()
    patient1=Patient.objects.all()

    if request.method=="POST":
        n=request.POST['doctor']
        g=request.POST['patient']
        m=request.POST['date']
        sp=request.POST['time']
        doctor=Doctor.objects.filter(Name=n).first()
        patient=Patient.objects.filter(Name=g).first()


        try:
            Appointment.objects.create(doctor=doctor, patient=patient, date=m, time=sp)
            error="no"
        except:
            error="yes"
    d={'doctor':doctor1, 'patient':patient1, 'error':error}
    return render(request,'add_appointment.html',d)

def View_Appointment(request):
    if not request.user.is_staff:
        return redirect('login')
    doc=Appointment.objects.all()
    d={'doc':doc}
    return render(request,'view_appointment.html',d)

def Delete_Appointment(request,pid):
    if not request.user.is_staff:
        return redirect('login')
    patient=Appointment.objects.get(id=pid)
    patient.delete()

    return redirect('view_appointment')
