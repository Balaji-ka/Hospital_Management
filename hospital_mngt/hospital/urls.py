from django.urls import path
from .views import About, Home, Contact, Login, Logout_admin, Index, View_Doctor, Delete_Doctor, AddDoctor, \
    View_Patient, Delete_Patient, AddPatient, Delete_Appointment, View_Appointment, AddAppointment

urlpatterns = [
    path('',Home,name='home'),
    path('about/',About,name='about'),
    path('contact/',Contact,name='contact'),
    path('admin_login/',Login,name='login'),
    path('logout/', Logout_admin, name='logout_admin'),
    path('index/', Index, name='dashboard'),
    path('view_doctor/', View_Doctor, name='view_doctor'),
    path('delete_doctor(?P<int:pid>)/', Delete_Doctor, name='delete_doctor'),
    path('add_doctor/',AddDoctor, name='add_doctor'),
    path('view_patient/', View_Patient, name='view_patient'),
    path('delete_patient(?P<int:pid>)/', Delete_Patient, name='delete_patient'),
    path('add_patient/', AddPatient, name='add_patient'),
    path('view_appointment/', View_Appointment, name='view_appointment'),
    path('delete_appointment(?P<int:pid>)/', Delete_Appointment, name='delete_appointment'),
    path('add_appointment/', AddAppointment, name='add_appointment'),
]