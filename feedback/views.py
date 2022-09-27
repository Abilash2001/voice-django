from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from django.shortcuts import render

# Create your views here.
from django.db import models

# Create your models here.
from feedback.models import UserFeedback
from django.views.decorators.csrf import csrf_exempt

class NewFeedback:
    def __init__(self, request) -> None:
        self.__FBName = request.POST.get('Name')
        self.__FBEmail = request.POST.get('Email')
        self.__FBFeedback = request.POST.get('Feedback')
        self.__FBStar = request.POST.get('Star')

    def check_fbempty(self) -> bool:
        if (len(self.__FBEmail) != 0 and len(self.__FBFeedback) != 0 and len(self.__FBName)!=0 and self.__FBStar!=None):
            return True
        return False

    def fbadd(self) -> None:
        return UserFeedback.objects.create(
                Email=self.__FBEmail,
                Feedback=self.__FBFeedback,
                Name = self.__FBName,
                Star=self.__FBStar
            )


@csrf_exempt
def FBVal(request):
    print(list(request.POST))
    if (request.method == "POST"):
        User1 = NewFeedback(request)
        if (User1.check_fbempty() == True):
            try:
                User1.fbadd()
                return HttpResponse("feedback?success=Feedback Submited Successfully")
            except:
                return HttpResponseRedirect("feedback?error=Something Went Wrong!!")
        return HttpResponseRedirect("feedback?error=Empty fields are not allowed")

    else:
        return HttpResponseRedirect("feedback?error=Invalid Request")



def FBdata(request):
    if(request.GET.get('best')!=None):
        data = UserFeedback.objects.values()
    elif(request.GET.get('all')=='True'):
        data =UserFeedback.objects.values()
    else:
        data = UserFeedback.objects.values('Email','Feedback')
    result=[]
    for i in data: result.append(i)
    return JsonResponse(result,safe=False)