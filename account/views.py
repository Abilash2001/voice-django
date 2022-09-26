# from django.shortcuts import render

from account.models import Users, Phone
import hashlib
from django.http import HttpResponse, JsonResponse
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
    def phoneno_exist(self) -> None:
        if(Phone.objects.filter(phoneNo=self.__newPhone).count() == 0):
            return False
        return True
    def check_exist(self) -> None:
        data = Phone.objects.filter(phoneNo=self.__newPhone).values()
        if(data.count()==0): return True
        
        if(data[0].get('register')==True):
            return False
        return True
    def add(self) -> None:
        data = Phone.objects.get(phoneNo=self.__newPhone)
        data.register = True
        data.save()
        Users.objects.create(
            name = self.__newUser,
            email = self.__newEmail,
            phone = self.__newPhone,
            password = self.__newPassword
        )
        return self.__newPhone
            


@csrf_exempt
def Signval(request):
    if(request.method == "POST"):
        User  = NewVoiceUser(request)
        if(User.check_empty()==True):
            if(User.check_exist()):
                if(User.phoneno_exist()):
                    User.encrypt()
                    try:
                        id= User.add()
                        return JsonResponse({"route":"profile","authenticate":True,"id":str(id)})
                    except:
                        return JsonResponse({"route":"signup?error=Something Went Wrong!!","authenticate":False})
                return JsonResponse({"location":"signup?error=Invalid PhoneNo","authenticate":"False"})
            return JsonResponse({"location":"signup?error=Phone No is already registered","authenticate":False})
        return JsonResponse({"location":"signup?error=Empty fields are not allowed","authenticate":False})
    return JsonResponse({"location":"signup?error=Invalid Request","authenticate":False})


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
