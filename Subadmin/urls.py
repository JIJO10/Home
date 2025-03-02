from django.urls import path,include
from Subadmin import views
app_name="subadmin"

urlpatterns = [
    path('shome/',views.subhom,name="subhome"),
    path('mprof/',views.profile,name="myprofile"),
    path('eprof/<int:eid>',views.edprof,name="editprofile"),
    path('chpwd/<int:cid>',views.chngpwd,name="changepass"),
    path('oreg/',views.officer,name="officerreg"),

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