from django.urls import path
from blogg import views
urlpatterns = [
path("",views.homepage,name="home"),
path("aboutus/",views.homepage1,name="aboutus"),
path("contactus/",views.homepage2,name="contact"),
path("savedata",views.datasave),
path("services/",views.services,name="services"),
path("deletedata/<int:myid>", views.deletethisdata),
path("updatethis/<int:abc>", views.updatethisdata),
path("update-this-data/<int:updateid>", views.updatedata),
path("search",views.searchthisdata),
path("signup",views.signup,name="signup"),
path("signupdata",views.signupdata,name="signupdata"),
path("login",views.loginthis,name="login"),
path("loginto",views.loginto,name="loginto"),
path("logouthere",views.logouthere,name="logouthere"),
]



