from django.shortcuts import render
from .models import Item
from django.views.decorators.csrf import ensure_csrf_cookie

# Create your views here.

@ensure_csrf_cookie
def video(request):
    videolist = []
    if request.method == 'POST':
        obj = Item.objects.all()
        pno=request.POST.get('btn')
        for i in obj:
            if i.playlist==pno:
                videolist.append(i.video)
    return render(request,'videos.html',{'allvideo':videolist})



@ensure_csrf_cookie
def search(request):
    videolist=[]
    if request.method=='GET':
        obj=Item.objects.all()
        query=request.GET.get('query')
        for i in obj:
            i.desc=i.playlist+' '+i.desc
            if query in i.desc or query.capitalize() in i.desc or query.upper() in i.desc or query.lower() in i.desc:
                videolist.append(i.video)
    if len(videolist)==0 or len(query)==0 :
        return render(request,'home.html')
    else:
        return render(request,'videos.html',{'allvideo':videolist})


def playlist(request):
    return render(request,'tutorials.html')



