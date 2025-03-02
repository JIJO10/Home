from django.urls import path,include
from User import views
app_name="user"


urlpatterns = [
    path('usrhome/',views.userhome,name="userhome"),

    path('usrprof/',views.userprof,name="userprofile"),
    path('edprf/<int:eid>',views.edprof,name="editprofile"),
    path('chgpwd/<int:cid>',views.chngpwd,name="changepass"),

    path('usrcmplnt/',views.usrcmplnt,name="usercomplaint"),
    path('delcom/<int:comid>',views.delcom,name="del_com"),

    path('usrfeed/',views.usrfeedbck,name="userfeedback"),
    path('delfeed/<int:fid>',views.delfeed,name="del_feed"),
    
    path('srchrent/',views.srchrnt,name="searchrent"),
    path('viewgallery/<int:glid>',views.viewgallery,name="viewgallery"),
    path('searchrent/',views.ajax_rent,name="Ajax-SearchRent"),
    path('rntbook/<int:rid>',views.rntbook,name="rentbooking"),
    
    path('mybook/',views.mybook,name="mybookings"),
    path('paynow/<int:pid>',views.paynow,name="paynow"),
]