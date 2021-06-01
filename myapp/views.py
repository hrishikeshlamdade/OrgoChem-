from django.shortcuts import render,HttpResponse
from .models import Box
# Create your views here.
def index(request):
    n1=Box()
    n1.name="Soil Sampling"
    n2=Box()
    n3=Box()
    n2.name="Environmental Planning"
    n3.name="Soil Feritlity"
    n4=Box()
    n4.name="Precision Agricultural"
    context={"na":[n1,n2,n3,n4]}
    return render(request,'index.html',context)
def about(request):
    context={
        "variable":"Sent from view"
    }
    return render(request,'about.html',context)
def services(request):
    context={
        "variable":"Sent from view"
    }
    return render(request,'services.html',context)
def contact(request):
    context={
        "variable":"Sent from view"
    }
    return render(request,'contact.html',context)
def fertilizers(request):
    context={
        "variable":"Sent from view"
    }
    return render(request,'fertilizers.html',context)
def pesticides(request):
    context={
        "variable":"Sent from view"
    }
    return render(request,'pesticides.html',context)
def prebook(request):
    context={
        "variable":"Sent from view"
    }
    return render(request,'prebook.html',context)
def roomserve(request):
    context={
            "variable":"Sent from view"
        }
    return render(request,'roomserve.html',context)
def add(request):
    num1=int(request.POST["n1"])
    num2=int(request.POST["n2"])
    res=num1+num2
    return render(request,'result.html',{"result":res})