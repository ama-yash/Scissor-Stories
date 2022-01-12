import secrets
from django.shortcuts import render,HttpResponse,HttpResponseRedirect,redirect
from django.urls import reverse
from Home.models import City,State,Offer,Service
from django.contrib.auth.models import User
from .models import OperatorProfile,Attendant,OperatorService
from Customer.models import Customer_Profile,Tokens
from Appointments.models import Appointment
from django.http import HttpResponse,JsonResponse
from .models import OperatorProfile
from django.contrib.auth.decorators import login_required,user_passes_test
from django.contrib.auth import authenticate,login,logout
from passlib.hash import django_pbkdf2_sha256
from django.core import serializers
from django.core.mail import send_mail
# Create your views here.

def isProvider(request):
    uname=request.user.username
    bool2=OperatorProfile.objects.filter(uname=uname).exists()
    if bool2:
        return True
    else:
        return False
def getLogin(request):
    if request.user.is_authenticated:
        return getIndex(request)
    else:
        template='SP/login.html'
        data={}
        return render(request,template,data)
def validateLogin(request):
    uname=request.POST.get('username')
    password1=request.POST.get('password')
    #passs=pbkdf2_sha256.encrypt(password1,rounds=12000,salt_size=32)
    bool1=User.objects.filter(username=uname).exists()
    bool2=OperatorProfile.objects.filter(uname=uname,is_active=1).exists()
    if bool1 and bool2:
        user=authenticate(username=uname,password=password1)
        if user is not None:
            login(request,user)
            data={
                'success':True,
                'url':'/service-provider/index'
            }
            return JsonResponse(data)
        else:
            data={
                'success':False,
                'name':True,
                'pass':False
            }
            return JsonResponse(data)
    else:
        data={
            'success':False,
            'pass':True,
            'name':False
        }
        return JsonResponse(data)
@login_required(login_url='/service-provider/')
def getIndex(request):
    if isProvider:
        template='SP/index.html'
        sp_no=OperatorProfile.objects.get(uname=request.user.username).id
        apcount=Appointment.objects.raw('Select ap_id,count(ap_id) as acount from Appointments_appointment where op_sr_id = (Select op_ser from ServiceProvider_operatorservice where provider_id = {})'.format(sp_no))
        atcount=Attendant.objects.raw('select at_id,count(at_id) as atcount from ServiceProvider_attendant where is_active=1 and ser_pro_id={}'.format(sp_no))
        todapp=Appointment.objects.raw('select a.ap_id,c.first_name,c.last_name,cp.contact,os.time_from from Appointments_appointment a,auth_user c,Customer_customer_profile cp,ServiceProvider_operatorservice os where adate = CURRENT_DATE and cp.user_id = c.id and a.status=1 and os.provider_id={}'.format(sp_no))
        upapp=Appointment.objects.raw('select a.ap_id,c.first_name,c.last_name,cp.contact,a.adate,os.time_from from Appointments_appointment a,auth_user c,Customer_customer_profile cp,ServiceProvider_operatorservice os where cp.user_id = c.id and a.user_id=cp.id and os.op_ser = a.op_sr_id and a.status=1 and a.adate > CURRENT_DATE and os.provider_id={}'.format(sp_no))
        uobj=OperatorProfile.objects.get(uname=request.user.username)
        data={'uobj':uobj,'apcount':apcount,'atcount':atcount,'todapp':todapp,'upapp':upapp}
        return render(request,template,data)
    else:
        return HttpResponse('Sorry you should not be here.')

@login_required(login_url='/service-provider/')
def viewApp(request):
    if isProvider:
        template='SP/view-appointment.html'
        uobj=OperatorProfile.objects.get(uname=request.user.username)
        apno=request.GET.get('ap')
        ap_detail=Appointment.objects.raw('Select a.ap_id,a.bdate,a.adate,o.time_from,t.ser_name,o.time_to,o.price,a.status from Appointments_appointment a, Customer_customer_profile c, ServiceProvider_operatorservice o,Home_service t where a.user_id=c.id and a.op_sr_id=o.op_ser and o.ser_id_id=t.ser_id and a.ap_id={}'.format(apno))
        c_detail=Appointment.objects.raw('Select a.ap_id,c.usname,u.first_name,u.last_name,c.contact,u.email from Customer_customer_profile c, auth_user u,Appointments_appointment a where a.user_id = c.id and c.user_id = u.id and a.ap_id={}'.format(apno))
        sp_detail=Appointment.objects.raw('Select a.ap_id,s.uname,s.owner_name,s.contact,c.city_name,st.state_name,s.address,u.email from Appointments_appointment a,ServiceProvider_operatorprofile s,Home_city c,Home_state st,auth_user u,ServiceProvider_operatorservice os where a.op_sr_id = os.op_ser and os.provider_id=s.id and s.user_id=u.id and s.city_id = c.city_id and s.state_id = st.state_id and a.ap_id={}'.format(apno))
        data={'uobj':uobj,'ap':ap_detail,'cp':c_detail,'sp':sp_detail}  
        return render(request,template,data)

@login_required(login_url='/service-provider/')
def spLogOut(request):
    logout(request)
    return redirect('/service-provider/')

@login_required(login_url='/service-provider/')
def getBookings(request):
    if isProvider:
        template='SP/bookings.html'
        sp_no=OperatorProfile.objects.get(uname=request.user.username).id
        uobj=OperatorProfile.objects.get(uname=request.user.username)
        app=Appointment.objects.raw('select a.ap_id,c.first_name,c.last_name,cp.contact,os.time_from,a.adate from Appointments_appointment a,auth_user c,Customer_customer_profile cp,ServiceProvider_operatorservice os where cp.user_id = c.id and a.user_id=cp.id and a.op_sr_id=os.op_ser and os.provider_id={}'.format(sp_no))
        data={'uobj':uobj,'app':app}
        return render(request,template,data)

@login_required(login_url='/service-provider/')
def getAttendant(request):
    if isProvider:
        template="SP/attendants.html"
        uobj=OperatorProfile.objects.get(uname=request.user.username)
        sp_no=OperatorProfile.objects.get(uname=request.user.username).id
        att=Attendant.objects.raw('Select * from ServiceProvider_attendant where ser_pro_id={} and is_active=1'.format(sp_no))     
        data={'uobj':uobj,'att':att}
        return render(request,template,data)
@login_required(login_url='/service-provider/')
def removeAttendant(request):
    if isProvider:
        at=request.GET.get('atno')
        aobj=Attendant.objects.get(at_id=at)
        aobj.is_active=0
        aobj.save()
        return redirect('/service-provider/attendants')
@login_required(login_url='/service-provider/')
def addAttendant(request):
    if isProvider:
        at_name=request.POST.get('atname')
        gender=request.POST.get('gender')
        contact=request.POST.get('contact')
        image=request.FILES['image']
        sp_no=OperatorProfile.objects.get(uname=request.user.username).id
        At=Attendant(at_name=at_name,gender=gender,contact=contact,image=image,ser_pro_id=sp_no)
        At.save()
        return HttpResponse('Attendant Added Successfully')

@login_required(login_url='/service-provider/')
def getUpdateAttendant(request):
    if isProvider:
        at_id=request.GET.get('atno')
        template='SP/update-attendant.html'
        uobj=OperatorProfile.objects.get(uname=request.user.username)
        atobj=Attendant.objects.get(at_id=at_id)
        data={'uobj':uobj,'atobj':atobj}
        return render(request,template,data)

@login_required(login_url='/service-provider/')
def UpdateAttendant(request):
    if isProvider:
        at_id=request.POST.get('atid')
        at_name=request.POST.get('atname')
        gender=request.POST.get('gender')
        contact=request.POST.get('contact')
        if len(request.FILES) != 0:
            at=Attendant.objects.get(at_id=at_id)
            print(at)
            at.at_name=at_name
            at.gender=gender
            at.contact=contact
            at.image=request.FILES['image']
            at.save()
        else:
            at=Attendant.objects.get(at_id=at_id)
            print(at)
            at.at_name=at_name
            at.gender=gender
            at.contact=contact
            at.save()
        return redirect('/service-provider/attendants')
@login_required(login_url='/service-provider/')
def getService(request):
    if isProvider:
        template='SP/services.html'
        uobj=OperatorProfile.objects.get(uname=request.user.username)
        sp_no=OperatorProfile.objects.get(uname=request.user.username).id
        sr=OperatorService.objects.raw('select os.op_ser,a.at_name,s.ser_name,s.gender,os.time_from,os.time_to,os.price from ServiceProvider_operatorservice os, ServiceProvider_attendant a, Home_service s where s.ser_id = os.ser_id_id and os.attendant_id = a.at_id and os.is_active = 1 and os.provider_id={}'.format(sp_no))
        at_list=Attendant.objects.filter(ser_pro_id=sp_no,is_active=1)
        sl=Service.objects.filter(is_active=1)
        data={'uobj':uobj,'srobj':sr,'atlist':at_list,'sl':sl}
        return render(request,template,data)

@login_required(login_url='/service-provider/')
def addService(request):
    if isProvider:
        sp_no=OperatorProfile.objects.get(uname=request.user.username).id
        at_name=request.POST.get('attendant')
        ser=request.POST.get('service')
        tf=request.POST.get('timefrom')
        tt=request.POST.get('timeto')
        price=request.POST.get('price')
        At = OperatorService(provider_id=sp_no,attendant_id=at_name,ser_id_id=ser,time_from=tf,time_to=tt,price=price)
        At.save()
        return HttpResponse('Service Added Successfully!')
@login_required(login_url='/service-provider/')
def getUpdateService(request):
    if isProvider:
        sno=request.GET.get('sno')
        uobj=OperatorProfile.objects.get(uname=request.user.username)
        sp_no=OperatorProfile.objects.get(uname=request.user.username).id
        sr=OperatorService.objects.filter(op_ser=sno)
        at_list=Attendant.objects.filter(ser_pro_id=sp_no,is_active=1)
        sl=Service.objects.filter(is_active=1)
        template='SP/update-service.html'
        data={'uobj':uobj,'srobj':sr,'atlist':at_list,'sl':sl}
        return render(request,template,data)
@login_required(login_url='/service-provider/')
def updateService(request):
    sid=request.POST.get('op_ser')
    at_name=request.POST.get('attendant')
    ser=request.POST.get('service')
    tf=request.POST.get('timefrom')
    tt=request.POST.get('timeto')
    price=request.POST.get('price')
    At = OperatorService.objects.get(op_ser=sid)
    At.attendant_id=at_name
    At.ser_id_id=ser
    At.time_from=tf
    At.time_to=tt
    At.price=price
    At.save()
    return redirect('/service-provider/myservices')
@login_required(login_url='/service-provider/')
def removeService(request):
    if isProvider:
        sno=request.GET.get('ssno')
        sobj=OperatorService.objects.get(op_ser=sno)
        sobj.is_active=0
        sobj.save()
        return redirect('/service-provider/myservices')
@login_required(login_url='/service-provider/')
def getProfile(request):
    if isProvider:
        template='SP/myprofile.html'
        uobj=OperatorProfile.objects.get(uname=request.user.username)
        states=State.objects.all()
        sid=OperatorProfile.objects.get(uname=request.user.username).state_id
        cobj=City.objects.filter(state_id=sid)
        semail=User.objects.get(username=request.user.username).email
        data={'uobj':uobj,'states':states,'cobj':cobj,'spemail':semail}
        return render(request,template,data)
@login_required(login_url='/service-provider/')
def changePassword(request):
    if isProvider:
        uname=request.user.username
        passw=request.POST.get('password')
        encpass=django_pbkdf2_sha256.encrypt(passw)
        uobj=User.objects.get(username=uname)
        uobj.password=encpass
        uobj.save()
        return redirect('/service-provider/myprofile')

def getForgotPassword(request):
    template='SP/forgot-password.html'
    data={}
    return render(request,template,data)
def changePass(request):
    uname=request.POST.get('uname')
    passs=request.POST.get('pass')
    op=User.objects.get(username=uname)
    hashpass=django_pbkdf2_sha256.encrypt(passs)
    op.password=hashpass
    op.save()
    return redirect('/service-provider/')
def getResetPass(request):
    email=request.GET.get('email')
    template='SP/mail-sent.html'
    return render(request,template,{'email':email})
def sendLink(request):
    uname=request.POST.get('username')
    bool1=OperatorProfile.objects.filter(uname=uname).exists()
    if not bool1:
        data={
            'success':False,
        }
        return JsonResponse(data)
    else:
        uemail=User.objects.get(username=uname).email
        token=secrets.token_hex(20)
        url='127.0.0.1:8000/service-provider/reset-password?user=' + uname + '&token=' + token
        tobj=Tokens(username=uname,token=token)
        tobj.save()
        subject='Scissor Stories - Reset Password'
        message='Dear ' + uname + ',\n' + 'Here\'s the link to reset your password. Clicking on the link will let you reset your password.\n\nRESET PASSWORD LINK:\n' + url + '\n*NOTE: The above link can only be used once.\n\nBest Regards,\nYash Soni,\nOperations Executive,\nScissor Stories Ltd.'
        receiver=uemail
        send_mail(subject,message,'scissorstories1@gmail.com',[receiver],fail_silently=False)
        data={
            'success':True,
            'url':'/service-provider/forgot-password/mail?email={}'.format(uemail)
        }
        return JsonResponse(data)

def valToken(request):
    uname=request.GET.get('user')
    token=request.GET.get('token')
    try:
        test=Tokens.objects.get(token=token).username
        if test == uname:
            template='SP/reset-password.html'
            data={'username':uname}
            tobj=Tokens.objects.get(token=token)
            tobj.delete()
            return render(request,template,data)
        else:
            return HttpResponse('Something went wrong!')
    except:
        return HttpResponse('The link is expired!')
    
@login_required(login_url='/service-provider/')
def updateProfile(request):
    if isProvider:
        sobj=OperatorProfile.objects.get(uname=request.user.username)
        oname=request.POST.get('oname')
        fname=request.POST.get('fname')
        contact=request.POST.get('contact')
        #email=request.POST.get('email')
        address=request.POST.get('address')
        bio=request.POST.get('bio')
        city=City.objects.get(city_id=request.POST.get('city'))
        state=State.objects.get(state_id=request.POST.get('state'))
        try:
            image=request.FILES['image']
            sobj.firm_name=fname
            sobj.owner_name=oname
            sobj.contact=contact
            sobj.image=image
            sobj.address=address
            sobj.city=city
            sobj.state=state
            sobj.bio=bio
            sobj.save()
        except:
            sobj.firm_name=fname
            sobj.owner_name=oname
            sobj.contact=contact
            sobj.address=address
            sobj.city=city
            sobj.state=state
            sobj.bio=bio
            sobj.save()
        return redirect('/service-provider/myprofile')
