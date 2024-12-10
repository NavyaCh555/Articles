from django.shortcuts import render
from .models import Article
data=Article.objects.all().order_by('id')


# Create your views here.
def index(req):
    context={
        'data':data
    }
    return render(req,'index.html',context)

def details(req,pk):
    data1= Article.objects.get(id=pk) 
    context={
        'data1':data1
    } 
    return render(req,'details.html',context)
def abouts(req):
   context={
    'data':data
   }
   return render(req,'about.html',context)