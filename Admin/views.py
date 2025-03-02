from django.shortcuts import render,redirect
from Admin.models import *
from User.models import *

# Create your views here.

def country(request):
    if 'aid' in request.session:
        if request.method=="POST":
            Country.objects.create(country_name=request.POST.get('txt_country'))
            con=Country.objects.all()
            return render(request,"Admin/Country.html",{'CON':con})
        else:
            con=Country.objects.all()
            return render(request,"Admin/Country.html",{'CON':con})
    else:
        return redirect("webguest:Login")


def del_con(request,cid):
    Country.objects.get(id=cid).delete()
    return redirect('webadmin:Country')

def up_con(request,eid):
    selcon=Country.objects.get(id=eid)
    if request.method=="POST":
        selcon.country_name=request.POST.get('txt_country')
        selcon.save()
        return redirect('webadmin:Country')
    else:
         return render(request,"Admin/EditCountry.html",{'CN':selcon})


def sta(request):
    if 'aid' in request.session:
        cont=Country.objects.all()
        st=State.objects.all()
        if request.method=="POST":
            conid=request.POST.get('sel_con')
            con=Country.objects.get(id=conid)
            State.objects.create(state_name=request.POST.get('txt_sta'),country=con)
            return render(request,"Admin/State.html",{'CN':cont,'st':st})
        else:
            return render(request,"Admin/State.html",{'CN':cont,'st':st})
    else:
        return redirect("webguest:Login")

def Del_sta(request,sid):
    State.objects.get(id=sid).delete()
    return redirect('webadmin:state')


def dis(request):
    if 'aid' in request.session:
        con=Country.objects.all()
        di=District.objects.all()
        if request.method=="POST":
            stid=request.POST.get('sel_sta')
            st=State.objects.get(id=stid)
            District.objects.create(district_name=request.POST.get('txt_dis'),state=st)
            return render(request,"Admin/District.html",{'con':con,'DIS':di})
        else:
            return render(request,"Admin/District.html",{'con':con,'DIS':di})
    else:
        return redirect("webguest:Login")

def Del_dis(request,disid):
    District.objects.get(id=disid).delete()
    return redirect('webadmin:district')

def plc(request):
    if 'aid' in request.session:
        con=Country.objects.all()
        pl=Place.objects.all()
        if request.method=="POST":
            disid=request.POST.get('sel_dis')
            dis=District.objects.get(id=disid)
            Place.objects.create(place_name=request.POST.get('txt_plc'),district=dis)
            return render(request,"Admin/Place.html",{'con':con,'PL':pl})
        else:
            return render(request,"Admin/Place.html",{'con':con,'PL':pl})
    else:
        return redirect("webguest:Login")

def Del_pl(request,pid):
    Place.objects.get(id=pid).delete()
    return redirect('webadmin:place')






def renttype(request):
    if 'aid' in request.session:
        rnt=RentType.objects.all()
        if request.method=="POST":
            RentType.objects.create(renttype_name=request.POST.get('rent_type'))
            return render(request,"Admin/Renttype.html",{'RT':rnt})
        else:
            return render(request,"Admin/Renttype.html",{'RT':rnt})
    else:
        return redirect("webguest:Login")

def del_rnt(request,rid):
    RentType.objects.get(id=rid).delete()
    return redirect('webadmin:renttype')

def AjaxState(request):
    con=Country.objects.get(id=request.GET.get('CNTRY'))
    state=State.objects.filter(country=con)
    return render(request,"Admin/AjaxState.html",{'st':state})

def AjaxDistrict(request):
    sta=State.objects.get(id=request.GET.get('CNTRY'))
    dis=District.objects.filter(state=sta)
    return render(request,"Admin/AjaxDistrict.html",{'dis':dis})



def subadmin(request):
    if 'aid' in request.session:
        con=Country.objects.all()
        if request.method=="POST" and request.FILES:
            conid=request.POST.get('sel_con')
            cont=Country.objects.get(id=conid)
            Subadmin.objects.create(subadmin_name=request.POST.get('txtname'),subadmin_contact=request.POST.get('contact'),
                                subadmin_email=request.POST.get('mail'),subadmin_address=request.POST.get('textaddress'),
                                subadmin_photo=request.FILES.get('file_photo'),subadmin_pwd=request.POST.get('pwd'),
                                subadmin_country=cont)
            return render(request,"Admin/Subadmin.html",{'CON':con})
        else:
            return render(request,"Admin/Subadmin.html",{'CON':con})
    else:
        return redirect("webguest:Login")


def admnhome(request):
    if 'aid' in request.session:
        an=Admin.objects.get(id=request.session['aid'])
        return render(request,"Admin/Adminhome.html",{'AN':an})
    else:
        return redirect("webguest:Login")


def usercomplaint(request):
    if 'aid' in request.session:
        usr=Complaint.objects.filter(user_id__gt=0)
        owr=Complaint.objects.filter(owner_id__gt=0)
        ofcr=Complaint.objects.filter(officer_id__gt=0)
        return render(request,"Admin/viewcomplaints.html",{'USR':usr,'OWR':owr,'OFCR':ofcr})
    else:
        return redirect("webguest:Login")

def feedback(request):
    if 'aid' in request.session:
        usr=Feedback.objects.filter(user_id__gt=0)
        owr=Feedback.objects.filter(owner_id__gt=0)
        ofcr=Feedback.objects.filter(officer_id__gt=0)
        return render(request,"Admin/viewfeedback.html",{'USR':usr,'OWR':owr,'OFCR':ofcr})
    else:
        return redirect("webguest:Login")

def del_feed(request,fid):
    Feedback.objects.get(id=fid).delete()
    return redirect("webadmin:feedback")


def rply(request,rid):
    com=Complaint.objects.get(id=rid)
    if request.method=="POST":
        com.complaint_replay=request.POST.get('txt_rply')
        com.save()
        return render(request,"Admin/Replay.html")
    else:
        return render(request,"Admin/Replay.html")

def del_urply(request,uid):
    Complaint.objects.get(id=uid).delete()
    return redirect("webadmin:usercomplaint")


def rply(request,rid):
    com=Complaint.objects.get(id=rid)
    if request.method=="POST":
        com.complaint_replay=request.POST.get('txt_rply')
        com.save()
        return render(request,"Admin/Replay.html")
    else:
        return render(request,"Admin/Replay.html")
