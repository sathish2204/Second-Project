from django.http.response import HttpResponse
from django.shortcuts import redirect, render
from django.views.decorators.cache import cache_control


from app1 import models
from app1.models import employe
from app1.models import india
from app1.models import australia
from app1.models import team1_batting
from app1.models import team2_batting
from app1.models import team1_bowling
from app1.models import team2_bowling

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


def update(request,score,overs,covers,team1,team2,striker,non_striker,bowler,wickets,pid1,pid2):
    
    if team1 =='India':
        
        if  request.POST['runs'] == '':
            runs= 0
        else:
            runs = int(request.POST['runs'])
            score += runs
            
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

        


        obt1ba = team1_batting()
        obt2ba = team2_batting()

        obt1bo = team1_bowling()
        obt2bo = team2_bowling()


        
       
        
        if  request.POST['wc'] == 'none':
            pass
        else:
            twicket = request.POST['wc']
        
            if twicket == 'bold':
                wickets += 1
                ob1 = team2_bowling.objects.get(id = 1)
                ob1.name = bowler
                ob1.wickets += 1
                ob1.runs += runs
                ob1.save()
                
                

            elif twicket == 'lbw':
                wickets += 1

            elif twicket == 'catch':
                wickets += 1

            elif twicket == 'striker':
                wickets += 1

            elif twicket == 'non_striker':
                wickets += 1
    
            
    

    
    

        obj = india.objects.all()
        s1 = obj.get(id=pid1)
        s2 = obj.get(id=pid2)
        p1 = s1.name
        p2 = s2.name



        
    

    

        if runs == 1 or runs == 3 :
            if striker == p1 :  
                if covers == 1 or covers == 2  or covers == 3 or covers == 4 or covers == 5 or covers == 6 or covers == 7 or covers == 8 or covers == 9 or covers == 10 :
                    striker = p1
                    non_striker = p2
                else:
                    striker = p2
                    non_striker = p1
            elif striker == p2 :  
                if covers == 1 or covers == 2  or covers == 3 or covers == 4 or covers == 5 or covers == 6 or covers == 7 or covers == 8 or covers == 9 or covers == 10 :
                    striker = p2
                    non_striker = p1
                
                else:
                    striker = p1
                    non_striker = p2
                
        
            return render(request,'update.html',{'score':score,'overs':overs,'covers':covers,'team1':team1,'team2':team2,'striker':striker,'non_striker':non_striker,'bowler':bowler,'wickets':wickets,'pid1':pid1,'pid2':pid2})
    

        elif runs == 2 or runs == 4 or runs == 6:
            if striker == p1 :
                if covers == 1 or covers == 2  or covers == 3 or covers == 4 or covers == 5 or covers == 6 or covers == 7 or covers == 8 or covers == 9 or covers == 10 :
                    striker = p2
                    non_striker = p1
                else:
                    striker = p1
                    non_striker = p2
            elif striker == p2 :
                if covers == 1 or covers == 2  or covers == 3 or covers == 4 or covers == 5 or covers == 6 or covers == 7 or covers == 8 or covers == 9 or covers == 10 :
                    striker = p1
                    non_striker = p2
                
                else:
                    striker = p2
                    non_striker = p1

            return render(request,'update.html',{'score':score,'overs':overs,'covers':covers,'team1':team1,'team2':team2,'striker':striker,'non_striker':non_striker,'bowler':bowler,'wickets':wickets,'pid1':pid1,'pid2':pid2})

        return render(request,'update.html',{'score':score,'overs':overs,'covers':covers,'team1':team1,'team2':team2,'striker':striker,'non_striker':non_striker,'bowler':bowler,'wickets':wickets,'pid1':pid1,'pid2':pid2})

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
    pid1 = 1
    pid2 = 2
    


    team1 = request.POST['dropdown']
    team2 = request.POST['dropdown2']
    
    check1 = request.POST['c1']


    if team1 == 'India':
        ob2 =australia.objects.all()
        temp = ob2.get(id=7)
        bowler = temp.name
    else:
        ob2 =india.objects.all()
        temp = ob2.get(id=7)
        bowler = temp.name
        
    if check1 == 'c1':
        overs = 10
    else:
        overs = 5

    return render(request,'delete.html',{'team1':team1,'team2':team2,'overs':overs,'score':score,'wickets':wickets,'covers':covers,'bowler':bowler,'striker':striker,'non_striker':non_striker,'pid1':pid1,'pid2':pid2})




def allemployes(request):

    obj = employe.objects.all()
    return render(request,'allemployes.html',{'obj':obj})


def insert(request):

    ob = employe()
    return render(request,'insert.html')