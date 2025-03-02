from django.urls import path
from Admin import views
app_name="webadmin"

urlpatterns = [
    path('cntry/',views.country,name="Country"),
    path('delcon/<int:cid>',views.del_con,name="Del_con"),
    path('upcon/<int:eid>',views.up_con,name="Up_count"),

    path('sta/',views.sta,name="state"),
    path('delsta/<int:sid>',views.Del_sta,name="del_sta"),
    
    path('dist/',views.dis,name="district"),
    path('pla/',views.plc,name="place"),
    path('delpl/<int:pid>',views.Del_pl,name="del_pl"),
    path('del_dis/<int:disid>',views.Del_dis,name="del_dis"),

    path('rnttyp/',views.renttype,name="renttype"),
    path('delrnt/<int:rid>',views.del_rnt,name="del_rnt"),

    path('ajaxstate/', views.AjaxState, name="Ajax-State"),
    path('ajaxdistrict/',views.AjaxDistrict,name="Ajax-District"),

    path('sadmin/',views.subadmin,name="subadmin"),

    path('ahome/',views.admnhome,name="adminhome"),
    
    path('usrcom/',views.usercomplaint,name="usercomplaint"),
    path('rply/<int:rid>',views.rply,name="replay"),
    path('delurply/<int:uid>',views.del_urply,name="delusrrply"),

    path('feed/',views.feedback,name="feedback"),
    path('delfeed/<int:fid>',views.del_feed,name="delfeed"),
  
    
    
]