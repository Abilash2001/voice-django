from django.shortcuts import render
from django.http import JsonResponse
from plan.models import Plans

# Create your views here.

def BestPlan(request):
    data = Plans.objects.filter(plan_usage=request.GET.get('usage')).values('plan_price','plan_talktime','plan_data','plan_validity')    
    result=[]
    for i in data: result.append(i)
    return JsonResponse(result,safe=False)