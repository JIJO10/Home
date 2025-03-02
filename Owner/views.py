from django.shortcuts import render,redirect
from Owner.models import *
from guest.models import Owner
from Admin.models import RentType
from Subadmin.models import Officer
from User.models import Complaint
from User.models import Feedback
from User.models import Booking

# Create your views here.


def ownerhome(request):
    if 'oid' in request.session:
        on=Owner.objects.get(id=request.session['oid'])
        return render(request,"Owner/Ownerhome.html",{'ON':on})
    else:
        return redirect("webguest:Login")


def ownerprof(request):
    if 'oid' in request.session:
        onr=Owner.objects.get(id=request.session['oid'])
        return render(request,"Owner/Ownerprofile.html",{'PF':onr})
    else:
        return redirect("webguest:Login")

def edprof(request,eid):
    selonr=Owner.objects.get(id=eid)
    if request.method=="POST":
        selonr.owner_name=request.POST.get('txt_name')
        selonr.owner_contact=request.POST.get('cnct')
        selonr.owner_email=request.POST.get('mail')
        selonr.owner_address=request.POST.get('textaddress')
        selonr.save()
        return redirect('owner:ownerprofile')
    else:
        return render(request,"owner/Editprofile.html",{'EP':selonr})

def chngpwd(request,cid):
    change=Owner.objects.get(id=cid)
    if request.method=="POST":
        pwd=change.owner_pwd
        current=request.POST.get('txt_pwd')
        if pwd == current:
            change=Owner.objects.get(id=cid)
            new=request.POST.get('txt_npwd')
            change.owner_pwd=new
            change.save()
            return redirect('webguest:Login')
        else:
            error="Incorrect Password!!"
            return render(request,"Owner/Changepassword.html",{'ER':error})
    else:
        return render(request,"Owner/Changepassword.html")


def addrnt(request):
    if 'oid' in request.session:
        rnttyp=RentType.objects.all()
        on=Owner.objects.get(id=request.session['oid'])
        rnt=Rent.objects.filter(owner_id=on)
        if request.method=="POST":
            rntid=request.POST.get('sel_rent')
            rent=RentType.objects.get(id=rntid)
            Rent.objects.create(rent_name=request.POST.get('txtname'),rent_image=request.FILES.get('file_img'),
                               rent_details=request.POST.get('dtils'),rent_amount=request.POST.get('amnt'),
                               owner_id=on,renttype_id=rent)
            return render(request,"Owner/AddRent.html",{'RENTT':rnttyp,'RNT':rnt})
        else:
            return render(request,"Owner/AddRent.html",{'RENTT':rnttyp,'RNT':rnt})
    else:
        return redirect("webguest:Login")

def delrent(request,rntid):
    Rent.objects.get(id=rntid).delete()
    return redirect("owner:addrent")

def addgalry(request,glid):
    rent=Rent.objects.get(id=glid)
    gl=Gallery.objects.filter(rent_id=rent)
    if request.method=="POST":
        Gallery.objects.create(gallery_image=request.FILES.get('file_img'),rent_id=rent)
        return redirect("owner:addrent")
       
    else:
        return render(request,"Owner/Gallery.html",{'GL':gl})

def delgal(request,galid):
    Gallery.objects.get(id=galid).delete()
    return redirect("owner:addrent")

def ownrcmplnt(request):
    if 'oid' in request.session:
        com=Complaint.objects.all()
        on=Owner.objects.get(id=request.session['oid'])
        owr=Complaint.objects.filter(owner_id=on)
        if request.method=="POST":
            Complaint.objects.create(complaint_title=request.POST.get('txt_cmplnttyp'),complaint_content=request.POST.get('txt_cntnt'),
                                 owner_id=on)
            return render(request,"Owner/OwnerComplaint.html",{'COM':com,'OWR':owr})
        else:
            return render(request,"Owner/OwnerComplaint.html",{'COM':com,'OWR':owr})
    else:
        return redirect("webguest:Login")

def delcom(request,comid):
    Complaint.objects.get(id=comid).delete()
    return redirect("user:usercomplaint")


def ownrfeedbck(request):
    if 'oid' in request.session:
        feed=Feedback.objects.all()
        ownr=Owner.objects.get(id=request.session['oid'])
        owr=Feedback.objects.filter(owner_id=ownr)
        if request.method=="POST":
            Feedback.objects.create(feedback_content=request.POST.get('txt_feedback'),owner_id=ownr)
            return render(request,"Owner/Ownerfeedback.html",{'FEED':feed,'OWR':owr})
        else:
            return render(request,"Owner/Ownerfeedback.html",{'FEED':feed,'OWR':owr})
    else:
        return redirect("webguest:Login")

def delfeed(request,fid):
    Feedback.objects.get(id=fid).delete()
    return redirect("owner:ownerfeedback")


def myrntbook(request):
    if 'oid' in request.session:
        
        ownr=Owner.objects.get(id=request.session['oid'])
        book=Booking.objects.filter(rent_id__owner_id=ownr)
        return render(request,"Owner/MyRentBookings.html",{'BOOK':book})
    else:
        return redirect("webguest:Login")

def acpt(request,aid):
    accept=Booking.objects.get(id=aid)
    accept.booking_status=1
    accept.save()
    return redirect('owner:myrentbookings')

def rjct(request,rid):
    accept=Booking.objects.get(id=rid)
    accept.booking_status=2
    accept.save()
    return redirect('owner:myrentbookings')







