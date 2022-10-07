"""voice URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from account import views as ac
from plan import views as pl
from feedback import views as fb
from dongle import views as dg
from postpaid import views as p
from query import views as q

urlpatterns = [
    path('admin/', admin.site.urls),
    
    path('sign',ac.Signval),
    path('login',ac.Logval),
    path('newadmin',ac.AddAccount),

    path('plan',pl.BestPlan),
    path('remplan',pl.DeletePlan),
    path('addplan',pl.NewPlan),
    path('editplan',pl.EditPlan),

    path('feedback',fb.FBVal),
    path('getReview',fb.FetchFeedback),

    path('dongle',dg.dBestPlan),
    path('dongleplan',dg.NewDPlan),
    path('delplan',dg.DeletePlan),
    path('edit',dg.EditPlan),

    path('fetchplan',pl.Fetchplan),
    path('fetchCat',ac.FetchCategory),
    path('usersCount',ac.FetchUserCount),
    path('fetchAdmin',ac.CheckAdmin),

    
    path('connection',ac.Subscriber),

    path('postplan',p.BestPlan),
    path('dltplan',p.DeletePlan),
    path('newpost',p.NewPlan),
    path('editpostplan',p.EditPlan),
    path('fetchpostplan',p.Fetchplan),

    path('recharge',pl.RechargePlan),

    path('queries',q.QueryVal),
    path('getquery',q.FetchQuery)

]
