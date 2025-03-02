from django.urls import path,include
from guest import views
app_name="webguest"

urlpatterns = [
    path('log/',views.log,name="Login"),
    path('usrr/',views.usr,name="Userreg"),
    path('ajaxplace/',views.AjaxPlace,name="Ajax-Place"),
    path('ownrr/',views.ownr,name="ownrreg"),
    path('home/',views.home,name="homepage"),
    path('fpass/', views.ForgetPassword,name="forpass"),
    path('otpver/', views.OtpVerification,name="verification"),
    path('create/', views.CreateNewPass,name="create"),
   
    
]
