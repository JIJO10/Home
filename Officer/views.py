from django.shortcuts import render,redirect
from Subadmin.models import Officer
from User.models import Complaint
from User.models import Feedback
from guest.models import *

# Create your views here.

def officerhome(request):
    if 'oid' in request.session:
        of=Officer.objects.get(id=request.session['oid'])
        return render(request,"Officer/Officerhome.html",{'OF':of})
    else:
        return redirect("webguest:Login")


def officerprof(request):
    if 'oid' in request.session:
        prof=Officer.objects.get(id=request.session['oid'])
        return render(request,"Officer/Officerprofile.html",{'PF':prof})
    else:
        return redirect("webguest:Login")

def edprof(request,eid):
    selofr=Officer.objects.get(id=eid)
    if request.method=="POST":
        selofr.officer_name=request.POST.get('txt_name')
        selofr.officer_contact=request.POST.get('cnct')
        selofr.officer_email=request.POST.get('mail')
        selofr.officer_address=request.POST.get('textaddress')
        selofr.save()
        return redirect('officer:officerprofile')
    else:
        return render(request,"Officer/Editprofile.html",{'EP':selofr})


def chngpwd(request,cid):
    change=Officer.objects.get(id=cid)
    if request.method=="POST":
        pwd=change.officer_pwd
        current=request.POST.get('txt_pwd')
        if pwd == current:
            change=Officer.objects.get(id=cid)
            new=request.POST.get('txt_npwd')
            change.officer_pwd=new
            change.save()
            return redirect('webguest:Login')
        else:
            error="Incorrect Password!!"
            return render(request,"Officer/Changepassword.html",{'ER':error})
    else:
        return render(request,"Officer/Changepassword.html")

def ofcrcmplnt(request):
    if 'oid' in request.session:
        com=Complaint.objects.all()
        of=Officer.objects.get(id=request.session['oid'])
        ofr=Complaint.objects.filter(officer_id=of)
        if request.method=="POST":
            Complaint.objects.create(complaint_title=request.POST.get('txt_cmplnttyp'),complaint_content=request.POST.get('txt_cntnt'),
                                 officer_id=of)
            return render(request,"Officer/OfficerComplaints.html",{'COM':com,'OFR':ofr})
        else:
            return render(request,"Officer/OfficerComplaints.html",{'COM':com,'OFR':ofr})
    else:
        return redirect("webguest:Login")

def delcom(request,comid):
    Complaint.objects.get(id=comid).delete()
    return redirect("officer:officercomplaint")

def ofcrfeedbck(request):
    if 'oid' in request.session:
        feed=Feedback.objects.all()
        ofcr=Officer.objects.get(id=request.session['oid'])
        ofr=Feedback.objects.filter(officer_id=ofcr)
        if request.method=="POST":
            Feedback.objects.create(feedback_content=request.POST.get('txt_feedback'),officer_id=ofcr)
            return render(request,"Officer/Officerfeedback.html",{'FEED':feed,'OFR':ofr})
        else:
            return render(request,"Officer/Officerfeedback.html",{'FEED':feed,'OFR':ofr})
    else:
        return redirect("webguest:Login")


def delfeed(request,fid):
    Feedback.objects.get(id=fid).delete()
    return redirect("officer:officerfeedback")

def ownrver(request):
    if 'oid' in request.session:
        ownr=Owner.objects.filter(owner_vsts=0)
        return render(request,"Officer/OwnerVerification.html",{'OWNR':ownr})
    else:
        return redirect("webguest:Login")


def ow_accpt(request,oaid):
    accept=Owner.objects.get(id=oaid)
    accept.owner_vsts=1
    accept.save()
    return redirect('officer:ownerverfication')


def ow_rjct(request,orid):
    reject=Owner.objects.get(id=orid)
    reject.owner_vsts=2
    reject.save()
    return redirect('officer:ownerverfication')


def ownraccpt(request):
    if 'oid' in request.session:
        ownr=Owner.objects.filter(owner_vsts=1)
        return render(request,"Officer/OwnerAccepted.html",{'OWNR':ownr})
    else:
        return redirect("webguest:Login")


def ownrrjct(request):
    if 'oid' in request.session:
        ownr=Owner.objects.filter(owner_vsts=2)
        return render(request,"Officer/OwnerRejected.html",{'OWNR':ownr})
    else:
        return redirect("webguest:Login")


def usrver(request):
    if 'oid' in request.session:
        usr=User.objects.filter(user_vsts=0)
        return render(request,"Officer/UserVerification.html",{'USR':usr})
    else:
        return redirect("webguest:Login")


def usr_accpt(request,uaid):
    accept=User.objects.get(id=uaid)
    accept.user_vsts=1
    accept.save()
    return redirect('officer:userverification')


def usr_rjct(request,urid):
    reject=User.objects.get(id=urid)
    reject.user_vsts=2
    reject.save()
    return redirect('officer:userverification')

def usraccpt(request):
    if 'oid' in request.session:
        usr=User.objects.filter(user_vsts=1)
        return render(request,"Officer/UserAccepted.html",{'USR':usr})
    else:
        return redirect("webguest:Login")


def usrrjct(request):
    if 'oid' in request.session:
        usr=User.objects.filter(user_vsts=2)
        return render(request,"Officer/UserRejected.html",{'USR':usr})
    else:
        return redirect("webguest:Login")

















        


