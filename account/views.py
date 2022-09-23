# from django.shortcuts import render
import imp
from account.models import Users
import hashlib
from django.http import HttpResponseRedirect
from django.views.decorators.csrf import csrf_exempt
# Create your views here.

class NewVoiceUser:
    def __init__(self,request) -> None:
        self.__newUser = request.POST.get('name')
        self.__newEmail = request.POST.get('email')
        self.__newPhone = request.POST.get('phone')
        self.__tempPass = request.POST.get('password')
    def check_empty(self) -> bool:
        if(len(self.__newUser)!=0 and len(self.__newEmail)!=0 and len(self.__newPhone)!=0 and len(self.__tempPass)!=0):
            return True
        return False
    def encrypt(self) -> None:
        self.__newPassword = hashlib.sha256(self.__tempPass.encode())
        self.__newPassword = self.__newPassword.hexdigest()
    def add(self) -> None:
        return Users.objects.create(
            name = self.__newUser,
            email = self.__newEmail,
            password = self.__newPassword
        )
        
@csrf_exempt
def Signval(request):
    print(list(request.POST))
    if(request.method == "POST"):
        User  = NewVoiceUser(request)
        if(User.check_empty()==True):
            User.encrypt()
            try:
                User.add()
                return HttpResponseRedirect("http://localhost:4200/home")
            except:
                return HttpResponseRedirect("http://localhost:4200/signup?error=Something Went Wrong!!")
        return HttpResponseRedirect("http://localhost:4200/signup?error=Empty fields are not allowed")

    else:
        return HttpResponseRedirect("http://localhost:4200/signup?error=Invalid Request")