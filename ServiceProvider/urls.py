from django.urls import path,include
from .views import *
app_name = 'SP'
urlpatterns=[
    path('',getLogin,name='login'),
    path('valLog/',validateLogin,name='valLog'),
    path('index/',getIndex,name='index'),
    path('appointment-details',viewApp,name='viewApp'),
    path('forgot-password',getForgotPassword,name='forpass'),
    path('forgot-password/sendmail',sendLink,name='link'),
    path('forgot-password/mail',getResetPass,name='res'),
    path('change-password',changePass,name='ch'),
    path('reset-password/',valToken,name='getres'),
    path('logout',spLogOut,name='spLogOut'),
    path('bookings/',getBookings,name='getBookings'),
    path('attendants/',getAttendant,name='getAttendants'),
    path('attendants/add',addAttendant,name='addAttendant'),
    path('attendants/update',getUpdateAttendant,name='upAttendant'),
    path('attendants/update/done',UpdateAttendant,name='upapp'),
    path('myservices/',getService,name='service'),
    path('myservices/update',getUpdateService,name='upser'),
    path('myservices/updated',updateService,name='asdf'),
    path('myservices/remove',removeService,name='remser'),
    path('myservices/add',addService,name='addser'),
    path('myprofile',getProfile,name='profile'),
    path('myprofile/change-password',changePassword,name='cp'),
    path('myprofile/update',updateProfile,name='uprofile'),
    path('attendants/remove',removeAttendant,name='rematt')
]