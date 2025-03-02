from django.urls import path,include
from Owner import views
app_name="owner"

urlpatterns = [
    path('onrhome/',views.ownerhome,name="ownerhome"),

    path('onrprof/',views.ownerprof,name="ownerprofile"),
    path('edprf/<int:eid>',views.edprof,name="editprofile"),
    path('chgpwd/<int:cid>',views.chngpwd,name="changepass"),

    path('adrnt/',views.addrnt,name="addrent"),
    path('delrnt/<int:rntid>',views.delrent,name="del_rent"),
    path('adrnt/<int:glid>',views.addgalry,name="add_galry"),
    path('delgal/<int:galid>',views.delgal,name="del_galry"),

    path('onrcmplnt/',views.ownrcmplnt,name="ownercomplaint"),
    path('delcom/<int:comid>',views.delcom,name="del_com"),

    path('onrfeed/',views.ownrfeedbck,name="ownerfeedback"),
    path('delfeed/<int:fid>',views.delfeed,name="del_feed"),
    
    path('myrntbook/',views.myrntbook,name="myrentbookings"),
    path('accept/<int:aid>',views.acpt,name="accept"),
    path('reject/<int:rid>',views.rjct,name="reject"),


    
]