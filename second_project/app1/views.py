from django.http.response import HttpResponse
from django.shortcuts import redirect, render
from django.views.decorators.cache import cache_control


from app1 import models
from app1.models import employe
from app1.models import india
from app1.models import australia

@cache_control(no_cache=True, must_revalidate=True, no_store=True)
def home(request):
    if request.method == 'POST':
        
        name = str(request.POST['username'])
        password = str(request.POST['password'])
        if name == 'sathish' and password == '87654321':
            return render(request,'select.html')     

        else:
            return render(request,'home.html',{'msg':'Invalid Username or Password'})
    return render(request,'home.html')



def select(request):
    return render(request,'select.html',)


def update(request,score,overs,covers,team1,team2,striker,non_striker,bowler,wickets):
    
    runs = int(request.POST['runs'])
    covers = round(float(covers),1)
    if covers == 0.5 :
        covers = 1
    elif covers == 1.5:
        covers = 2
    elif covers == 2.5:
        covers = 3
    elif covers == 3.5:
        covers = 4
    elif covers == 4.5:
        covers = 5
    elif covers == 5.5:
        covers = 6
    elif covers == 6.5:
        covers = 7
    elif covers == 7.5:
        covers = 8
    elif covers == 8.5:
        covers = 9
    elif covers == 9.5:
        covers = 10
    else:
        covers = round(covers + 0.1,1)
    score += runs

    obj = india.objects.all()
    s1 = obj.get(id=1)
    s2 = obj.get(id=2)
    p1 = s1.id
    p2 = s2.id


    if runs == 1 or runs == 3 :
        if striker == 'KL Rahul' :  
            if covers == 1 or covers == 2  or covers == 3 or covers == 4 or covers == 5 or covers == 6 or covers == 7 or covers == 8 or covers == 9 or covers == 10 :
                striker = 'KL Rahul'
                non_striker = 'Rohit Sharma'
            else:
                striker = 'Rohit Sharma'
                non_striker = 'KL Rahul'
        elif striker == 'Rohit Sharma' :  
            if covers == 1 or covers == 2  or covers == 3 or covers == 4 or covers == 5 or covers == 6 or covers == 7 or covers == 8 or covers == 9 or covers == 10 :
                striker = 'Rohit Sharma'
                non_striker = 'KL Rahul'
                
            else:
                striker = 'KL Rahul'
                non_striker = 'Rohit Sharma'
                
        
        return render(request,'update.html',{'score':score,'overs':overs,'covers':covers,'team1':team1,'team2':team2,'striker':striker,'non_striker':non_striker,'bowler':bowler,'wickets':wickets})
    

    elif runs == 2 or runs == 4 or runs == 6:
        if striker == 'KL Rahul' :
            if covers == 1 or covers == 2  or covers == 3 or covers == 4 or covers == 5 or covers == 6 or covers == 7 or covers == 8 or covers == 9 or covers == 10 :
                striker = 'Rohit Sharma'
                non_striker = 'KL Rahul'
            else:
                striker = 'KL Rahul'
                non_striker = 'Rohit Sharma'
        elif striker == 'Rohit Sharma' :
            if covers == 1 or covers == 2  or covers == 3 or covers == 4 or covers == 5 or covers == 6 or covers == 7 or covers == 8 or covers == 9 or covers == 10 :
                striker = 'KL Rahul'
                non_striker = 'Rohit Sharma'
                
            else:
                striker = 'Rohit Sharma'
                non_striker = 'KL Rahul'

        return render(request,'update.html',{'score':score,'overs':overs,'covers':covers,'team1':team1,'team2':team2,'striker':striker,'non_striker':non_striker,'bowler':bowler,'wickets':wickets})

    

def delete(request):
    obj = india.objects.all()
    s1 = obj.get(id=1)
    s2 = obj.get(id=2)
    striker = s1.name
    non_striker = s2.name
    score = 0
    wickets = 0
    covers = 0
    overs = 0
    bowler = 'Mitcheal Stark'


    team1 = request.POST['dropdown']
    team2 = request.POST['dropdown2']
    
    check1 = request.POST['c1']
        
    if check1 == 'c1':
        overs = 10
    else:
        overs = 5

    return render(request,'delete.html',{'team1':team1,'team2':team2,'overs':overs,'score':score,'wickets':wickets,'covers':covers,'bowler':bowler,'striker':striker,'non_striker':non_striker})




def allemployes(request):

    obj = employe.objects.all()
    return render(request,'allemployes.html',{'obj':obj})


def insert(request):

    ob = employe()
    return render(request,'insert.html')