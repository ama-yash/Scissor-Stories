import secrets
from datetime import date
from django.shortcuts import render,HttpResponse,HttpResponseRedirect,redirect
from django.urls import reverse
from Home.models import City,State,Offer,Service
from django.contrib.auth.models import User
from ServiceProvider.models import OperatorProfile,Attendant,OperatorService
from .models import Customer_Profile,Tokens
from Appointments.models import Appointment,ReserveLog
from django.http import HttpResponse,JsonResponse
from ServiceProvider.models import OperatorProfile
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate,login,logout
from passlib.hash import django_pbkdf2_sha256
from django.core.mail import send_mail

@login_required(login_url='/auth')
def userLogout(request):
    logout(request)
    return redirect('/')

def isCustomer(request):
    username=request.user.username
    bool1=User.objects.filter(username=username,is_active=1).exists()
    bool2=Customer_Profile.objects.filter(usname=username).exists()
    if bool1 and bool2:
        return True
    else:
        return False
def getIndex(request):
    if request.user.is_authenticated:
        return getUserIndex(request)
    else:
        template='Customer/index.html'
        ser_list=Service.objects.raw('Select * from Home_service where is_active=1')
        att_list=Attendant.objects.raw('Select a.at_id,a.at_name,a.image,a.ser_pro_id,s.firm_name from ServiceProvider_attendant a,ServiceProvider_operatorprofile s where a.is_active=1 and a.ser_pro_id = s.id ORDER by at_id DESC LIMIT 4')
        offers=Offer.objects.filter(is_active=1)
        data={'ser_list':ser_list,'offers':offers,'at_list':att_list}
        return render(request,template,data)
def getLogin(request):
    template='Customer/login.html'
    data={}
    return render(request,template,data)
def getVerPage(request):
    template='Customer/verification.html'
    data={}
    return render(request,template,data)
def getAbout(request):
    template='Customer/about-us.html'
    data={}
    return render(request,template,data)
def getSP(request):
    template='Customer/service-providers.html'
    sobj=OperatorProfile.objects.raw('select sp.id,sp.firm_name,c.city_name,sp.image from ServiceProvider_operatorprofile sp, Home_city c where sp.city_id = c.city_id and sp.is_active =1')
    data={'sobj':sobj}
    return render(request,template,data)
def getSPView(request):
    sid=request.GET.get('id')
    ser_list=Service.objects.raw('select ser_id,ser_name,gender from Home_service where is_active=1 and ser_id IN (select ser_id_id from ServiceProvider_operatorservice where is_active=1 and provider_id ={})'.format(sid))
    sobj=OperatorProfile.objects.raw('select sp.id,sp.firm_name,sp.image,sp.address,sp.contact,c.city_name,s.state_name,sp.owner_name from ServiceProvider_operatorprofile sp,Home_city c,Home_state s where sp.city_id=c.city_id and sp.state_id=s.state_id and sp.id={}'.format(sid))
    att_list=Attendant.objects.raw('Select * from ServiceProvider_attendant where is_active=1 and ser_pro_id={}'.format(sid))  
    template='Customer/sp-detail.html'
    data={'ser':ser_list,'sobj':sobj,'at_list':att_list}
    return render(request,template,data)
def activation(request):
    user=request.GET.get('user')
    token=request.GET.get('token')
    test=Tokens.objects.get(token=token).username
    if test == user:
        uobj=User.objects.get(username=user)
        uobj.is_active=1
        uobj.save()
        tobj=Tokens.objects.get(token=token)
        tobj.delete()
        template='Customer/account-activated.html'
        return render(request,template,{})
    else:
        return HttpResponse('Something went wrong')

def getForgotPassword(request):
    template='Customer/forgot-password.html'
    data={}
    return render(request,template,data)
def getTest(request):
    template='aja.html'
    return render(request,template,{})
def getNover(request):
    template='Customer/no-verification.html'
    return render(request,template,{})
def addUser(request):
    uname=request.POST.get('username')
    email=request.POST.get('email')
    password=request.POST.get('pass')
    test=User.objects.filter(username=uname).exists()
    if test:
        data={
            'success':False,
            'user':False,
        }
        return JsonResponse(data)
    else:
        hashpass=django_pbkdf2_sha256.encrypt(password,rounds=12000,salt_size=12)
        uobj=User(username=uname,email=email,password=hashpass)
        uobj.is_active=0
        uobj.save()
        token=secrets.token_hex(20)
        tobj=Tokens(username=uname,token=token)
        tobj.save()
        cobj=Customer_Profile(usname=uname,user_id=uobj.id)
        cobj.save()
        subject='Scissor Stories - Account Activation'
        url='127.0.0.1:8000/activation?user=' + uname + '&token=' + token
        message='Dear ' + uname + ',\n' + 'Welcome to our Community. We are glad to have you. Please click on the below link to activate your account.\n\nACTIVATION LINK:\n' + url + '\n*NOTE: The above link can only be used once.\n\nBest Regards,\nYash Soni,\nOperations Executive,\nScissor Stories Ltd.'
        receiver=email
        send_mail(subject,message,'scissorstories1@gmail.com',[receiver],fail_silently=False)
        data={
            'success':True,
            'url':'/auth/ver'
        }
        return JsonResponse(data)

def validateLogin(request):
    uname=request.POST.get('username')
    passw=request.POST.get('password')
    bool2=User.objects.filter(username=uname,is_active=1).exists()
    cbool=Customer_Profile.objects.filter(usname=uname).exists()
    bool3=User.objects.filter(username=uname,is_active=0).exists()     
    if bool2 and cbool:
        user=authenticate(username=uname,password=passw)
        if user is not None:
            login(request,user)
            data={
                'success':True,
                'url':'/myaccount/'
            }
            return JsonResponse(data)
        else:
            data={
                'success':False,
                'user':True,
                'passw':False
            }
            return JsonResponse(data)
    elif bool3 and cbool:
        user=authenticate(username=uname,password=passw)
        if user is not None:
            data={
                'success':True,
                'url':'/auth/ver-fail'
            }
            return JsonResponse(data)
        else:
            data={
                'success':False,
                'user':True,
                'passw':False
            }
            return JsonResponse(data)
    else:
        data={
            'success':False,
            'user':False,
            'passw':True
        }
        return JsonResponse(data)
def sendForgotPasswordLink(request):
    uname=request.POST.get('username')
    bool1=User.objects.filter(username=uname).exists()
    if not bool1:
        data={
            'success':False,
        }
        return JsonResponse(data)
    else:
        uemail=User.objects.get(username=uname).email
        token=secrets.token_hex(20)
        url='127.0.0.1:8000/auth/reset-password?user=' + uname + '&token=' + token
        tobj=Tokens(username=uname,token=token)
        tobj.save()
        subject='Scissor Stories - Reset Password'
        message='Dear ' + uname + ',\n' + 'Here\'s the link to reset your password. Clicking on the link will let you reset your password.\n\nRESET PASSWORD LINK:\n' + url + '\n*NOTE: The above link can only be used once.\n\nBest Regards,\nYash Soni,\nOperations Executive,\nScissor Stories Ltd.'
        receiver=uemail
        send_mail(subject,message,'scissorstories1@gmail.com',[receiver],fail_silently=False)
        data={
            'success':True,
            'url':'/auth/reset-password-link-sent?email={}'.format(uemail)
        }
        return JsonResponse(data)
def getLinkSent(request):
    email=request.GET.get('email')
    data={
        'email':email
    }
    template='Customer/for-pass-link.html'
    return render(request,template,data)
def getResetPass(request):
    uname=request.GET.get('user')
    token=request.GET.get('token')
    try:
        test=Tokens.objects.get(token=token).username
        if test == uname:
            template='Customer/reset-password.html'
            data={'username':uname}
            tobj=Tokens.objects.get(token=token)
            tobj.delete()
            return render(request,template,data)
        else:
            return HttpResponse('Something went wrong!')
    except:
        return HttpResponse('The link is expired!')

def resetPassword(request):
    try:
        uname=request.POST.get('uname')
        passw=request.POST.get('pass1')
        hashpass=django_pbkdf2_sha256.encrypt(passw)
        uobj=User.objects.get(username=uname)
        uobj.password=hashpass
        uobj.save()
        return redirect('/auth')
    except:
        return HttpResponse('Sorry, Something went wrong.')
@login_required(login_url='/auth')
def getUserIndex(request):
    if isCustomer:
        template='Customer/user-index.html'
        ser_list=Service.objects.raw('Select * from Home_service where is_active=1')
        att_list=Attendant.objects.raw('Select a.at_id,a.at_name,a.image,a.ser_pro_id,s.firm_name from ServiceProvider_attendant a,ServiceProvider_operatorprofile s where a.is_active=1 and a.ser_pro_id = s.id ORDER by at_id DESC LIMIT 4')
        uid=Customer_Profile.objects.get(user_id=request.user.id).id
        ap_list=Appointment.objects.raw('Select a.ap_id,sp.firm_name,att.at_name,s.ser_name,a.bdate,a.adate,os.time_from,os.time_to,os.price,a.status from Appointments_appointment a,ServiceProvider_attendant att,ServiceProvider_operatorservice os, Home_service s,ServiceProvider_operatorprofile sp WHERE a.op_sr_id = os.op_ser and os.attendant_id = att.at_id and os.ser_id_id = s.ser_id and os.provider_id = sp.id and a.user_id={}'.format(uid))
        offers=Offer.objects.filter(is_active=1)
        data={'ser_list':ser_list,'offers':offers,'at_list':att_list,'ap_list':ap_list}
        return render(request,template,data)
@login_required(login_url='/auth')
def getUserProfile(request):
    template='Customer/profile.html'
    uname=request.user.username
    cus_profile=Customer_Profile.objects.raw('Select a.id,a.username,a.first_name,a.last_name,a.email,a.last_login,a.date_joined,c.image,c.contact,c.gender,c.city_id,c.state_id,c.address,ct.city_name,st.state_name from auth_user a,Customer_customer_profile c,Home_city ct,Home_state st where a.id=c.user_id and c.city_id = ct.city_id and c.state_id = st.state_id and a.username="{}"'.format(uname))
    cities=City.objects.filter(is_active=1)
    states=State.objects.filter(is_active=1)
    data={'customers':cus_profile,'cities':cities,'states':states}
    return render(request,template,data)

@login_required(login_url='/auth')
def updateProfile(request):
    try:
        uname=request.POST.get('username')
        fname=request.POST.get('fname')
        lname=request.POST.get('lname')
        city=request.POST.get('city')
        state=request.POST.get('state')
        contact=request.POST.get('contact')
        gender=request.POST.get('gender')
        dob=request.POST.get('dob')
        address=request.POST.get('address')
        image=request.FILES['image']
        uobj=User.objects.get(username=uname)
        uobj.first_name=fname
        uobj.last_name=lname
        uobj.save()
        cobj=Customer_Profile.objects.get(usname=uname)
        cobj.contact=contact
        cobj.gender=gender
        cobj.address=address
        cobj.city_id=city
        cobj.state_id=state
        cobj.image=image
        cobj.save()
        return redirect('/myaccount/profile')
    except:
        uname=request.POST.get('username')
        fname=request.POST.get('fname')
        lname=request.POST.get('lname')
        city=request.POST.get('city')
        state=request.POST.get('state')
        contact=request.POST.get('contact')
        gender=request.POST.get('gender')
        dob=request.POST.get('dob')
        address=request.POST.get('address')
        uobj=User.objects.get(username=uname)
        uobj.first_name=fname
        uobj.last_name=lname
        uobj.save()
        cobj=Customer_Profile.objects.get(usname=uname)
        cobj.contact=contact
        cobj.gender=gender
        cobj.address=address
        cobj.city_id=city
        cobj.state_id=state
        cobj.save()
        return redirect('/myaccount/profile')
def sendServices(request):
    yyyy=request.POST.get('yyyy')
    dd=request.POST.get('dd')
    mm=request.POST.get('mm')
    mm=int(mm)
    mm=mm+1
    mm=str(mm)
    if mm == '11' or mm == '10' or mm =='12':
        pass
    else:
        mm = '0'+ mm
    if dd == '1' or dd == '2' or dd == '3' or dd == '4' or dd == '5' or dd == '6' or dd == '7' or dd == '8' or dd == '9':
        dd = '0' + dd
    date = ''
    date = date + yyyy + '-' + mm + '-' + dd
    but=request.POST.get('but')
    sobjs=OperatorService.objects.filter(is_active=1,provider_id=but)
    lista=[]
    for s in sobjs:
        bool1=ReserveLog.objects.filter(rdate=date,os_id=s.op_ser).exists()
        if not bool1:
            lista.append(s.op_ser)
    listb=[]
    for l in lista:
        obj=OperatorService.objects.raw('select sp.op_ser,s.ser_name,sp.time_from,sp.time_to,a.at_name,s.gender,sp.price from ServiceProvider_operatorservice sp, Home_service s, ServiceProvider_attendant a where sp.attendant_id = a.at_id and sp.ser_id_id = s.ser_id and sp.is_active = 1 and sp.op_ser={}'.format(l))        
        listb.append(obj)
    idlist=[]
    serlist=[]
    fromlist=[]
    tolist=[]
    atlist=[]
    genlist=[]
    pricelist=[]
    for l in listb:
        for o in l:
            idlist.append(o.op_ser)
            serlist.append(o.ser_name)
            fromlist.append(o.time_from)
            tolist.append(o.time_to)
            atlist.append(o.at_name)
            genlist.append(o.gender)
            pricelist.append(o.price)
    data={'success':True,'idlist':idlist,'serlist':serlist,'fromlist':fromlist,'tolist':tolist,'atlist':atlist,'genlist':genlist,'pricelist':pricelist,'length':len(idlist),'pro':but,'date':date}
    return JsonResponse(data)
@login_required(login_url='/auth')
def getConfirmAppointment(request):
    ser_id=request.GET.get('id')
    pro=request.GET.get('pro')
    date1=request.GET.get('date')
    tod=date.today()
    tod=tod.strftime("%Y-%m-%d")
    uid=Customer_Profile.objects.get(user_id=request.user.id).id
    ap=Appointment(bdate=tod,user_id=uid,op_sr_id=ser_id,status=2,adate=date1)
    res=ReserveLog(os_id=ser_id,rdate=date1)
    ap.save()
    apid=ap.ap_id
    res.save()
    aobj=Appointment.objects.raw('Select a.ap_id,sp.firm_name,att.at_name,s.ser_name,a.bdate,a.adate,os.time_from,os.time_to,os.price,a.status from Appointments_appointment a,ServiceProvider_attendant att,ServiceProvider_operatorservice os, Home_service s,ServiceProvider_operatorprofile sp WHERE a.op_sr_id = os.op_ser and os.attendant_id = att.at_id and os.ser_id_id = s.ser_id and os.provider_id = sp.id and a.ap_id={}'.format(apid))
    off=Offer.objects.filter(is_active=1)
    template='Customer/confirm-appointment.html'
    data={'apdetails':aobj,'offers':off}
    return render(request,template,data)

@login_required(login_url='/auth')
def viewAppointment(request):
    if isCustomer:
        template='Customer/appointment-view.html'
        aid=request.GET.get('id')
        ap_list=Appointment.objects.raw('Select a.ap_id,sp.firm_name,att.at_name,s.ser_name,a.bdate,a.adate,os.time_from,os.time_to,os.price,a.status from Appointments_appointment a,ServiceProvider_attendant att,ServiceProvider_operatorservice os, Home_service s,ServiceProvider_operatorprofile sp WHERE a.op_sr_id = os.op_ser and os.attendant_id = att.at_id and os.ser_id_id = s.ser_id and os.provider_id = sp.id and a.ap_id={}'.format(aid))
        data={'ap_list':ap_list}
        return render(request,template,data)

def getAppointment(request):
    if isCustomer:
        template='Customer/appointments.html'
        aid=Customer_Profile.objects.get(user_id=request.user.id).id
        ap_list=Appointment.objects.raw('Select a.ap_id,sp.firm_name,att.at_name,s.ser_name,a.bdate,a.adate,os.time_from,os.time_to,os.price,a.status from Appointments_appointment a,ServiceProvider_attendant att,ServiceProvider_operatorservice os, Home_service s,ServiceProvider_operatorprofile sp WHERE a.op_sr_id = os.op_ser and os.attendant_id = att.at_id and os.ser_id_id = s.ser_id and os.provider_id = sp.id and a.user_id={}'.format(aid))
        data={'ap_list':ap_list}
        return render(request,template,data)

@login_required(login_url='/auth')
def getChangePass(request):
    template='Customer/change-password.html'
    data={}
    return render(request,template,data)
def getPayment(request):
    template='Payment/index.html'
    return render(request,template,{})

def getAck(request):
    template='Customer/app-ack.html'
    return render(request,template,{})

def getDec(request):
    template='Customer/account-deactivate.html'
    return render(request,template,{})