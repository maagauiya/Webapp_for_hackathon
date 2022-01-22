from django.http import HttpResponse
from django.shortcuts import render
from .models import*
from django.core import serializers
def index(request):
    if request.POST.get('save'):
        name=request.POST.get("fname") 
        surname=request.POST.get("lname") 
        father_name=request.POST.get("otec") 
        serial_id=request.POST.get("iin") 
        city=request.POST.get("city") 
        street=request.POST.get("ulica") 
        home_n=request.POST.get("house") 
        flat_n=request.POST.get("kvnum") 
        cad_n=request.POST.get("kadastr") 
        area_n=request.POST.get("s") 
        addi_info=request.POST.get("dopl")
        lat=request.POST.get("lat")
        lng=request.POST.get("lng")
        info=User()
        info.surname=surname
        info.name=name
        info.father_name=father_name
        info.serial_id=serial_id
        info.city=city
        info.street=street
        info.home_n=home_n
        info.flat_n=flat_n
        info.cad_n=cad_n
        info.area_n=area_n
        info.addi_info=addi_info
        info.lat=lat
        info.lng=lng
        info.save()
    return render(request,'hackapp/index.html')

def liste(request):
    user = User.objects.all()
    context={ 
        'user' : user
    }
    return render(request,'hackapp/list.html',context=context)

def pageofuser(request,userid):
   
    if request.POST.get('update'):
        i_upt=User.objects.get(pk=userid)
        if request.POST.get("lname") is not None:
            i_upt.surname=request.POST.get("lname")
        if request.POST.get("fname") is not None:
            i_upt.name=request.POST.get("fname")
        if request.POST.get("otec") is not None:
            i_upt.father_name=request.POST.get("otec")
        if request.POST.get("iin") is not None:
            i_upt.serial_id=request.POST.get("iin")
        if request.POST.get("city") is not None:
            i_upt.city=request.POST.get("city")
        if request.POST.get("ulica") is not None:
            i_upt.street=request.POST.get("ulica")
        if request.POST.get("house") is not None:
            i_upt.home_n=request.POST.get("house")
        if request.POST.get("kvnum") is not None:
            i_upt.flat_n=request.POST.get("kvnum")
        if request.POST.get("kadastr") is not None:
            i_upt.cad_n=request.POST.get("kadastr")
        if request.POST.get("s") is not None:
            i_upt.area_n=request.POST.get("s")
        if request.POST.get("lat") is not None:
            i_upt.lat=request.POST.get("lat")
        if request.POST.get("lng") is not None:
            i_upt.lng=request.POST.get("lng")
        if request.POST.get("dopl") is not None:
            i_upt.addi_info=request.POST.get("dopl")
        i_upt.save()
    elif request.POST.get('delete'):
        i_del=User.objects.get(pk=userid)
        i_del.delete()
        user = User.objects.all()
        context={ 
            'user' : user
        }
        return render(request,'hackapp/list.html',context=context)

        
    user2=serializers.serialize("json",User.objects.filter(pk=userid))
    user=User.objects.filter(pk=userid)
    context={
        "user" : user,
        "user2":user2
    }

    return render(request,'hackapp/index2.html',context=context)