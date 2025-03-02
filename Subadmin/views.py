from django.shortcuts import render,redirect
from Subadmin.models import *
from Admin.models import *
from guest.models import *


# Create your views here.

def subhom(request):
    if 'sid' in request.session:
        sa=Subadmin.objects.get(id=request.session['sid'])
        return render(request,"Subadmin/subadminhome.html",{'SA':sa})
    else:
        return redirect("webguest:Login")


def profile(request):
    if 'sid' in request.session:
        prof=Subadmin.objects.get(id=request.session['sid'])
        return render(request,"Subadmin/Myprofile.html",{'PF':prof})
    else:
        return redirect("webguest:Login")



def edprof(request,eid):
    selusr=Subadmin.objects.get(id=eid)
    if request.method=="POST":
        selusr.subadmin_name=request.POST.get('txt_name')
        selusr.subadmin_contact=request.POST.get('cnct')
        selusr.subadmin_email=request.POST.get('mail')
        selusr.subadmin_address=request.POST.get('textaddress')
        selusr.save()
        return redirect('subadmin:myprofile')
    else:
        return render(request,"Subadmin/Editprofile.html",{'EP':selusr})


def chngpwd(request,cid):
    change=Subadmin.objects.get(id=cid)
    if request.method=="POST":
        pwd=change.subadmin_pwd
        current=request.POST.get('txt_pwd')
        if pwd == current:
            change=Subadmin.objects.get(id=cid)
            new=request.POST.get('txt_npwd')
            change.subadmin_pwd=new
            change.save()
            return redirect('webguest:Login')
        else:
            error="Incorrect Password!!"
            return render(request,"Subadmin/Changepassword.html",{'ER':error})
    else:
        return render(request,"Subadmin/Changepassword.html")


def officer(request):
    if 'sid' in request.session:
        con=Country.objects.all()
        sa=Subadmin.objects.get(id=request.session['sid'])
        if request.method=="POST" and request.FILES:
            stid=request.POST.get('sel_sta')
            st=State.objects.get(id=stid)
            Officer.objects.create(officer_name=request.POST.get('txtname'),officer_contact=request.POST.get('cnct'),
                               officer_email=request.POST.get('mail'),officer_gender=request.POST.get('gender'),
                               officer_address=request.POST.get('textaddress'),officer_photo=request.FILES.get('file_photo'),
                               officer_proof=request.FILES.get('file_proof'),officer_pwd=request.POST.get('txt_pwd'),
                               officer_state=st,subadmin_id=sa)
            return render(request,"Subadmin/Officer.html",{'con':con,'SA':sa})
        else:
            return render(request,"Subadmin/Officer.html",{'con':con,'SA':sa})
    else:
        return redirect("webguest:Login")


def ownrver(request):
    if 'sid' in request.session:
        ownr=Owner.objects.filter(owner_vsts=1)
        return render(request,"Subadmin/OwnerVerification.html",{'OWNR':ownr})
    else:
        return redirect("webguest:Login")


def ow_accpt(request,oaid):
    accept=Owner.objects.get(id=oaid)
    accept.owner_vsts=3
    accept.save()
    return redirect('subadmin:owneraccepted')


def ow_rjct(request,orid):
    reject=Owner.objects.get(id=orid)
    reject.owner_vsts=4
    reject.save()
    return redirect('subadmin:ownerrejected')

def ownraccpt(request):
    if 'sid' in request.session:
        ownr=Owner.objects.filter(owner_vsts=3)
        return render(request,"Subadmin/OwnerAccepted.html",{'OWNR':ownr})
    else:
        return redirect("webguest:Login")


def ownrrjct(request):
    if 'sid' in request.session:
        ownr=Owner.objects.filter(owner_vsts=4)
        return render(request,"Subadmin/OwnerRejected.html",{'OWNR':ownr})
    else:
        return redirect("webguest:Login")


def usrver(request):
    if 'sid' in request.session:
        usr=User.objects.filter(user_vsts=1)
        return render(request,"Subadmin/UserVerification.html",{'USR':usr})
    else:
        return redirect("webguest:Login")


def usr_accpt(request,uaid):
    accept=User.objects.get(id=uaid)
    accept.user_vsts=3
    accept.save()
    return redirect('subadmin:useraccepted')


def usr_rjct(request,urid):
    reject=User.objects.get(id=urid)
    reject.user_vsts=4
    reject.save()
    return redirect('subadmin:userrejected')

def usraccpt(request):
    if 'sid' in request.session:
        usr=User.objects.filter(user_vsts=3)
        return render(request,"Subadmin/UserAccepted.html",{'USR':usr})
    else:
        return redirect("webguest:Login")


def usrrjct(request):
    if 'sid' in request.session:
        usr=User.objects.filter(user_vsts=4)
        return render(request,"Subadmin/UserRejected.html",{'USR':usr})
    else:
        return redirect("webguest:Login")






        


