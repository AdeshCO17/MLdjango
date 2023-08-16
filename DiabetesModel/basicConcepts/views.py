from django.shortcuts import render       #used to render the html pages

def Welcome(request):
    return render(request,'index.html')      


def User(request):
    username=request.GET['username']        # data coming from input of username 
    print(username)
    return render(request,'user.html',{'name':username})  #req present in name key
