from tkinter.messagebox import NO
from django.shortcuts import render
from django.http import JsonResponse
from plan.models import Plans

# Create your views here.

def BestPlan(request):
    if(request.GET.get('best')!=None):
        data = Plans.objects.order_by('plan_usage').reverse().values('plan_price','plan_talktime','plan_data','plan_validity','id')[:int(request.GET.get('best'))]
    else:
        data = Plans.objects.order_by('plan_usage').reverse().values('plan_price','plan_talktime','plan_data','plan_validity','id')    
    result=[]
    for i in data: result.append(i)
    print(result)
    return JsonResponse(result,safe=False)