from django.urls import path,include
from Officer import views
app_name="officer"

urlpatterns = [
    path('ohome/',views.officerhome,name="officerhome"),

    path('oprof/',views.officerprof,name="officerprofile"),
    path('edprf/<int:eid>',views.edprof,name="editprofile"),
    path('chgpwd/<int:cid>',views.chngpwd,name="changepass"),

    path('offcrcmplnt/',views.ofcrcmplnt,name="officercomplaint"),
    path('delcom/<int:comid>',views.delcom,name="del_com"),

    path('ofcrfeed/',views.ofcrfeedbck,name="officerfeedback"),
    path('delfeed/<int:fid>',views.delfeed,name="del_feed"),

    path('onrver/',views.ownrver,name="ownerverfication"),
    path('owner_accpt/<int:oaid>',views.ow_accpt,name="Owner_Accept"),
    path('owner_rjct/<int:orid>',views.ow_rjct,name="Owner_Reject"),
    path('onracptd/',views.ownraccpt,name="owneraccepted"),
    path('onrrejct/',views.ownrrjct,name="ownerrejected"),

    path('usrver/',views.usrver,name="userverification"),
    path('user_accpt/<int:uaid>',views.usr_accpt,name="user_Accept"),
    path('user_rjct/<int:urid>',views.usr_rjct,name="user_Reject"),
    path('usracptd/',views.usraccpt,name="useraccepted"),
    path('usrrejct/',views.usrrjct,name="userrejected"),
    

]
