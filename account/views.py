# from django.shortcuts import render
from account.models import Users, Phone, UsersDetails, Connection
import hashlib
from django.http import  JsonResponse, HttpResponse
from django.views.decorators.csrf import csrf_exempt
# Create your views here.

class NewVoiceUser:
    def __init__(self,request) -> None:
        self.__newUser = request.POST.get('name')
        self.__newEmail = request.POST.get('email')
        self.__newPhone = request.POST.get('phone')
        self.__tempPass = request.POST.get('password')
        self.__category = request.POST.get('usercat')
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
            password = self.__newPassword,
            isAdmin = False
        )
        return Users.objects.filter(phone=self.__newPhone).values()[0].get('id')
    
    def UpdateAndFetchHashPhone(self,id):
        data = Phone.objects.get(phoneNo = self.__newPhone)
        data.userId = id
        data.save()
        return data.hashPhone
    def Cat(self,id):
        UsersDetails.objects.create(
            userId=id,
            userCat=self.__category
        )

        

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
                        User.Cat(id)
                        hasphone = User.UpdateAndFetchHashPhone(id)
                        return JsonResponse({"route":"profile","authenticate":True,"id":str(hasphone)})
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
                hashid = hashlib.sha256(phone.encode())
                hashid =hashid.hexdigest()
                if(data.values()[0].get('isAdmin')==True):
                    return JsonResponse({"location":"admin","authenticate":True,"id":str(hashid)})
                return JsonResponse({"location":'home',"authenticate":True,"id":str(hashid)})
            return JsonResponse({"location":'login?error=Username or Password is invalid',"authenticate":False})
        except Exception as e:
            print(e)
            return JsonResponse({"location":'login?error=Something went wrong',"authenticate":False})   
    return JsonResponse({"location":"signup?error=Invalid Request","authenticate":False})


@csrf_exempt
def AddAccount(request):
    if(request.method == "POST"):
        phoneNo = request.POST.get('phoneNo')
        password = hashlib.sha256(request.POST.get('password').encode())
        password = password.hexdigest()
        try:
            Users.objects.create(
                name = "admin",
                phone = phoneNo,
                password = password,
                isAdmin = True
            )
            return HttpResponse("admin?success=Successfully created a new account")
        except:
            return HttpResponse("admin?error=Something went wrong!!!")
    return HttpResponse("admin?error=Invalid Request")


def FetchCategory(request):
    result= []
    result.append(UsersDetails.objects.filter(userCat='p').count())
    result.append(UsersDetails.objects.filter(userCat='P').count())
    result.append(UsersDetails.objects.filter(userCat='d').count())
    return HttpResponse(result)


def FetchUserCount(request):
    result=[0 for _ in range(12)]
    data = UsersDetails.objects.order_by('joined').values('joined')
    for i in range(len(data)):
        match(data[i].get('joined').month):
            case 1: result[0] +=1
            case 2: result[1] +=1
            case 3: result[2] +=1
            case 4: result[3] +=1
            case 5: result[4] +=1
            case 6: result[5] +=1
            case 7: result[6] +=1
            case 8: result[7] +=1
            case 9: result[8] +=1
            case 10: result[9] +=1
            case 11: result[10] +=1
            case 12: result[11] +=1
    return HttpResponse(result)


def CheckAdmin(request):
    usid= request.GET.get('sid')
    usaid = request.GET.get('said')
    if(usid!=None):
        try:
            data = Phone.objects.filter(hashPhone = usid).values('userId')[0]
            id = data.get('userId')
            result = Users.objects.filter(id=id).values('isAdmin')[0]
            print(result.get('isAdmin'))
            if(result.get('isAdmin')==True):
                return HttpResponse('admin')
            return HttpResponse("home")
        except:
            return HttpResponse('checkadmin')
    elif(usaid!=None):
        try:
            data = Users.objects.filter(isAdmin=True).values('phone')
            for i in data:
                getHashValue = hashlib.sha256(data.get('phone').encode())
                getHashValue = getHashValue.hexdigest()
                if(getHashValue==usaid):
                    return HttpResponse("admin")
        except:
            return HttpResponse("home")


@csrf_exempt
def Subscriber(request):
    if(request.method == "POST"):
        pincode = request.POST.get('pincode')
        phoneNo = request.POST.get('phoneno')
        state = request.POST.get('state')
        address = request.POST.get('address')
        try:
            if(pincode!=None and phoneNo!=None and state!=None and address!=None):
                Connection.objects.create(
                    pincode=pincode,
                    state=state,
                    phoneNo=phoneNo,
                    address=address
                )
                data = Phone.objects.filter(userId=0).values('phoneNo')[0]
                return JsonResponse({"phone":data.get('phoneNo'),"location":"connection"})
        except Exception as e:
            return JsonResponse({"phone":"nil","location":"connection?error=Something went wrong!!!"})
    return JsonResponse({"phone":"nil","location":"connection?error=Invalid Request"})