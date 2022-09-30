
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse, HttpResponse, HttpResponseRedirect
from plan.models import Plans, Recharge
from account.models import Phone
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
        Data = request.POST.get('data')
        validity = request.POST.get('validity')
        id = request.POST.get('id')
        try:
            data =Plans.objects.get(id=id)
            data.plan_price = price
            data.plan_talktime = talktime
            data.plan_validity=validity
            data.plan_data=Data
            #saving
            data.save()
            return HttpResponse("admin?success=Plan Updated Successfully")
        except:
            return HttpResponse("admin/newplan?error=Something went wrong")
    return HttpResponse("admin/newplan?error=Invalid Request")



@csrf_exempt
def RechargePlan(request):
    if(request.method == "POST"):
        planId = request.POST.get("pid")
        hashPhone= request.POST.get("id")
        try:
            id = Phone.objects.filter(hashPhone=hashPhone).values('userId')[0].get('userId')
            Recharge.objects.create(
                userId = id,
                planId = planId
            )
            return HttpResponse("connection/bank?plan=True")
        except Exception as e:
            print(e)
            return HttpResponse("home?error=Something Went Wrong")

    return HttpResponse("home?error=Invalid Request")

