from django.shortcuts import render

# Create your views here.
from app.models import *
from django.http import HttpResponse
def insert_topic(request):
    if request.method=='POST':
        tn=request.POST['tn']
        TO=Topic.objects.get_or_create(topic_name=tn)[0]
        TO.save()
        return HttpResponse('topic_name is inserted successfully')
    return render(request,'insert_topic.html')
def insert_Webpage(request):
    lto=Topic.objects.all()
    d={'topics':lto}
    if request.method=='POST':
        topic_name=request.POST['topic']
        name=request.POST['name']
        url=request.POST['url']
        email=request.POST['email']
        TO=Topic.objects.get(topic_name=topic_name)
        WO=Webpage.objects.get_or_create(topic_name=TO,name=name,url=url,email=email)[0]
        WO.save()
        return HttpResponse('webpage data will be inserted successfully')

    return render(request,'insert_Webpage.html',d)
def insert_Accessrecord(request):
    lar=Webpage.objects.all()
    d={'access':lar}
    if request.method=='POST':
        name=request.POST['name']
        author=request.POST['author']
        date=request.POST['date']
        WO=Webpage.objects.get(name=name)
        AR=Accessrecord.objects.get_or_create(name=WO,author=author,date=date)[0]
        AR.save()
        return HttpResponse('insert_acesss is successfully !!!!')


    return render(request,'insert_Accessrecord.html',d)