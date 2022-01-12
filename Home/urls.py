from django.urls import path,include
from .views import *
app_name = 'Home'
urlpatterns = [
    path('',getAdminLogin,name='getAdminLogin'),
    path('loggedout/',adminLogOut,name='logout'),
    path('index/',validateAdminLogin,name='validateAdmin'),
    path('Index/',getIndex,name='index2'),
    path('service-provider/',getServiceOp,name='serviceop'),
    path('service-provider/validate',validateSPForm,name='valsp'),
    path('service-provider/add',getAddSer,name='addser'),
    path('service-provider/getcity',sendCity,name='addc'),
    path('service-provider/update',getUpdateForm,name='update'),
    path('service-provider/view',viewSP,name='viewsp'),
    path('service-provider/update/validate',validateUpdateForm,name='validate'),
    path('customer/',getCustomer,name='customer'),
    path('bookings/',getBooking,name='bookings'),
    path('bookings/view',updateApp,name='up-app'),
    path('bookings/offers',addOffer,name='addoff'),
    path('others/',getOthers,name='others'),
    path('others/add-service',addSer,name='addser'),
    path('others/add-city',addCity,name='addCity'),
    path('others/add-state',addState,name='addState')
]