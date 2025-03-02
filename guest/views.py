from django.shortcuts import render,redirect
from guest.models import *
from Admin.models import *
import random
from django.conf import settings
from django.core.mail import send_mail
from Subadmin.models import Officer




# Create your views here.

def log(request):
    if request.method=="POST":
        Email=request.POST.get('txt_mail')
        Password=request.POST.get('txt_pwd')
        sublog=Subadmin.objects.filter(subadmin_email=Email,subadmin_pwd=Password).count()
        offlog=Officer.objects.filter(officer_email=Email,officer_pwd=Password).count()
        ownrlog=Owner.objects.filter(owner_email=Email,owner_pwd=Password,owner_vsts=3).count()
        usrlog=User.objects.filter(user_email=Email,user_pwd=Password,user_vsts=3).count()
        adlog=Admin.objects.filter(admin_email=Email,admin_pwd=Password).count()

        if sublog > 0:
            sadmin=Subadmin.objects.get(subadmin_email=Email,subadmin_pwd=Password)
            request.session['sid']=sadmin.id
            request.session['sname']=sadmin.subadmin_name
            con=Country.objects.get(id=sadmin.subadmin_country_id)
            request.session['cid']=con.id
            return redirect('subadmin:subhome')
        elif offlog > 0:
            officer=Officer.objects.get(officer_email=Email,officer_pwd=Password)
            request.session['oid']=officer.id
            request.session['oname']=officer.officer_name
            request.session['stid']=officer.officer_state.id
            return redirect('officer:officerhome')
        elif ownrlog > 0:
            owner=Owner.objects.get(owner_email=Email,owner_pwd=Password,owner_vsts=3)
            request.session['oid']=owner.id
            request.session['oname']=owner.owner_name
            return redirect('owner:ownerhome')
        elif usrlog > 0:
            user=User.objects.get(user_email=Email,user_pwd=Password,user_vsts=3)
            request.session['uid']=user.id
            request.session['uname']=user.user_name
            return redirect('user:userhome')
        elif adlog > 0:
            admin=Admin.objects.get(admin_email=Email,admin_pwd=Password)
            request.session['aid']=admin.id
            request.session['aname']=admin.admin_name
            return redirect('webadmin:adminhome')
        else:
            error="Invalid Credentials!!"
            return render(request,"guest/Login.html",{'ER':error})
    else:
        return render(request,"guest/Login.html")
        

def usr(request):
    con=Country.objects.all()
    if  request.method=="POST" and request.FILES:
        plcid=request.POST.get('sel_plc')
        plc=Place.objects.get(id=plcid)
        User.objects.create(user_name=request.POST.get('txtname'),user_contact=request.POST.get('contact'),
                               user_email=request.POST.get('mail'),user_gender=request.POST.get('gender'),
                               user_address=request.POST.get('textaddress'),user_zipcode=request.POST.get('zcode'),
                               user_photo=request.FILES.get('file_photo'),user_proof=request.FILES.get('file_proof'),
                               user_pwd=request.POST.get('pwd'),user_place=plc,)
        return render(request,"guest/NewUser.html",{'CON':con})
    else:
        return render(request,"guest/NewUser.html",{'CON':con})


def ownr(request):
    con=Country.objects.all()
    if  request.method=="POST" and request.FILES:
        plcid=request.POST.get('sel_plc')
        plc=Place.objects.get(id=plcid)
        Owner.objects.create(owner_name=request.POST.get('txtname'),owner_contact=request.POST.get('contact'),
                               owner_email=request.POST.get('mail'),owner_gender=request.POST.get('gender'),
                               owner_address=request.POST.get('textaddress'),owner_zipcode=request.POST.get('zcode'),
                               owner_photo=request.FILES.get('file_photo'),owner_proof=request.FILES.get('file_proof'),
                               owner_pwd=request.POST.get('pwd'),owner_place=plc,)
        return render(request,"guest/NewOwner.html",{'CON':con})
    else:
        return render(request,"guest/NewOwner.html",{'CON':con})







def AjaxPlace(request):
    dis=District.objects.get(id=request.GET.get('CNTRY'))
    plc=Place.objects.filter(district=dis)
    return render(request,"guest/AjaxPlace.html",{'plc':plc})


def home(request):
    return render(request,"guest/Home.html")



def ForgetPassword(request): 
    if request.method=="POST":
        otp=random.randint(10000, 999999)
        request.session["otp"]=otp
        request.session["txtemail"]=request.POST.get('txtemail')
        send_mail(
            'Respected Sir/Madam ',#subject
            "\rYour OTP for Reset Password Is"+str(otp),#body
            settings.EMAIL_HOST_USER,
            [request.POST.get('txtemail')],
        )
        return redirect("webguest:verification")
    else:
        return render(request,"guest/ForgotPassword.html")

def OtpVerification(request):
    if request.method=="POST":
        otp=int(request.session["otp"])
        if int(request.POST.get('txtotp'))==otp:
            return redirect("webguest:create")
    return render(request,"guest/Otpverification.html")

def CreateNewPass(request):
    if request.method=="POST":
        if request.POST.get('txtpassword2')==request.POST.get('txtpassword3'):
            usercount=User.objects.filter(user_email=request.session["txtemail"]).count()
            ownercount=Owner.objects.filter(owner_email=request.session["txtemail"]).count()
            Subadmincount=Subadmin.objects.filter(subadmin_email=request.session["txtemail"]).count()
            hos=Officer.objects.filter(officer_email=request.session["txtemail"]).count()
            if usercount>0:
                user=User.objects.get(user_email=request.session["txtemail"])
                user.user_pwd=request.POST.get('txtpassword2')
                user.save()
                return redirect("webguest:Login")

            elif ownercount>0:
                doc=Owner.objects.get(owner_email=request.session["txtemail"])
                doc.owner_pwd=request.POST.get('txtpassword2')
                doc.save()
                return redirect("webguest:Login")

            elif Subadmincount>0:
                con=Subadmin.objects.get(subadmin_email=request.session["txtemail"])
                con.subadmin_pwd=request.POST.get('txtpassword2')
                con.save()
                return redirect("webguest:Login")

            else:
                hos=Officer.objects.get( officer_email=request.session["txtemail"])
                hos.officer_pwd=request.POST.get('txtpassword2')
                hos.save()
                return redirect("webguest:Login")
    else:       
        return render(request,"guest/Createpassword.html")
