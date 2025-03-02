from django.shortcuts import render,redirect
from guest.models import User
from Admin.models import *
from User.models import *
from Owner.models import Rent,Gallery
from datetime import datetime

# Create your views here.

def userhome(request):
    if 'uid' in request.session:
        us=User.objects.get(id=request.session['uid'])
        return render(request,"User/Userhome.html",{'US':us})
    else:
        return redirect("webguest:Login")


def userprof(request):
    if 'uid' in request.session:
        usr=User.objects.get(id=request.session['uid'])
        return render(request,"User/Userprofile.html",{'PF':usr})
    else:
        return redirect("webguest:Login")

def edprof(request,eid):
    selusr=User.objects.get(id=eid)
    if request.method=="POST":
        selusr.user_name=request.POST.get('txt_name')
        selusr.user_contact=request.POST.get('cnct')
        selusr.user_email=request.POST.get('mail')
        selusr.user_address=request.POST.get('textaddress')
        selusr.save()
        return redirect('user:userprofile')
    else:
        return render(request,"User/Editprofile.html",{'EP':selusr})

def chngpwd(request,cid):
    change=User.objects.get(id=cid)
    if request.method=="POST":
        pwd=change.user_pwd
        current=request.POST.get('txt_pwd')
        if pwd == current:
            change=User.objects.get(id=cid)
            new=request.POST.get('txt_npwd')
            change.user_pwd=new
            change.save()
            return redirect('webguest:Login')
        else:
            error="Incorrect Password!!"
            return render(request,"User/Changepassword.html",{'ER':error})
    else:
        return render(request,"User/Changepassword.html")




def usrcmplnt(request):
    if 'uid' in request.session:
        com=Complaint.objects.all()
        us=User.objects.get(id=request.session['uid'])
        usr=Complaint.objects.filter(user_id=us)
        if request.method=="POST":
            Complaint.objects.create(complaint_title=request.POST.get('txt_cmplnttyp'),complaint_content=request.POST.get('txt_cntnt'),
                                 user_id=us)
            return render(request,"User/UserComplaints.html",{'COM':com,'USR':usr})
        else:
            return render(request,"User/UserComplaints.html",{'COM':com,'USR':usr})
    else:
        return redirect("webguest:Login")

def delcom(request,comid):
    Complaint.objects.get(id=comid).delete()
    return redirect("user:usercomplaint")

def usrfeedbck(request):
    if 'uid' in request.session:
        feed=Feedback.objects.all()
        us=User.objects.get(id=request.session['uid'])
        usr=Feedback.objects.filter(user_id=us)
        if request.method=="POST":
            Feedback.objects.create(feedback_content=request.POST.get('txt_feedback'),user_id=us)
            return render(request,"User/Userfeedback.html",{'FEED':feed,'USR':usr})
        else:
            return render(request,"User/Userfeedback.html",{'FEED':feed,'USR':usr})
    else:
        return redirect("webguest:Login")

def delfeed(request,fid):
    Feedback.objects.get(id=fid).delete()
    return redirect("user:userfeedback")




def srchrnt(request):
    if 'uid' in request.session:
        con=Country.objects.all()
        rnt=RentType.objects.all()
        if  request.method=="POST" and request.FILES:
            rtype=request.POST.get('sel_Rtype')
            rt=RentType.objects.get(id=rtype)
            result=Rent.objects.filter(renttype_id=rt)
            return render(request,"User/SearchRent.html",{'CON':con,'RNT':rnt,'Rent':result})
        else:
            rt=Rent.objects.all()
            return render(request,"User/SearchRent.html",{'CON':con,'RNT':rnt,'Rent':rt})
    else:
        return redirect("webguest:Login")




def ajax_rent(request):
    if request.GET.get('rid')=="":
        if request.GET.get('pid')!="":
            place=Place.objects.get(id=request.GET.get('pid'))   
            rentdetails=Rent.objects.filter(owner_id__owner_place=place)
            return render(request,"User/Ajax_SearchRent.html",{'SR':rentdetails})
        elif request.GET.get('did')!="":
            dis=District.objects.get(id=request.GET.get('did'))   
            rentdetails=Rent.objects.filter(owner_id__owner_place__district=dis)
            return render(request,"User/Ajax_SearchRent.html",{'SR':rentdetails})
        elif request.GET.get('sid')!="":
            st=State.objects.get(id=request.GET.get('sid'))   
            rentdetails=Rent.objects.filter(owner_id__owner_place__district__state=st)
            return render(request,"User/Ajax_SearchRent.html",{'SR':rentdetails})    
        else:
          
            cou=Country.objects.get(id=request.GET.get('cid'))   
            rentdetails=Rent.objects.filter(owner_id__owner_place__district__state__country_id=cou)
            return render(request,"User/Ajax_SearchRent.html",{'SR':rentdetails})
    else:
        rt=RentType.objects.get(id=request.GET.get('rid')) 
        if request.GET.get('pid')!="":
            place=Place.objects.get(id=request.GET.get('pid'))   
            rentdetails=Rent.objects.filter(owner_id__owner_place=place,renttype_id=rt)
            return render(request,"User/Ajax_SearchRent.html",{'SR':rentdetails})
        elif request.GET.get('did')!="":
            dis=District.objects.get(id=request.GET.get('did'))   
            rentdetails=Rent.objects.filter(owner_id__owner_place__district=dis,renttype_id=rt)
            return render(request,"User/Ajax_SearchRent.html",{'SR':rentdetails})
        elif request.GET.get('sid')!="":
            st=State.objects.get(id=request.GET.get('sid'))   
            rentdetails=Rent.objects.filter(owner_id__owner_place__district__state=st,renttype_id=rt)
            return render(request,"User/Ajax_SearchRent.html",{'SR':rentdetails})    
        elif request.GET.get('cid')!="":
            cou=Country.objects.get(id=request.GET.get('cid'))
            rentdetails=Rent.objects.filter(owner_id__owner_place__district__state__country_id=cou,renttype_id=rt)
            return render(request,"User/Ajax_SearchRent.html",{'SR':rentdetails})
        else:
             
            rentdetails=Rent.objects.filter(renttype_id=rt)
            return render(request,"User/Ajax_SearchRent.html",{'SR':rentdetails})



def viewgallery(request,glid):
    rent=Rent.objects.get(id=glid)
    gal=Gallery.objects.filter(rent_id=rent)
    return render(request,"User/ViewGallery.html",{'GL':gal})



def rntbook(request,rid):
    rnt=Rent.objects.get(id=rid)
    us=User.objects.get(id=request.session['uid'])
    if request.method=="POST":
        Booking.objects.create(booking_fromdate=request.POST.get('f_date'),booking_todate=request.POST.get('t_date'),user_id=us,rent_id=rnt)
        return render(request,"User/RentBooking.html",{'RNT':rnt})
    else:
        return render(request,"User/RentBooking.html",{'RNT':rnt})

def mybook(request):
    if 'uid' in request.session:
        book=Booking.objects.all()
        return render(request,"User/MyBookings.html",{'BOOK':book})
    else:
        return redirect("webguest:Login")

    



    
def paynow(request,pid):
    pay=Booking.objects.get(id=pid)
    if request.method=="POST":
        pay.payment_status=1
        pay.save()
        return redirect('user:mybookings')
    else:
        return render(request,"User/Payment.html")

