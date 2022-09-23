# from django.shortcuts import render

from account.models import Users
import hashlib
from django.http import HttpResponse
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
            phone = self.__newPhone,
            password = self.__newPassword
        )

@csrf_exempt
def Signval(request):
    if(request.method == "POST"):
        User  = NewVoiceUser(request)
        if(User.check_empty()==True):
            User.encrypt()
            try:
                User.add()
                return HttpResponse("home")
            except:
                return HttpResponse("signup?error=Something Went Wrong!!")
        return HttpResponse("signup?error=Empty fields are not allowed")
    return HttpResponse("signup?error=Invalid Request")


@csrf_exempt
def Logval(request):
    if(request.method == "POST"):
        phone = request.POST.get('phone')
        temp_password = request.POST.get('password')
        password = hashlib.sha256(temp_password.encode())
        password = password.hexdigest()
        try:
            data = Users.objects.filter(phone=phone,password=password)
            if(data.count() == 1):
                return HttpResponse('profile')
            return HttpResponse('login?error=Username or Password is invalid')
        except:
            return HttpResponse('login?error=Something went wrong')   
    return HttpResponse("signup?error=Invalid Request")
