from django.shortcuts import render
from .models import REG,PLACE
from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.models import User, auth
from django.http import HttpResponse
from django.conf import settings
from django.views.generic.list import ListView 
from math import radians, sin, cos, acos
#from .forms import CreateListForm

def login(request):
    if request.method== 'POST':
        username = request.POST['emailAddress']
        password = request.POST['password']
        request.session['user'] = username
        user1 = REG.objects.filter(email=username,password=password)
        len=user1.count()
        if len != 0:
            return render(request,'city.html')
        else:
            messages.info(request,'Invalid credentials... Retry...')
            return redirect('login')

    else:
        return render(request,'login.html')    

def registration(request):

    if request.method == 'POST':
        
        firstname = request.POST['firstName']
        lastname = request.POST['lastName']
        password2 = request.POST['password2']
        password1 = request.POST['password1']
        emailaddress = request.POST['emailAddress']
        mobile = request.POST['mobile']
        
        
        if password1==password2:
            
            if REG.objects.filter(email=emailaddress).exists():
                messages.info(request,'Email Taken')
                return redirect('registration')
            else:   
                user = REG(firstname=firstname,lastname=lastname, password=password1, email=emailaddress, mobile=mobile)
                user.save();
                print('user created')
                return redirect('login')

        else:
            messages.info(request,'password not matching..')    
            return redirect('registration')
        
        
    else:
        return render(request,'registration.html')

def portal(request):

    return render(request,'tourguide.html')
def getl(request):
    return render(request,'city.html')
def getm(request):
    if request.method == "POST":
        x = request.POST["op"]
        city=""
        if x=="1":
            return render(request,'routehyd.html')
        if x == "2":
            return render(request,'routeblr.html')
        
       
        
    else:
        return render(request,'loc.html')
def locdet(request):
    loc=[]
    if request.method == 'POST':
        loc = request.POST.getlist('btw')
        str=request.POST["start"]
        end=request.POST["end"]
        if str=="" or end=="" :
            return render(request,'locdet.html')
        else:
            m=PLACE.objects.get(id=str)
            start=m.name
            n=PLACE.objects.get(id=end)
            dest=n.name
            if start in loc:
                loc.remove(start)
                loc.insert(0,start)
            else:
                loc.insert(0,start)
            if dest in loc:
                loc.remove(dest)
                loc.insert(len(loc),dest)
            else:
                loc.insert(len(loc),dest)
            lat=[]
            log=[]
            for i in range(len(loc)):
                x=PLACE.objects.get(name=loc[i])
                dup_lat=float(x.latitude)
                dup_log=float(x.logitude)
                lat.append(dup_lat)
                log.append(dup_log)
            matrix=[]
            for i in range(len(lat)):          # A for loop for row entries 
                a =[] 
                for j in range(len(log)):      # A for loop for column entries 
                    a.append(0) 
                    matrix.append(a)
            dist=[]
            for i in range(len(lat)):
                for j in range(len(log)):
                    matrix[i][j] = 6371.01 * acos(sin(lat[i])*sin(lat[j]) + cos(lat[i])*cos(lat[j])*cos(log[i] - log[j]))
                
            print(matrix)
            return render(request,'locdet.html',{'loc':loc})

    




#def calcdist(request):
 #   laa=[laa1,laa2,laa3,laa4,laa5,laa6,laa7,laa7,laa8,laa9,laa10]#normal stuff
  #  lga=[lga1,lga2,lga3,lga4,lga5,lga6,lga7,lga7,lga8,lga9,lga10]#normal stuff
   # print("Input coordinates of two points:")
    #la7=radians(17.3507)
   # la=[la1,la2,la3,la4,la5,la6,la7,la8,la9,la10]#radian stuff
   # lg=[lg1,lg2,lg3,lg4,lg5,lg6,lg7,lg8,lg9,lg10]#radian stuff
   # for i in range(0,10):
    #    for j in range(0,10):
     #       count=count+1
      #      dist = 6371.01 * acos(sin(lat[i])*sin(lat[j]) + cos(lat[i])*cos(lat[j])*cos(log[i] - log[j]))
       #     print("distance between",laa[i],"and",laa[j],"is",round(dist) )
       

    