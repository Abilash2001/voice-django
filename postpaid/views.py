from django.shortcuts import render

# Create your views here.
from django.shortcuts import render

# Create your views here.
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse, HttpResponse, HttpResponseRedirect
from postpaid.models import Postpaidplan


# Create your views here.

def BestPlan(request):
    if (request.GET.get('best') != None):
        data = Postpaidplan.objects.order_by('plan_usage').reverse().values()[:int(request.GET.get('best'))]
    elif (request.GET.get('all') == 'True'):
        data = Postpaidplan.objects.order_by('plan_usage').reverse().values()
    else:
        data = Postpaidplan.objects.order_by('plan_usage').reverse().values('plan_price', 'plan_talktime', 'plan_data',
                                                                            'id')
    result = []
    for i in data: result.append(i)
    return JsonResponse(result, safe=False)


@csrf_exempt
def DeletePlan(request):
    if (request.method == "DELETE"):
        try:
            Postpaidplan.objects.filter(id=request.GET.get('plan')).delete()
            return HttpResponse("admin/viewpostpaid?success=Plan Successfully Removed")
        except:
            return HttpResponse("admin/viewpostpaid?error=Something went wrong")
    return HttpResponse("admin/viewpostpaid?error=Invalid Request")


@csrf_exempt
def NewPlan(request):
    if (request.method == "POST"):
        price = request.POST.get('price')
        talktime = request.POST.get('talktime')
        data = request.POST.get('data')
        try:
            Postpaidplan.objects.create(
                plan_price=price,
                plan_talktime=talktime,
                plan_data=data,
                plan_usage=0
            )
            return HttpResponse("admin?success=Successfully added a new plan")
        except:
            return HttpResponse("admin/newpostpaid?error=Something went wrong")
    return HttpResponse("admin/newpostpaid?error=Invalid Request")


def Fetchplan(request):
    id = request.GET.get('id')
    try:
        data = Postpaidplan.objects.filter(id=id).values('id', 'plan_price', 'plan_talktime', 'plan_data')
        result = []
        for i in data: result.append(i)
        print(result)
        return JsonResponse(result, safe=False)
    except Exception as e:
        print(e)
        return HttpResponseRedirect(
            "http://localhost:4200/admin/editpostplan?id=" + id + "&error=Something went wrong!!")


@csrf_exempt
def EditPlan(request):
    if (request.method == "POST"):
        price = request.POST.get('price')
        talktime = request.POST.get('talktime')
        Data = request.POST.get('data')
        id = request.POST.get('id')
        try:
            data = Postpaidplan.objects.get(id=id)
            data.plan_price = price
            data.plan_talktime = talktime
            data.plan_data = Data
            # saving
            data.save()
            return HttpResponse("admin?success=Plan Updated Successfully")
        except:
            return HttpResponse("admin/newpostpaid?error=Something went wrong")
    return HttpResponse("admin/newpostpaid?error=Invalid Request")

