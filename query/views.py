from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from django.shortcuts import render

# Create your views here.
from django.views.decorators.csrf import csrf_exempt

from query.models import UserQuery


class NewQuery:
    def __init__(self, request) -> None:
        self.__QMobile = request.POST.get('mobile_no')
        self.__QEmail = request.POST.get('Email')
        self.__QQuery = request.POST.get('Query')
        self.__QCat = request.POST.get('a')

    def check_qempty(self) -> bool:
        if (len(self.__QMobile) != 0 and len(self.__QEmail) != 0 and len(self.__QQuery)!=0 and self.__QCat!=None):
            return True
        return False

    def qadd(self) -> None:
        return UserQuery.objects.create(
                Email=self.__QEmail,
                mobile_no=self.__QMobile,
                Query = self.__QQuery,
                a=self.__QCat
            )


@csrf_exempt
def QueryVal(request):
    if (request.method == "POST"):
        User1 = NewQuery(request)
        if (User1.check_qempty() == True):
            try:
                User1.qadd()
                return HttpResponse("query?success=Query Submited Successfully")
            except:
                return HttpResponseRedirect("Query?error=Something Went Wrong!!")
        return HttpResponseRedirect("Query?error=Empty fields are not allowed")

    else:
        return HttpResponseRedirect("Query?error=Invalid Request")


def FetchQuery(request):
    if(request.GET.get('fetchCount')!=None):
        data=[]
        data.append(UserQuery.objects.filter(a='1').count())
        data.append(UserQuery.objects.filter(a='2').count())
        data.append(UserQuery.objects.filter(a='3').count())
        data.append(UserQuery.objects.filter(a='4').count())
        data.append(UserQuery.objects.filter(a='5').count())
        return HttpResponse(data)
    else:
        data = UserQuery.objects.filter(a=request.GET.get('value')).values('mobile_no','Email','Query')
        result = []
        for i in data: result.append(i)
        return JsonResponse(result,safe=False)