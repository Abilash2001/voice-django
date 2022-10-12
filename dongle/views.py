from django.shortcuts import render

# Create your views here.
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import render
from django.http import JsonResponse, HttpResponse, HttpResponseRedirect
from dongle.models import Dongleplans, Recharge
from account.models import Phone, Users

# Create your views here.

def dBestPlan(request):
    if(request.GET.get('best')!=None):
        data = Dongleplans.objects.order_by('plan_usage').reverse().values()[:int(request.GET.get('best'))]
    elif(request.GET.get('all')=='True'):
        data = Dongleplans.objects.order_by('plan_usage').reverse().values()
    else:
        data = Dongleplans.objects.order_by('plan_usage').reverse().values('plan_price','plan_data','plan_validity','id')
    result=[]
    for i in data: result.append(i)
    return JsonResponse(result,safe=False)

@csrf_exempt
def DeletePlan(request):
    if(request.method=="DELETE"):
        try:
            Dongleplans.objects.filter(id=request.GET.get('plan')).delete()
            return HttpResponse("admin/viewdonglepack?success=Plan Successfully Removed")
        except:
            return HttpResponse("admin/viewdonglepack?error=Something went wrong")
    return HttpResponse("admin/viewdonglepack?error=Invalid Request")

@csrf_exempt
def NewDPlan(request):
    if(request.method=="POST"):
        price = request.POST.get('price')
        data = request.POST.get('data')
        validity = request.POST.get('validity')
        try:
            Dongleplans.objects.create(
                plan_price=price,
                plan_data=data,
                plan_validity=validity,
                plan_usage=0
            )
            return HttpResponse("admin?success=Successfully added a new plan")
        except:
            return HttpResponse("admin/newdongleplan?error=Something went wrong")
    return HttpResponse("admin/newdongleplan?error=Invalid Request")


def Fetchplan(request):
    id = request.GET.get('id')
    try:
        data = Dongleplans.objects.filter(id=id).values('id','plan_price','plan_validity','plan_data')
        result=[]
        for i in data: result.append(i)
        print(result)
        return JsonResponse(result,safe=False)
    except Exception as e:
        print(e)
        return HttpResponseRedirect("http://localhost:4200/admin/editdongle?id="+id+"&error=Something went wrong!!")


@csrf_exempt
def EditPlan(request):
    if(request.method=="POST"):
        price = request.POST.get('price')
        Data = request.POST.get('data')
        validity = request.POST.get('validity')
        id = request.POST.get('id')
        try:
            data =Dongleplans.objects.get(id=id)
            data.plan_price = price
            data.plan_validity=validity
            data.plan_data=Data
            #saving
            data.save()
            return HttpResponse("admin?success=Plan Updated Successfully")
        except:
            return HttpResponse("admin/newdongleplan?error=Something went wrong")
    return HttpResponse("admin/newdongleplan?error=Invalid Request")

@csrf_exempt
def DongleRechargePlan(request):
    if(request.method == "POST"):
        planId = request.POST.get("pid")
        hashPhone= request.POST.get("id")
        try:
            id = Phone.objects.filter(hashPhone=hashPhone).values('userId')[0].get('userId')
            Recharge.objects.create(
                userId = id,
                planId = planId
            )
            data = Dongleplans.objects.get(id=planId)
            data.plan_usage+=1
            data.save()
            return HttpResponse("connection/bank?dongle=True")
        except Exception as e:
            print(e)
            return HttpResponse("home?error=Something Went Wrong")

    return HttpResponse("home?error=Invalid Request")
