from django.shortcuts import render,redirect
from django.http import HttpResponse
from blogg.models import contactUs
from django.core.mail import EmailMessage
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
# Create your views here.
@login_required
def homepage(request):
        return render(request, "home.html")
def homepage1(request):
        return render(request, "aboutus.html")

@login_required
def homepage2(request):
        return render(request, "contactus.html")

def datasave(request):
            if request.method == "POST":
             fullname = request.POST.get("name")
             email = request.POST.get("email")
             phone = request.POST.get("phone")
             message = request.POST.get("message")
             myimg = request.FILES.get('img')
             messageemail=f"""

          Name={fullname}
          email={email}
          phone={phone}
          message={message}


"""

             mail = EmailMessage("this is for testing django mail functionality", messageemail, "creative07vibez@gmail.com ", ["swagythakur@gmail.com"])
             mail.send()

             mydata = contactUs(username = fullname, email = email,  phone = phone, message = message,myimage = myimg)
             mydata.save()
             messages.success(request, "Your Data Saved Sucessfully ")
             return redirect("contact")
            


@login_required
def services(request):
       mydata=contactUs.objects.all()
       allrecord={"record":mydata}
       return render(request,"services.html",allrecord)


def deletethisdata(request, myid):
    
    data = contactUs.objects.get(id = myid)
    data.delete()

    messages.warning(request, "Your Data Deleted successfully")
    return redirect("services")
       
def updatethisdata(request, abc):
    
    udata = contactUs.objects.get(id = abc)

    return render(request, "update.html", {"upd" : udata})




def updatedata (request,updateid):
        if request.method == "POST":
             fullname = request.POST.get("name")
 
  
        
             email = request.POST.get("email")
             phone = request.POST.get("phone")
             message = request.POST.get("message")
        mydata = contactUs.objects.get(id = updateid)
        mydata.username = fullname
        mydata.email = email
        mydata.phone = phone
        mydata.message = message
        mydata.save()
        messages.info(request, "Updated successfully........... :D")

        return redirect("services")

def searchthisdata(request):
       srch=request.GET["query"]
       searchdata=contactUs.objects.filter(username=srch)
       allrecord={"record":searchdata}
       return render(request,"services.html",allrecord)


def signup (request):
       return render(request,"signup.html")

def signupdata (request):
        if request.method == "POST":
            username = request.POST.get("username")
            email = request.POST.get("email")
            Password = request.POST.get("password")
            FullName = request.POST.get("fname")

            saveuser = User.objects.create_user(username = username, email = email, password=Password, first_name = FullName)
            saveuser.save()

        return render(request, "signup.html")
        

def loginthis(request):
       return render (request,"login.html")


def loginto(request):
       if request.user.is_authenticated:
            return redirect('contact')

       if request.method=="POST":
         name = request.POST.get("username")
         passx = request.POST.get("password")
    
         usercheck = authenticate(username=name, password=passx)

         if usercheck is not None:
             login(request, usercheck)
             messages.success(request, "Login Sucessfully done..!")
        
         else:
             messages.warning(request, "PLease Enter vaild Crentationals!.... ")

       return render(request, "login.html")
def logouthere(request):
        logout(request)
        return redirect("login")


       