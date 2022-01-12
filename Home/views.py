from django.shortcuts import render,HttpResponse,HttpResponseRedirect,redirect
from django.urls import reverse
from .models import City,State,Offer,Service
from django.contrib.auth.models import User
from ServiceProvider.models import OperatorProfile,Attendant,OperatorService
from Customer.models import Customer_Profile
from Appointments.models import Appointment
from django.http import HttpResponse,JsonResponse
from ServiceProvider.models import OperatorProfile
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate,login,logout
from passlib.hash import django_pbkdf2_sha256
from django.core import serializers
# Create your views here.
def adminLogOut(request):
    logout(request)
    template='s-Admin/login.html'
    return render(request,template,{'pass':True,'name':True})
def getAdminLogin(request):
    if request.user.is_authenticated:
        return getIndex(request)
    else:
        template='s-Admin/login.html'
        return render(request,template,{})
@login_required(login_url='/s-admin/')
def getIndex(request):
    if isAdmin(request):
        template='s-Admin/index.html'
        name=request.user.first_name
        apcount=Appointment.objects.raw('Select ap_id,count(ap_id) as acount from Appointments_appointment')
        cuscount=Customer_Profile.objects.raw('Select id,count(id) as ccount from Customer_Customer_Profile')
        spcount=OperatorProfile.objects.raw('Select id,count(id) as spcount from ServiceProvider_operatorprofile')
        operators=OperatorProfile.objects.raw('Select auth_user.id,auth_user.username,ServiceProvider_OperatorProfile.firm_name,ServiceProvider_OperatorProfile.owner_name,Home_city.city_name,ServiceProvider_OperatorProfile.contact from ServiceProvider_OperatorProfile,Home_city,auth_user where auth_user.id=ServiceProvider_OperatorProfile.user_id and Home_city.city_id=ServiceProvider_OperatorProfile.city_id and ServiceProvider_Operator_Profile.is_active=1')
        data={'name':name,'operators':operators,'ap':apcount,'sp':spcount,'cp':cuscount,}
        return render(request,template,data)
    else:
        return HttpResponse('You should not be here.')
def validateAdminLogin(request):
    user=request.POST.get('username')
    passw=request.POST.get('password')
    bool1=User.objects.filter(username=user,is_superuser=True).exists()
    if bool1:
        bool2=authenticate(username=user,password=passw)
        if bool2 is not None:
            login(request,bool2)
            data={'success':True,'url':'/s-admin/Index/'}
            return JsonResponse(data)      
        else:
            data={'success':False,'name':True,'pass':False}
            return JsonResponse(data)
    else:
        data={'success':False,'pass':True,'name':False}
        return JsonResponse(data)
@login_required
def getServiceOp(request):
    if isAdmin(request):
        curr=request.user.first_name
        operators=OperatorProfile.objects.raw('Select auth_user.id,auth_user.email,auth_user.username,ServiceProvider_OperatorProfile.firm_name,ServiceProvider_OperatorProfile.owner_name,Home_city.city_name,ServiceProvider_OperatorProfile.contact,ServiceProvider_OperatorProfile.id from ServiceProvider_OperatorProfile,Home_city,auth_user where auth_user.id=ServiceProvider_OperatorProfile.user_id and Home_city.city_id=ServiceProvider_OperatorProfile.city_id and ServiceProvider_OperatorProfile.is_active=1')
        attendants=Attendant.objects.raw('Select ServiceProvider_attendant.at_id,ServiceProvider_attendant.at_name,ServiceProvider_attendant.gender,ServiceProvider_attendant.contact,ServiceProvider_OperatorProfile.firm_name from ServiceProvider_attendant,ServiceProvider_OperatorProfile where ServiceProvider_attendant.ser_pro_id = ServiceProvider_OperatorProfile.id and ServiceProvider_attendant.is_active=1')
        template='s-Admin/serviceprovider.html'
        city=City.objects.all
        state=State.objects.all
        suc=request.GET.get('upsuccess')
        asuc=request.GET.get('adsuccess')

        data={'name':curr,'operators':operators,'attendants':attendants,'cities':city,'states':state,'suc':suc,'asuc':asuc}
        return render(request,template,data)
    else:
        return HttpResponse('Sorry page does not exists')
def validateSPForm(request):
    uname=request.POST.get('username')    
    email=request.POST.get('email')
    password1=request.POST.get('password')
    hashpass=django_pbkdf2_sha256.encrypt(password1,rounds=12000,salt_size=12)
    fname=request.POST.get('firm_name')
    oname=request.POST.get('owner_name')
    #image=request.FILES['image']
    contact=request.POST.get('contact')
    address=request.POST.get('address')
    city=City.objects.get(city_id=request.POST.get('city'))
    state=State.objects.get(state_id=request.POST.get('state'))
    ubool=User.objects.filter(username=uname).exists()
    if ubool:
        data={
            'success':False,
        }
        return JsonResponse(data)
    else:       
        u=User(username=uname,email=email,password=hashpass)
        u.save()
        user=User.objects.get(username=request.POST.get('username'))  
        Op=OperatorProfile(user=user,firm_name=fname,owner_name=oname,contact=contact,address=address,city=city,state=state,uname=uname)
        Op.save()
        data={'success':True}
        return JsonResponse(data)
@login_required
def getUpdateForm(request):
    if isAdmin(request):
        user=request.POST.get('user')
        uobjid=User.objects.get(username=user).id
        uobj=User.objects.get(username=user)
        admin=request.user.first_name
        sobj=OperatorProfile.objects.get(user_id=uobjid)
        city=City.objects.filter(is_active=1)
        state=State.objects.filter(is_active=1)
        template="s-Admin/update-sp.html"
        data={'uobj':uobj,'admin':admin,'sobj':sobj,'cities':city,'states':state}
        return render(request,template,data)

@login_required
def validateUpdateForm(request):
    uid=request.POST.get('but')
    sobj=OperatorProfile.objects.get(user_id=uid)
    oname=request.POST.get('oname')
    fname=request.POST.get('fname')
    contact=request.POST.get('contact')
    #email=request.POST.get('email')
    address=request.POST.get('address')
    bio=request.POST.get('bio')
    city=City.objects.get(city_id=request.POST.get('city'))
    state=State.objects.get(state_id=request.POST.get('state'))
    #sobj(firm_name=fname,owner_name=oname,contact=contact,address=address,city=city,state=state,bio=bio)
    sobj.firm_name=fname
    sobj.owner_name=oname
    sobj.contact=contact
    sobj.address=address
    sobj.city=city
    sobj.state=state
    sobj.bio=bio
    sobj.save()
    return redirect('/s-admin/service-provider?upsuccess=True')
@login_required
def getCustomer(request):
    if isAdmin(request):
        template='s-Admin/customer.html'
        customer=Customer_Profile.objects.raw('Select id,first_name,last_name,username,email,is_active from auth_user where id IN (select user_id from Customer_customer_profile)')
        cus_profile=Customer_Profile.objects.raw('Select a.id,a.username,a.first_name,a.last_name,a.email,a.last_login,a.date_joined,c.image,c.contact,c.gender,c.address,ct.city_name,st.state_name from auth_user a,Customer_customer_profile c,Home_city ct,Home_state st where a.id=c.user_id and c.city_id = ct.city_id and c.state_id = st.state_id')
        uname=request.user.first_name
        data={'name':uname,'customers':customer,'cuss':cus_profile}
        return render(request,template,data)

@login_required
def getBooking(request):
    if isAdmin(request):
        template='s-Admin/booking.html'
        ap_detail=Appointment.objects.raw('Select a.ap_id,c.usname,s.uname,a.bdate,a.adate,o.time_from,a.status from Appointments_appointment a, Customer_customer_profile c, ServiceProvider_operatorprofile s, ServiceProvider_operatorservice o where a.user_id=c.id and a.op_sr_id=o.op_ser and o.provider_id=s.id') 
        offers=Offer.objects.raw('Select * from Home_offer where is_active=1')
        uname=request.user.first_name
        data={'name':uname,'appointments':ap_detail,'offers':offers}
        return render(request,template,data)
@login_required
def updateApp(request):
    if isAdmin(request):
        template='s-Admin/up-appointment.html'
        uname=request.user.first_name
        apno=request.GET.get('ap')
        ap_detail=Appointment.objects.raw('Select a.ap_id,a.bdate,a.adate,o.time_from,t.ser_name,o.time_to,o.price,a.status from Appointments_appointment a, Customer_customer_profile c, ServiceProvider_operatorservice o,Home_service t where a.user_id=c.id and a.op_sr_id=o.op_ser and o.ser_id_id=t.ser_id and a.ap_id={}'.format(apno))
        c_detail=Appointment.objects.raw('Select a.ap_id,c.usname,u.first_name,u.last_name,c.contact,u.email from Customer_customer_profile c, auth_user u,Appointments_appointment a where a.user_id = c.id and c.user_id = u.id and a.ap_id={}'.format(apno))
        sp_detail=Appointment.objects.raw('Select a.ap_id,s.uname,s.owner_name,s.contact,c.city_name,st.state_name,s.address,u.email from Appointments_appointment a,ServiceProvider_operatorprofile s,Home_city c,Home_state st,auth_user u,ServiceProvider_operatorservice os where a.op_sr_id = os.op_ser and os.provider_id=s.id and s.user_id=u.id and s.city_id = c.city_id and s.state_id = st.state_id and a.ap_id={}'.format(apno))
        data={'name':uname,'ap':ap_detail,'cp':c_detail,'sp':sp_detail}  
        return render(request,template,data)

def getAddSer(request):
    if isAdmin(request):
        template='s-Admin/add-serviceprovider.html'
        city=City.objects.filter(is_active=1)
        state=State.objects.filter(is_active=1)
        curr=request.user.first_name
        data={'name':curr,'cities':city,'states':state} 
        return render(request,template,data)

def sendCity(request):
    sid=request.GET.get('sid')
    city=City.objects.filter(state_id=sid)
    data={}
    lista=[]
    listb=[]
    for c in city:
        lista.append(c.city_id)
        listb.append(c.city_name)
    data={'city_id':lista,'city_name':listb,'length':len(lista)}
    return JsonResponse(data)
def addOffer(request):
    if isAdmin(request):
        off_id=request.POST.get('off_id')
        off_name=request.POST.get('off_name')
        off_from=request.POST.get('off_from')
        off_to=request.POST.get('off_to')
        disc_rat=request.POST.get('disc_rat')
        maxamt=request.POST.get('maxamt')
        bool1=Offer.objects.filter(offer_id=off_id).exists()
        if bool1:
            data={
                'success':False,
            }
            return JsonResponse(data)
        else:
            off=Offer(offer_id=off_id,offer_name=off_name,offer_from=off_from,offer_to=off_to,disc_ratio=disc_rat,maxamount=maxamt)
            off.save()
            data={
                'success':True,
            }
            return JsonResponse(data)

@login_required
def getOthers(request):
    if isAdmin(request):
        template='s-Admin/others.html'
        curr=request.user.first_name
        services=Service.objects.raw('Select * from Home_service where is_active=1')
        city=City.objects.raw('Select * from Home_city c,Home_state s where c.city_id > 0 and c.state_id = s.state_id LIMIT 5')
        state=State.objects.raw('Select * from Home_state where state_id>0 LIMIT 5')
        data={'name':curr,'services':services,'cities':city,'states':state} 
        return render(request,template,data)

@login_required
def addSer(request):
    sername=request.POST.get('sername')
    gen=request.POST.get('gender')
    pos=request.FILES['poster']
    ser=Service(ser_name=sername,gender=gen,poster=pos)
    ser.save()
    return redirect('/s-admin/others')
@login_required
def addCity(request):
    city_name=request.POST.get('city_name')
    state_id=request.POST.get('state_id')
    cit=City(city_name=city_name,state_id=state_id)
    cit.save()
    return redirect('/s-admin/others')
@login_required
def addState(request):
    state_name=request.POST.get('state_name')
    st=State(state_name=state_name)
    st.save()
    return redirect('/s-admin/others')

@login_required
def viewSP(request):
    if isAdmin(request):
        curr=request.user.first_name
        sp_id=request.POST.get('sp_id')
        sobj=OperatorProfile.objects.get(user_id=sp_id)
        sobj=OperatorProfile.objects.raw('Select auth_user.id,auth_user.username,ServiceProvider_OperatorProfile.firm_name,ServiceProvider_OperatorProfile.owner_name,Home_city.city_name,ServiceProvider_OperatorProfile.contact,Home_state.state_name,ServiceProvider_OperatorProfile.bio,ServiceProvider_OperatorProfile.image,ServiceProvider_OperatorProfile.address from ServiceProvider_OperatorProfile,Home_city,Home_state,auth_user where auth_user.id=ServiceProvider_OperatorProfile.user_id and Home_city.city_id=ServiceProvider_OperatorProfile.city_id and Home_state.state_id=ServiceProvider_OperatorProfile.state_id and ServiceProvider_OperatorProfile.user_id={}'.format(sp_id))
        uobj=User.objects.get(id=sp_id)
        sp2_id=OperatorProfile.objects.get(user_id=sp_id).id
        serobj=OperatorService.objects.raw('Select sp.op_ser,a.contact,s.ser_name,s.gender,a.at_name,sp.time_from,sp.time_to,sp.price from ServiceProvider_operatorservice sp,Home_service s,ServiceProvider_attendant a where sp.ser_id_id=s.ser_id and sp.attendant_id = a.at_id and sp.is_active=1 and sp.provider_id={}'.format(sp2_id))
        ser_count=OperatorService.objects.raw('Select sp.op_ser,count(sp.op_ser) as sercount from ServiceProvider_operatorservice sp,Home_service s,ServiceProvider_attendant a where sp.ser_id_id=s.ser_id and sp.attendant_id = a.at_id and sp.is_active=1 and sp.provider_id={}'.format(sp2_id))
        att=Attendant.objects.raw('Select * from ServiceProvider_attendant where is_active=1 and ser_pro_id={}'.format(sp2_id))
        atcount=Attendant.objects.raw('Select at_id,count(at_id) as apcount from ServiceProvider_attendant where is_active=1 and ser_pro_id={}'.format(sp2_id))
        apcount=Appointment.objects.raw('Select ap_id,count(ap_id) as apcount from Appointments_appointment where op_sr_id=(Select op_ser from ServiceProvider_operatorservice WHERE provider_id = {})'.format(sp2_id))
        data={
                'sobjs':sobj,
                'uobj':uobj,
                'sp':serobj,
                'scount':ser_count,
                'att':att,
                'name':curr,
                'attc':atcount,
                'ap':apcount
            }
        template='s-Admin/view-serviceprovider.html'
        return render(request,template,data)  

def isAdmin(request):
    uname=request.user.username
    bool1=User.objects.filter(username=uname,is_superuser=True).exists()
    if bool1:
        return True
    else:
        return False