import imp
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import render
from django.http import JsonResponse,HttpResponse,HttpResponseRedirect
from plan.models import Plans

# Create your views here.

def BestPlan(request):
    if(request.GET.get('best')!=None):
        data = Plans.objects.order_by('plan_usage').reverse().values()[:int(request.GET.get('best'))]
    elif(request.GET.get('all')=='True'):
        data = Plans.objects.order_by('plan_usage').reverse().values()
    else:
        data = Plans.objects.order_by('plan_usage').reverse().values('plan_price','plan_talktime','plan_data','plan_validity','id')    
    result=[]
    for i in data: result.append(i)
    return JsonResponse(result,safe=False)

@csrf_exempt
def DeletePlan(request):
    if(request.method=="DELETE"):
        try:
            Plans.objects.filter(id=request.GET.get('plan')).delete()
            return HttpResponse("admin/viewpack?success=Plan Successfully Removed")
        except:
            return HttpResponse("admin/viewpack?error=Something went wrong")
    return HttpResponse("admin/viewpack?error=Invalid Request")

@csrf_exempt
def NewPlan(request):
    if(request.method=="POST"):
        price = request.POST.get('price')
        talktime = request.POST.get('talktime')
        data = request.POST.get('data')
        validity = request.POST.get('validity')
        try:
            Plans.objects.create(
                plan_price=price,
                plan_talktime=talktime,
                plan_data=data,
                plan_validity=validity,
                plan_usage=0
            )
            return HttpResponse("admin?success=Successfully added a new plan")
        except:
            return HttpResponse("admin/newplan?error=Something went wrong")
    return HttpResponse("admin/newplan?error=Invalid Request")


def Fetchplan(request):
    id = request.GET.get('id')
    try:
        data = Plans.objects.filter(id=id).values('id','plan_price','plan_talktime','plan_validity','plan_data')
        result=[]
        for i in data: result.append(i)
        print(result)
        return JsonResponse(result,safe=False)
    except Exception as e:
        print(e)
        return HttpResponseRedirect("http://localhost:4200/admin/editplan?id="+id+"&error=Something went wrong!!")


@csrf_exempt
def EditPlan(request):
    if(request.method=="POST"):
        price = request.POST.get('price')
        talktime = request.POST.get('talktime')
        data = request.POST.get('data')
        validity = request.POST.get('validity')
        id = request.POST.get('id')
        try:
            data =Plans.objects.filter(id=id)
            data.plan_price = price
            data.plan_talktime = talktime
            data.plan_validity=validity
            data.plan_data=data
            #saving
            data.save()
            return HttpResponse("admin?success=Plan Updated Successfully")
        except:
            return HttpResponse("admin/newplan?error=Something went wrong")
    return HttpResponse("admin/newplan?error=Invalid Request")


