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


def update(request,score,overs,covers,team1,team2,striker,non_striker,bowler,wickets,pid1,pid2,gone,stbow,op1b,op2b,op1r,op2r,b1,b2,b3,b4,b5,b6,sp1,sp2,bowo,bowr,boww ):
    
    if team1 =='india':
        if covers == overs:
            return render(request,'delete.html',{'team1':team1,'team2':team2,'overs':overs,'score':score,'wickets':wickets,'covers':covers,'bowler':bowler,'striker':striker,'non_striker':non_striker,'pid1':pid1,'pid2':pid2,'gone':gone,'stbow':stbow,'op1r':op1r,'op2r':op2r,'op1b':op1b,'op2b':op2b,'b1':b1,'b2':b2,'b3':b3,'b4':b4,'b5':b5,'b6':b6,'sp1':sp1,'sp2':sp2,'bowo':bowo,'bowr':bowr,'boww':boww })
        
        obj = india.objects.all()
        obtab = team2_bowling.objects.all()
        s1 = obj.get(id=pid1)
        s2 = obj.get(id=pid2)
        p1 = s1.name
        p2 = s2.name
        


        
        
        

        
        
        if  request.POST['runs'] == '':
            runs= 0
        else:
            runs = int(request.POST['runs'])
            score += runs
          
        
            
        covers = round(float(covers),1)

        if covers == 0.5 :
            if request.POST['rc'] != 'wide' and request.POST['rc'] != 'no ball' and request.POST['rc'] != 'over throw':
                covers = 1
                b1 = b2 = b3 = b4 = b5 = b6 = ' '
            
        elif covers == 1.5:
            if request.POST['rc'] != 'wide' and request.POST['rc'] != 'no ball' and request.POST['rc'] != 'over throw':
                covers = 2
                b1 = b2 = b3 = b4 = b5 = b6 = ' '
        elif covers == 2.5:
            if request.POST['rc'] != 'wide' and request.POST['rc'] != 'no ball' and request.POST['rc'] != 'over throw':
                covers = 3
                b1 = b2 = b3 = b4 = b5 = b6 = ' '
        elif covers == 3.5:
            if request.POST['rc'] != 'wide' and request.POST['rc'] != 'no ball' and request.POST['rc'] != 'over throw':
                covers = 4
                b1 = b2 = b3 = b4 = b5 = b6 = ' '
        elif covers == 4.5:
            if request.POST['rc'] != 'wide' and request.POST['rc'] != 'no ball' and request.POST['rc'] != 'over throw':
                covers = 5
                b1 = b2 = b3 = b4 = b5 = b6 = ' '
        elif covers == 5.5:
            if request.POST['rc'] != 'wide' and request.POST['rc'] != 'no ball' and request.POST['rc'] != 'over throw':
                covers = 6
                b1 = b2 = b3 = b4 = b5 = b6 = ' '
        elif covers == 6.6:
            if request.POST['rc'] != 'wide' and request.POST['rc'] != 'no ball' and request.POST['rc'] != 'over throw':
                covers = 7
                b1 = b2 = b3 = b4 = b5 = b6 = ' '
        elif covers == 7.7:
            if request.POST['rc'] != 'wide' and request.POST['rc'] != 'no ball' and request.POST['rc'] != 'over throw':
                covers = 8
                b1 = b2 = b3 = b4 = b5 = b6 = ' '
        elif covers == 8.9:
            if request.POST['rc'] != 'wide' and request.POST['rc'] != 'no ball' and request.POST['rc'] != 'over throw':
                covers = 9
                b1 = b2 = b3 = b4 = b5 = b6 = ' '
        elif covers == 9.9:
            if request.POST['rc'] != 'wide' and request.POST['rc'] != 'no ball' and request.POST['rc'] != 'over throw':
                covers = 10
                b1 = b2 = b3 = b4 = b5 = b6 = ' '
        else:
            if request.POST['rc'] == 'wide' and request.POST['rc'] == 'no ball' and request.POST['rc'] != 'over throw':
                covers = round(covers,1)
            else:
                if request.POST['rc'] != 'wide' and request.POST['rc'] != 'no ball' and request.POST['rc'] != 'over throw':
                    covers = round(covers + 0.1,1)


        
        wc = request.POST['wc']

        if covers == 0:
            if request.POST['rc'] == 'over throw':
                b1 = 'ot'
            elif wc == 'none' and request.POST['rc'] != 'wide' and request.POST['rc'] != 'no ball':  
                b1 = runs
            elif request.POST['rc'] == 'wide':
                b1 = 'wd'
            elif request.POST['rc'] == 'no ball':
                b1 = 'nb'
            
            elif request.POST['wc'] == 'striker' or request.POST['wc'] == 'non striker':
                b1 = 'ro'
            else:
                b1 = 'w'

        
        if covers == 0.1 or covers == 1.1 or covers == 2.1 or covers == 3.1 or covers == 4.1 or covers == 5.1 or covers == 6.1 or covers == 7.1 or covers == 8.1 or covers == 9.1  :
            if request.POST['rc'] == 'over throw':
                b1 = 'ot'
            elif wc == 'none' and request.POST['rc'] != 'wide' and request.POST['rc'] != 'no ball':  
                b1 = runs
            elif request.POST['rc'] == 'wide':
                b2 = 'wd'
            elif request.POST['rc'] == 'no ball':
                b2 = 'nb'
            
            elif request.POST['wc'] == 'striker' or request.POST['wc'] == 'non striker':
                b2 = 'ro'
            else:
                b1 = 'w'
        elif covers == 0.2 or covers == 1.2 or covers == 2.2 or covers == 3.2 or covers == 4.2 or covers == 5.2 or covers == 6.2 or covers == 7.2 or covers == 8.2 or covers == 9.2  :
            if request.POST['rc'] == 'over throw':
                b2 = 'ot'
            elif wc == 'none' and request.POST['rc'] != 'wide' and request.POST['rc'] != 'no ball':  
                b2 = runs
            elif request.POST['rc'] == 'wide':
                b3 = 'wd'
            elif request.POST['rc'] == 'no ball':
                b3 = 'nb'
            
            elif request.POST['wc'] == 'striker' or request.POST['wc'] == 'non striker':
                b3 = 'ro'
            else:
                b2 = 'w'
        elif covers == 0.3 or covers == 1.3 or covers == 2.3 or covers == 3.3 or covers == 4.3 or covers == 5.3 or covers == 6.3 or covers == 7.3 or covers == 8.3 or covers == 9.3 :
            if request.POST['rc'] == 'over throw':
                b3 = 'ot'
            elif wc == 'none' and request.POST['rc'] != 'wide' and request.POST['rc'] != 'no ball':  
                b3 = runs
            elif request.POST['rc'] == 'wide':
                b4 = 'wd'
            elif request.POST['rc'] == 'no ball':
                b4 = 'nb'
            
            elif request.POST['wc'] == 'striker' or request.POST['wc'] == 'non striker':
                b4 = 'ro'
            else:
                b3 = 'w'
        elif covers == 0.4 or covers == 1.4 or covers == 2.4 or covers == 3.4 or covers == 4.4 or covers == 5.4 or covers == 6.4 or covers == 7.4 or covers == 8.4 or covers == 9.4  :
            if request.POST['rc'] == 'over throw':
                b4 = 'ot'
            elif wc == 'none' and request.POST['rc'] != 'wide' and request.POST['rc'] != 'no ball':  
                b4 = runs
            elif request.POST['rc'] == 'wide':
                b5 = 'wd'
            elif request.POST['rc'] == 'no ball':
                b5 = 'nb'
            
            elif request.POST['wc'] == 'striker' or request.POST['wc'] == 'non striker':
                b5 = 'ro'
            else:
                b4 = 'w'
        elif covers == 0.5 or covers == 1.5 or covers == 2.5 or covers == 3.5 or covers == 4.5 or covers == 5.5 or covers == 6.5 or covers == 7.5 or covers == 8.5 or covers == 9.5  :
            if request.POST['rc'] == 'over throw':
                b5 = 'ot'
            elif wc == 'none' and request.POST['rc'] != 'wide' and request.POST['rc'] != 'no ball':  
                b5 = runs
            elif request.POST['rc'] == 'wide':
                b6 = 'wd'
            elif request.POST['rc'] == 'no ball':
                b6 = 'nb'
            
            elif request.POST['wc'] == 'striker' or request.POST['wc'] == 'non striker':
                b6 = 'ro'
            else:
                b5 = 'w'
        
        
        


        ind = india.objects.all()
        aus = australia.objects.all()

        obt1ba = team1_batting.objects.all()
        obt2ba = team2_batting.objects.all()

        obt1bo = team1_bowling.objects.all()
        obt2bo = team2_bowling.objects.all()


        

        
        
        if request.POST['wc'] == 'none' or request.POST['rc'] == 'no ball':
            s1 = obj.get(id=pid1)
            s2 = obj.get(id=pid2)
            p1 = s1.name
            p2 = s2.name

            ob1 = obt1ba.get(id=pid1)
            ob2 = obt1ba.get(id=pid2)
            

            if sp1 == '*':
        
                obow = obt2bo.get(id = stbow)
                if request.POST['rc'] == 'runs':
                    ob1.runs += runs
                    ob1.balls += 1

                elif request.POST['rc'] == 'leg bye':
                    ob1.balls += 1

                elif request.POST['rc'] == 'wide':
                    obow.runs += 1
                    score += 1

                elif request.POST['rc'] == 'no ball':
                    ob1.runs += runs
                    obow.runs += 1
                    score += 1

                elif request.POST['rc'] == 'over throw':
                    ob1.runs += runs
                    

        
                    
                    

                if obow.overs == 0.5:
                    if request.POST['rc'] == 'runs' or request.POST['rc'] == 'leg bye':
                        obow.overs = 1
                        bowo = round(round(obow.overs,1),1)
                        stbow += 1
                else:
                    if request.POST['rc'] == 'runs' or request.POST['rc'] == 'leg bye' :
                        obow.overs += round(round(0.1,1),1)
                        bowo = round(round(obow.overs,1),1)


                obow.runs += runs
                
            
                indba = ind.get(id = pid1)
                indba.runs += runs

            
                obow.save()
                ob1.save()
                indba.save()

                op1b = ob1.balls
                op1r = ob1.runs


                tbr =  obtab.get(id = stbow)  #For Bowler Runs and  Wickets
                bowr = tbr.runs
                boww = tbr.wickets


            else:

            
                obow = obt2bo.get(id = stbow)
                if request.POST['rc'] == 'runs':
                    ob2.runs += runs
                    ob2.balls += 1

                elif request.POST['rc'] == 'leg bye':
                    ob2.balls += 1

                elif request.POST['rc'] == 'wide':
                    obow.runs += 1
                    score += 1

                elif request.POST['rc'] == 'no ball':
                    ob2.runs += runs
                    obow.runs += 1
                    score += 1

                elif request.POST['rc'] == 'over throw':
                    ob2.runs += runs
                   
                    
                    

                if obow.overs == 0.5:
                    if request.POST['rc'] == 'runs' or request.POST['rc'] == 'leg bye' :
                        obow.overs = 1
                        bowo = round(round(obow.overs,1),1)
                        stbow += 1
                else:
                    if request.POST['rc'] == 'runs' or request.POST['rc'] == 'leg bye' :
                        obow.overs += round(round(0.1,1),1)
                        bowo = round(round(obow.overs,1),1)


                obow.runs += runs
                
            
                indba = ind.get(id = pid1)
                indba.runs += runs

            
                obow.save()
                ob2.save()
                indba.save()

                op2b = ob2.balls
                op2r = ob2.runs


                tbr =  obtab.get(id = stbow)  #For Bowler Runs and  Wickets
                bowr = tbr.runs
                boww = tbr.wickets
                
            
        
                
        elif  request.POST['wc'] == 'bold' and request.POST['rc'] != 'no ball':

            if sp1 == '*':
                wc = request.POST['wc']
                ob1 = obt1ba.get(id=pid1)
                obow = obt2bo.get(id = stbow)
                ob1.balls += 1
                ob1.bowler = bowler
                ob1.wicket = wc
                if obow.overs == 0.5:
                    obow.overs = 1
                    bowo = round(round(obow.overs,1),1)
                    if request.POST['rc'] != 'no ball':
                        stbow += 1
                else:
                    
                    obow.overs += round(round(0.1,1),1)
                    bowo = round(round(obow.overs,1),1)
                obow.runs += runs
                obow.wickets += 1
            
                indba = ind.get(id = pid1)
                indba.runs += runs
                obow.save()
                ob1.save()
                indba.save()
        
                wickets += 1 
            
            
                gone += 1
                pid1 = gone
                ob1 = obt1ba.get(id=pid1)
                striker = ob1.name
                op1b = 0
                op1r = 0
            

            
                ob1.save()
                obow.save()
                indba.save()


                
                tbr =  obtab.get(id = stbow)  #For Bowler Runs and  Wickets
                bowr = tbr.runs
                boww = tbr.wickets
                
            else:
                wc = request.POST['wc']
                ob2 = obt1ba.get(id=pid2)
                obow = obt2bo.get(id = stbow)
                ob2.balls += 1
                ob2.bowler = bowler
                ob2.wicket = wc
                if obow.overs == 0.5:
                    obow.overs = 1
                    bowo = round(round(obow.overs,1),1)
                    if request.POST['rc'] != 'no ball':
                        stbow += 1
                else:
                    
                    obow.overs += round(round(0.1,1),1)
                    bowo = round(round(obow.overs,1),1)
                obow.runs += runs
                obow.wickets += 1
            
                indba = ind.get(id = pid1)
                indba.runs += runs
                obow.save()
                ob2.save()
                indba.save()
        
                wickets += 1 
            
            
                gone += 1
                pid2 = gone
                ob2 = obt1ba.get(id=pid2)
                non_striker = ob2.name
                op2b = 0
                op2r = 0
            

            
                ob2.save()
                obow.save()
                indba.save()



                
                tbr =  obtab.get(id = stbow)  #For Bowler Runs and  Wickets
                bowr = tbr.runs
                boww = tbr.wickets
                

        elif request.POST['wc'] == 'lbw' and request.POST['rc'] != 'no ball':
            
            if sp1 == '*':
                wc = request.POST['wc']
                ob1 = obt1ba.get(id=pid1)
                obow = obt2bo.get(id = stbow)
                ob1.balls += 1
                ob1.bowler = bowler
                ob1.wicket = wc
                if obow.overs == 0.5:
                    obow.overs = 1
                    bowo = round(round(obow.overs,1),1)
                    if request.POST['rc'] != 'no ball':
                        stbow += 1
                else:
                    
                    obow.overs += round(round(0.1,1),1)
                    bowo = round(round(obow.overs,1),1)
                obow.runs += runs
                obow.wickets += 1
            
                indba = ind.get(id = pid1)
                indba.runs += runs
                obow.save()
                ob1.save()
                indba.save()
        
                wickets += 1 
            
            
                gone += 1
                pid1 = gone
                ob1 = obt1ba.get(id=pid1)
                striker = ob1.name
                op1b = 0
                op1r = 0
            

            
                ob1.save()
                obow.save()
                indba.save()



                
                tbr =  obtab.get(id = stbow)  #For Bowler Runs and  Wickets
                bowr = tbr.runs
                boww = tbr.wickets
                
            else:
                wc = request.POST['wc']
                ob2 = obt1ba.get(id=pid2)
                obow = obt2bo.get(id = stbow)
                ob2.balls += 1
                ob2.bowler = bowler
                ob2.wicket = wc
                if obow.overs == 0.5:
                    obow.overs = 1
                    bowo = round(round(obow.overs,1),1)
                    if request.POST['rc'] != 'no ball':
                        stbow += 1
                else:
                    
                    obow.overs += round(round(0.1,1),1)
                    bowo = round(round(obow.overs,1),1)
                obow.runs += runs
                obow.wickets += 1
            
                indba = ind.get(id = pid1)
                indba.runs += runs
                obow.save()
                ob2.save()
                indba.save()
        
                wickets += 1 
            
            
                gone += 1
                pid2 = gone
                ob2 = obt1ba.get(id=pid2)
                non_striker = ob2.name
                op2b = 0
                op2r = 0
            

            
                ob2.save()
                obow.save()
                indba.save()




                
                tbr =  obtab.get(id = stbow)  #For Bowler Runs and  Wickets
                bowr = tbr.runs
                boww = tbr.wickets

        elif request.POST['wc'] == 'catch' and request.POST['rc'] != 'no ball':
            
            if sp1 == '*':
                wc = request.POST['wc']
                ob1 = obt1ba.get(id=pid1)
                obow = obt2bo.get(id = stbow)
                ob1.balls += 1
                ob1.bowler = bowler
                ob1.wicket = wc
                if obow.overs == 0.5:
                    obow.overs = 1
                    bowo = round(round(obow.overs,1),1)
                    if request.POST['rc'] != 'no ball':
                        stbow += 1
                else:   
                    obow.overs += round(round(0.1,1),1)
                    bowo = round(round(obow.overs,1),1)
                obow.runs += runs
                obow.wickets += 1
            
                indba = ind.get(id = pid1)
                indba.runs += runs
                obow.save()
                ob1.save()
                indba.save()
        
                wickets += 1 
            
            
                gone += 1
                pid1 = gone
                ob1 = obt1ba.get(id=pid1)
                striker = ob1.name
                op1b = 0
                op1r = 0
            

            
                ob1.save()
                obow.save()
                indba.save()




                
                tbr =  obtab.get(id = stbow)  #For Bowler Runs and  Wickets
                bowr = tbr.runs
                boww = tbr.wickets
                
            else:
                wc = request.POST['wc']
                ob2 = obt1ba.get(id=pid2)
                obow = obt2bo.get(id = stbow)
                ob2.balls += 1
                ob2.bowler = bowler
                ob2.wicket = wc
                if obow.overs == 0.5:
                    obow.overs = 1
                    bowo = round(round(obow.overs,1),1)
                    if request.POST['rc'] != 'no ball':
                        stbow += 1
                else:
                    
                        
                    obow.overs += round(round(0.1,1),1)
                    bowo = round(round(obow.overs,1),1)
                obow.runs += runs
                obow.wickets += 1
            
                indba = ind.get(id = pid1)
                indba.runs += runs
                obow.save()
                ob2.save()
                indba.save()
        
                wickets += 1 
            
            
                gone += 1
                pid2 = gone
                ob2 = obt1ba.get(id=pid2)
                non_striker = ob2.name
                op2b = 0
                op2r = 0
            

            
                ob2.save()
                obow.save()
                indba.save()




                
                tbr =  obtab.get(id = stbow)  #For Bowler Runs and  Wickets
                bowr = tbr.runs
                boww = tbr.wickets

        elif request.POST['wc'] == 'striker' :
            
            if sp1 == '*':
                wc = request.POST['wc']
                ob1 = obt1ba.get(name = striker)
                obow = obt2bo.get(id = stbow)
                ob1.balls += 1
                ob1.bowler = bowler
               
                if obow.overs == 0.5:
                    obow.overs = 1
                    bowo = round(round(obow.overs,1),1)
                    stbow += 1
                else:
                    
                    obow.overs += round(round(0.1,1),1)
                    bowo = round(round(obow.overs,1),1)
                obow.runs += runs
                
            
                indba = ind.get(id = pid1)
                indba.runs += runs
                obow.save()
                ob1.save()
                indba.save()
        
                wickets += 1 
            
            
                gone += 1
                pid1 = gone
                ob1 = obt1ba.get(id=pid1)
                striker = ob1.name
                op1b = 0
                op1r = 0
            

            
                ob1.save()
                obow.save()
                indba.save()




                
                tbr =  obtab.get(id = stbow)  #For Bowler Runs and  Wickets
                bowr = tbr.runs
                boww = tbr.wickets

            else:
                wc = request.POST['wc']
                ob2 = obt1ba.get(name = striker)
                obow = obt2bo.get(id = stbow)
                ob2.balls += 1
                ob2.bowler = bowler
                ob2.wicket = wc
                if obow.overs == 0.5:
                    obow.overs = 1
                    bowo = round(round(obow.overs,1),1)
                    stbow += 1
                else:
                    obow.overs += round(round(0.1,1),1)
                    bowo = round(round(obow.overs,1),1)
                obow.runs += runs
                
            
                indba = ind.get(id = pid1)
                indba.runs += runs
                obow.save()
                ob2.save()
                indba.save()
        
                wickets += 1 
            
            
                gone += 1
                pid2 = gone
                ob2 = obt1ba.get(id=pid2)
                striker = ob2.name
                op2b = 0
                op2r = 0
            

            
                ob2.save()
                obow.save()
                indba.save()


                
                tbr =  obtab.get(id = stbow)  #For Bowler Runs and  Wickets
                bowr = tbr.runs
                boww = tbr.wickets
                
            
        elif request.POST['wc'] == 'non striker':
            if sp2 == ' ':
                wc = request.POST['wc']
                ob2 = obt1ba.get(name = non_striker)
                obow = obt2bo.get(id = stbow)
                ob2.balls += 1
                ob2.bowler = bowler
               
                if obow.overs == 0.5:
                    obow.overs = 1
                    bowo = round(round(obow.overs,1),1)
                    stbow += 1
                else:
                    
                    obow.overs += round(round(0.1,1),1)
                    bowo = round(round(obow.overs,1),1)
                obow.runs += runs
                
            
                indba = ind.get(id = pid1)
                indba.runs += runs
                obow.save()
                ob2.save()
                indba.save()
        
                wickets += 1 
            
            
                gone += 1
                pid2 = gone
                ob2 = obt1ba.get(id=pid2)
                non_striker = ob2.name
                op2b = 0
                op2r = 0
            

            
                ob2.save()
                obow.save()
                indba.save()




                
                tbr =  obtab.get(id = stbow)  #For Bowler Runs and  Wickets
                bowr = tbr.runs
                boww = tbr.wickets
            
            else:
                wc = request.POST['wc']
                ob1 = obt1ba.get(name = non_striker)
                obow = obt2bo.get(id = stbow)
                ob1.balls += 1
                ob1.bowler = bowler
                ob1.wicket = wc
                if obow.overs == 0.5:
                    obow.overs = 1
                    bowo = round(round(obow.overs,1),1)
                    stbow += 1
                else:
                    obow.overs += round(round(0.1,1),1)
                    bowo = round(round(obow.overs,1),1)
                obow.runs += runs
                
            
                indba = ind.get(id = pid1)
                indba.runs += runs
                obow.save()
                ob1.save()
                indba.save()
        
                wickets += 1 
            
            
                gone += 1
                pid1 = gone
                ob1 = obt1ba.get(id=pid1)
                striker = ob1.name
                op1b = 0
                op1r = 0
            

            
                ob1.save()
                obow.save()
                indba.save()


                
                tbr =  obtab.get(id = stbow)  #For Bowler Runs and  Wickets
                bowr = tbr.runs
                boww = tbr.wickets
                
            
                
        
        temp = obtab.get(id = stbow)
        bowler = temp.name


        
        bowo = round(round(temp.overs,1),1)
        


        s1 = obj.get(id=pid1)
        s2 = obj.get(id=pid2)
        p1 = s1.name
        p2 = s2.name


                      #For Changing Bowler After Over Completed....


        if runs == 0 and request.POST['wc'] == 'none':          #For Rotating Strike....
            if sp1 == '*' :  
                if covers == 1 or covers == 2  or covers == 3 or covers == 4 or covers == 5 or covers == 6 or covers == 7 or covers == 8 or covers == 9 or covers == 10 :
                    sp1 = ' '
                    sp2 = '*'
                   
                    
                else:
                    sp1 = '*'
                    sp2 = ' '
            elif sp1 == '*' :  
                if covers == 1 or covers == 2  or covers == 3 or covers == 4 or covers == 5 or covers == 6 or covers == 7 or covers == 8 or covers == 9 or covers == 10 :
                    sp1 = '*'
                    sp2 = ' '
                   
                
                else:
                    sp1 = ' '
                    sp2 = '*'
                
        
            return render(request,'delete.html',{'team1':team1,'team2':team2,'overs':overs,'score':score,'wickets':wickets,'covers':covers,'bowler':bowler,'striker':striker,'non_striker':non_striker,'pid1':pid1,'pid2':pid2,'gone':gone,'stbow':stbow,'op1r':op1r,'op2r':op2r,'op1b':op1b,'op2b':op2b,'b1':b1,'b2':b2,'b3':b3,'b4':b4,'b5':b5,'b6':b6,'sp1':sp1,'sp2':sp2, 'bowo':bowo  ,'bowr':bowr,'boww':boww })

        if runs == 0 and request.POST['wc'] != 'none':          #For Rotating Strike....
            if sp1 == '*' :  
                if covers == 1 or covers == 2  or covers == 3 or covers == 4 or covers == 5 or covers == 6 or covers == 7 or covers == 8 or covers == 9 or covers == 10 :
                    sp1 = ' '
                    sp2 = '*'
                   
                    
                else:
                    sp1 = '*'
                    sp2 = ' '
            elif sp2 == '*' :  
                if covers == 1 or covers == 2  or covers == 3 or covers == 4 or covers == 5 or covers == 6 or covers == 7 or covers == 8 or covers == 9 or covers == 10 :
                    sp1 = '*'
                    sp2 = ' '
                   
                
                else:
                    sp1 = ' '
                    sp2 = '*'
                
        
            return render(request,'delete.html',{'team1':team1,'team2':team2,'overs':overs,'score':score,'wickets':wickets,'covers':covers,'bowler':bowler,'striker':striker,'non_striker':non_striker,'pid1':pid1,'pid2':pid2,'gone':gone,'stbow':stbow,'op1r':op1r,'op2r':op2r,'op1b':op1b,'op2b':op2b,'b1':b1,'b2':b2,'b3':b3,'b4':b4,'b5':b5,'b6':b6,'sp1':sp1,'sp2':sp2, 'bowo':bowo ,'bowr':bowr,'boww':boww })

    

        if runs == 1 or runs == 3 :          #For Rotating Strike....
            if sp1 == '*' :  
                if covers == 1 or covers == 2  or covers == 3 or covers == 4 or covers == 5 or covers == 6 or covers == 7 or covers == 8 or covers == 9 or covers == 10 :
                    sp1 = '*'
                    sp2 = ' '
                    
                    
                else:
                    sp1 = ' '
                    sp2 = '*'
                    
            elif sp2 == '*' :  
                if covers == 1 or covers == 2  or covers == 3 or covers == 4 or covers == 5 or covers == 6 or covers == 7 or covers == 8 or covers == 9 or covers == 10 :
                    sp1 = ' '
                    sp2 = '*'
                
                else:
                    sp1 = '*'
                    sp2 = ' '
                    
                
        
            return render(request,'delete.html',{'team1':team1,'team2':team2,'overs':overs,'score':score,'wickets':wickets,'covers':covers,'bowler':bowler,'striker':striker,'non_striker':non_striker,'pid1':pid1,'pid2':pid2,'gone':gone,'stbow':stbow,'op1r':op1r,'op2r':op2r,'op1b':op1b,'op2b':op2b,'b1':b1,'b2':b2,'b3':b3,'b4':b4,'b5':b5,'b6':b6,'sp1':sp1,'sp2':sp2,'bowo':bowo ,'bowr':bowr,'boww':boww })
    

        elif runs == 2 or runs == 4 or runs == 6:
            if sp1 == '*' :
                if covers == 1 or covers == 2  or covers == 3 or covers == 4 or covers == 5 or covers == 6 or covers == 7 or covers == 8 or covers == 9 or covers == 10 :
                    sp1 = ' '
                    sp2 = '*'
                   
                else:
                    sp1 = '*'
                    sp2 = ' '
            elif sp2 == '*' :
                if covers == 1 or covers == 2  or covers == 3 or covers == 4 or covers == 5 or covers == 6 or covers == 7 or covers == 8 or covers == 9 or covers == 10 :
                    sp1 = '*'
                    sp2 = ' '
                   
                
                else:
                    sp1 = ' '
                    sp2 = '*'

            return render(request,'delete.html',{'team1':team1,'team2':team2,'overs':overs,'score':score,'wickets':wickets,'covers':covers,'bowler':bowler,'striker':striker,'non_striker':non_striker,'pid1':pid1,'pid2':pid2,'gone':gone,'stbow':stbow,'op1r':op1r,'op2r':op2r,'op1b':op1b,'op2b':op2b,'b1':b1,'b2':b2,'b3':b3,'b4':b4,'b5':b5,'b6':b6,'sp1':sp1,'sp2':sp2,'bowo':bowo ,'bowr':bowr,'boww':boww })

        return render(request,'delete.html',{'team1':team1,'team2':team2,'overs':overs,'score':score,'wickets':wickets,'covers':covers,'bowler':bowler,'striker':striker,'non_striker':non_striker,'pid1':pid1,'pid2':pid2,'gone':gone,'stbow':stbow,'op1r':op1r,'op2r':op2r,'op1b':op1b,'op2b':op2b,'b1':b1,'b2':b2,'b3':b3,'b4':b4,'b5':b5,'b6':b6,'sp1':sp1,'sp2':sp2,'bowo':bowo,'bowr':bowr,'boww':boww })

def update2(request,score,overs,covers,team1,team2,striker,non_striker,bowler,wickets,pid1,pid2,gone,stbow,op1b,op2b,op1r,op2r,b1,b2,b3,b4,b5,b6,sp1,sp2,bowo,bowr,boww ):
    if team1 =='australia':
        if covers == overs:
            return render(request,'delete2.html',{'team1':team1,'team2':team2,'overs':overs,'score':score,'wickets':wickets,'covers':covers,'bowler':bowler,'striker':striker,'non_striker':non_striker,'pid1':pid1,'pid2':pid2,'gone':gone,'stbow':stbow,'op1r':op1r,'op2r':op2r,'op1b':op1b,'op2b':op2b,'b1':b1,'b2':b2,'b3':b3,'b4':b4,'b5':b5,'b6':b6,'sp1':sp1,'sp2':sp2,'bowo':bowo,'bowr':bowr,'boww':boww })
        
        obj = australia.objects.all()
        obtab = team1_bowling.objects.all()
        s1 = obj.get(id=pid1)
        s2 = obj.get(id=pid2)
        p1 = s1.name
        p2 = s2.name
        


        
        
        

        
        
        if  request.POST['runs'] == '':
            runs= 0
        else:
            runs = int(request.POST['runs'])
            score += runs
          
        
            
        covers = round(float(covers),1)

        if covers == 0.5 :
            if request.POST['rc'] != 'wide' and request.POST['rc'] != 'no ball' and request.POST['rc'] != 'over throw':
                covers = 1
                b1 = b2 = b3 = b4 = b5 = b6 = ' '
            
        elif covers == 1.5:
            if request.POST['rc'] != 'wide' and request.POST['rc'] != 'no ball' and request.POST['rc'] != 'over throw':
                covers = 2
                b1 = b2 = b3 = b4 = b5 = b6 = ' '
        elif covers == 2.5:
            if request.POST['rc'] != 'wide' and request.POST['rc'] != 'no ball' and request.POST['rc'] != 'over throw':
                covers = 3
                b1 = b2 = b3 = b4 = b5 = b6 = ' '
        elif covers == 3.5:
            if request.POST['rc'] != 'wide' and request.POST['rc'] != 'no ball' and request.POST['rc'] != 'over throw':
                covers = 4
                b1 = b2 = b3 = b4 = b5 = b6 = ' '
        elif covers == 4.5:
            if request.POST['rc'] != 'wide' and request.POST['rc'] != 'no ball' and request.POST['rc'] != 'over throw':
                covers = 5
                b1 = b2 = b3 = b4 = b5 = b6 = ' '
        elif covers == 5.5:
            if request.POST['rc'] != 'wide' and request.POST['rc'] != 'no ball' and request.POST['rc'] != 'over throw':
                covers = 6
                b1 = b2 = b3 = b4 = b5 = b6 = ' '
        elif covers == 6.6:
            if request.POST['rc'] != 'wide' and request.POST['rc'] != 'no ball' and request.POST['rc'] != 'over throw':
                covers = 7
                b1 = b2 = b3 = b4 = b5 = b6 = ' '
        elif covers == 7.7:
            if request.POST['rc'] != 'wide' and request.POST['rc'] != 'no ball' and request.POST['rc'] != 'over throw':
                covers = 8
                b1 = b2 = b3 = b4 = b5 = b6 = ' '
        elif covers == 8.9:
            if request.POST['rc'] != 'wide' and request.POST['rc'] != 'no ball' and request.POST['rc'] != 'over throw':
                covers = 9
                b1 = b2 = b3 = b4 = b5 = b6 = ' '
        elif covers == 9.9:
            if request.POST['rc'] != 'wide' and request.POST['rc'] != 'no ball' and request.POST['rc'] != 'over throw':
                covers = 10
                b1 = b2 = b3 = b4 = b5 = b6 = ' '
        else:
            if request.POST['rc'] == 'wide' and request.POST['rc'] == 'no ball' and request.POST['rc'] != 'over throw':
                covers = round(covers,1)
            else:
                if request.POST['rc'] != 'wide' and request.POST['rc'] != 'no ball' and request.POST['rc'] != 'over throw':
                    covers = round(covers + 0.1,1)


        
        wc = request.POST['wc']

        if covers == 0:
            if request.POST['rc'] == 'over throw':
                b1 = 'ot'
            elif wc == 'none' and request.POST['rc'] != 'wide' and request.POST['rc'] != 'no ball':  
                b1 = runs
            elif request.POST['rc'] == 'wide':
                b1 = 'wd'
            elif request.POST['rc'] == 'no ball':
                b1 = 'nb'
            
            elif request.POST['wc'] == 'striker' or request.POST['wc'] == 'non striker':
                b1 = 'ro'
            else:
                b1 = 'w'

        
        if covers == 0.1 or covers == 1.1 or covers == 2.1 or covers == 3.1 or covers == 4.1 or covers == 5.1 or covers == 6.1 or covers == 7.1 or covers == 8.1 or covers == 9.1  :
            if request.POST['rc'] == 'over throw':
                b1 = 'ot'
            elif wc == 'none' and request.POST['rc'] != 'wide' and request.POST['rc'] != 'no ball':  
                b1 = runs
            elif request.POST['rc'] == 'wide':
                b2 = 'wd'
            elif request.POST['rc'] == 'no ball':
                b2 = 'nb'
            
            elif request.POST['wc'] == 'striker' or request.POST['wc'] == 'non striker':
                b2 = 'ro'
            else:
                b1 = 'w'
        elif covers == 0.2 or covers == 1.2 or covers == 2.2 or covers == 3.2 or covers == 4.2 or covers == 5.2 or covers == 6.2 or covers == 7.2 or covers == 8.2 or covers == 9.2  :
            if request.POST['rc'] == 'over throw':
                b2 = 'ot'
            elif wc == 'none' and request.POST['rc'] != 'wide' and request.POST['rc'] != 'no ball':  
                b2 = runs
            elif request.POST['rc'] == 'wide':
                b3 = 'wd'
            elif request.POST['rc'] == 'no ball':
                b3 = 'nb'
            
            elif request.POST['wc'] == 'striker' or request.POST['wc'] == 'non striker':
                b3 = 'ro'
            else:
                b2 = 'w'
        elif covers == 0.3 or covers == 1.3 or covers == 2.3 or covers == 3.3 or covers == 4.3 or covers == 5.3 or covers == 6.3 or covers == 7.3 or covers == 8.3 or covers == 9.3 :
            if request.POST['rc'] == 'over throw':
                b3 = 'ot'
            elif wc == 'none' and request.POST['rc'] != 'wide' and request.POST['rc'] != 'no ball':  
                b3 = runs
            elif request.POST['rc'] == 'wide':
                b4 = 'wd'
            elif request.POST['rc'] == 'no ball':
                b4 = 'nb'
            
            elif request.POST['wc'] == 'striker' or request.POST['wc'] == 'non striker':
                b4 = 'ro'
            else:
                b3 = 'w'
        elif covers == 0.4 or covers == 1.4 or covers == 2.4 or covers == 3.4 or covers == 4.4 or covers == 5.4 or covers == 6.4 or covers == 7.4 or covers == 8.4 or covers == 9.4  :
            if request.POST['rc'] == 'over throw':
                b4 = 'ot'
            elif wc == 'none' and request.POST['rc'] != 'wide' and request.POST['rc'] != 'no ball':  
                b4 = runs
            elif request.POST['rc'] == 'wide':
                b5 = 'wd'
            elif request.POST['rc'] == 'no ball':
                b5 = 'nb'
            
            elif request.POST['wc'] == 'striker' or request.POST['wc'] == 'non striker':
                b5 = 'ro'
            else:
                b4 = 'w'
        elif covers == 0.5 or covers == 1.5 or covers == 2.5 or covers == 3.5 or covers == 4.5 or covers == 5.5 or covers == 6.5 or covers == 7.5 or covers == 8.5 or covers == 9.5  :
            if request.POST['rc'] == 'over throw':
                b5 = 'ot'
            elif wc == 'none' and request.POST['rc'] != 'wide' and request.POST['rc'] != 'no ball':  
                b5 = runs
            elif request.POST['rc'] == 'wide':
                b6 = 'wd'
            elif request.POST['rc'] == 'no ball':
                b6 = 'nb'
            
            elif request.POST['wc'] == 'striker' or request.POST['wc'] == 'non striker':
                b6 = 'ro'
            else:
                b5 = 'w'
        
        
        


        ind = india.objects.all()
        aus = australia.objects.all()

        obt1ba = team2_batting.objects.all()
        obt2ba = team1_batting.objects.all()

        obt1bo = team2_bowling.objects.all()
        obt2bo = team1_bowling.objects.all()


        

        
        
        if request.POST['wc'] == 'none' or request.POST['rc'] == 'no ball':
            s1 = obj.get(id=pid1)
            s2 = obj.get(id=pid2)
            p1 = s1.name
            p2 = s2.name

            ob1 = obt1ba.get(id=pid1)
            ob2 = obt1ba.get(id=pid2)
            

            if sp1 == '*':
        
                obow = obt2bo.get(id = stbow)
                if request.POST['rc'] == 'runs':
                    ob1.runs += runs
                    ob1.balls += 1

                elif request.POST['rc'] == 'leg bye':
                    ob1.balls += 1

                elif request.POST['rc'] == 'wide':
                    obow.runs += 1
                    score += 1

                elif request.POST['rc'] == 'no ball':
                    ob1.runs += runs
                    obow.runs += 1
                    score += 1

                elif request.POST['rc'] == 'over throw':
                    ob1.runs += runs
                    

        
                    
                    

                if obow.overs == 0.5:
                    if request.POST['rc'] == 'runs' or request.POST['rc'] == 'leg bye':
                        obow.overs = 1
                        bowo = round(round(obow.overs,1),1)
                        stbow += 1
                else:
                    if request.POST['rc'] == 'runs' or request.POST['rc'] == 'leg bye' :
                        obow.overs += round(round(0.1,1),1)
                        bowo = round(round(obow.overs,1),1)


                obow.runs += runs
                
            
                indba = ind.get(id = pid1)
                indba.runs += runs

            
                obow.save()
                ob1.save()
                indba.save()

                op1b = ob1.balls
                op1r = ob1.runs


                tbr =  obtab.get(id = stbow)  #For Bowler Runs and  Wickets
                bowr = tbr.runs
                boww = tbr.wickets


            else:

            
                obow = obt2bo.get(id = stbow)
                if request.POST['rc'] == 'runs':
                    ob2.runs += runs
                    ob2.balls += 1

                elif request.POST['rc'] == 'leg bye':
                    ob2.balls += 1

                elif request.POST['rc'] == 'wide':
                    obow.runs += 1
                    score += 1

                elif request.POST['rc'] == 'no ball':
                    ob2.runs += runs
                    obow.runs += 1
                    score += 1

                elif request.POST['rc'] == 'over throw':
                    ob2.runs += runs
                   
                    
                    

                if obow.overs == 0.5:
                    if request.POST['rc'] == 'runs' or request.POST['rc'] == 'leg bye' :
                        obow.overs = 1
                        bowo = round(round(obow.overs,1),1)
                        stbow += 1
                else:
                    if request.POST['rc'] == 'runs' or request.POST['rc'] == 'leg bye' :
                        obow.overs += round(round(0.1,1),1)
                        bowo = round(round(obow.overs,1),1)


                obow.runs += runs
                
            
                indba = ind.get(id = pid1)
                indba.runs += runs

            
                obow.save()
                ob2.save()
                indba.save()

                op2b = ob2.balls
                op2r = ob2.runs


                tbr =  obtab.get(id = stbow)  #For Bowler Runs and  Wickets
                bowr = tbr.runs
                boww = tbr.wickets
                
            
        
                
        elif  request.POST['wc'] == 'bold' and request.POST['rc'] != 'no ball':

            if sp1 == '*':
                wc = request.POST['wc']
                ob1 = obt1ba.get(id=pid1)
                obow = obt2bo.get(id = stbow)
                ob1.balls += 1
                ob1.bowler = bowler
                ob1.wicket = wc
                if obow.overs == 0.5:
                    obow.overs = 1
                    bowo = round(round(obow.overs,1),1)
                    if request.POST['rc'] != 'no ball':
                        stbow += 1
                else:
                    
                    obow.overs += round(round(0.1,1),1)
                    bowo = round(round(obow.overs,1),1)
                obow.runs += runs
                obow.wickets += 1
            
                indba = ind.get(id = pid1)
                indba.runs += runs
                obow.save()
                ob1.save()
                indba.save()
        
                wickets += 1 
            
            
                gone += 1
                pid1 = gone
                ob1 = obt1ba.get(id=pid1)
                striker = ob1.name
                op1b = 0
                op1r = 0
            

            
                ob1.save()
                obow.save()
                indba.save()


                
                tbr =  obtab.get(id = stbow)  #For Bowler Runs and  Wickets
                bowr = tbr.runs
                boww = tbr.wickets
                
            else:
                wc = request.POST['wc']
                ob2 = obt1ba.get(id=pid2)
                obow = obt2bo.get(id = stbow)
                ob2.balls += 1
                ob2.bowler = bowler
                ob2.wicket = wc
                if obow.overs == 0.5:
                    obow.overs = 1
                    bowo = round(round(obow.overs,1),1)
                    if request.POST['rc'] != 'no ball':
                        stbow += 1
                else:
                    
                    obow.overs += round(round(0.1,1),1)
                    bowo = round(round(obow.overs,1),1)
                obow.runs += runs
                obow.wickets += 1
            
                indba = ind.get(id = pid1)
                indba.runs += runs
                obow.save()
                ob2.save()
                indba.save()
        
                wickets += 1 
            
            
                gone += 1
                pid2 = gone
                ob2 = obt1ba.get(id=pid2)
                non_striker = ob2.name
                op2b = 0
                op2r = 0
            

            
                ob2.save()
                obow.save()
                indba.save()



                
                tbr =  obtab.get(id = stbow)  #For Bowler Runs and  Wickets
                bowr = tbr.runs
                boww = tbr.wickets
                

        elif request.POST['wc'] == 'lbw' and request.POST['rc'] != 'no ball':
            
            if sp1 == '*':
                wc = request.POST['wc']
                ob1 = obt1ba.get(id=pid1)
                obow = obt2bo.get(id = stbow)
                ob1.balls += 1
                ob1.bowler = bowler
                ob1.wicket = wc
                if obow.overs == 0.5:
                    obow.overs = 1
                    bowo = round(round(obow.overs,1),1)
                    if request.POST['rc'] != 'no ball':
                        stbow += 1
                else:
                    
                    obow.overs += round(round(0.1,1),1)
                    bowo = round(round(obow.overs,1),1)
                obow.runs += runs
                obow.wickets += 1
            
                indba = ind.get(id = pid1)
                indba.runs += runs
                obow.save()
                ob1.save()
                indba.save()
        
                wickets += 1 
            
            
                gone += 1
                pid1 = gone
                ob1 = obt1ba.get(id=pid1)
                striker = ob1.name
                op1b = 0
                op1r = 0
            

            
                ob1.save()
                obow.save()
                indba.save()



                
                tbr =  obtab.get(id = stbow)  #For Bowler Runs and  Wickets
                bowr = tbr.runs
                boww = tbr.wickets
                
            else:
                wc = request.POST['wc']
                ob2 = obt1ba.get(id=pid2)
                obow = obt2bo.get(id = stbow)
                ob2.balls += 1
                ob2.bowler = bowler
                ob2.wicket = wc
                if obow.overs == 0.5:
                    obow.overs = 1
                    bowo = round(round(obow.overs,1),1)
                    if request.POST['rc'] != 'no ball':
                        stbow += 1
                else:
                    
                    obow.overs += round(round(0.1,1),1)
                    bowo = round(round(obow.overs,1),1)
                obow.runs += runs
                obow.wickets += 1
            
                indba = ind.get(id = pid1)
                indba.runs += runs
                obow.save()
                ob2.save()
                indba.save()
        
                wickets += 1 
            
            
                gone += 1
                pid2 = gone
                ob2 = obt1ba.get(id=pid2)
                non_striker = ob2.name
                op2b = 0
                op2r = 0
            

            
                ob2.save()
                obow.save()
                indba.save()




                
                tbr =  obtab.get(id = stbow)  #For Bowler Runs and  Wickets
                bowr = tbr.runs
                boww = tbr.wickets

        elif request.POST['wc'] == 'catch' and request.POST['rc'] != 'no ball':
            
            if sp1 == '*':
                wc = request.POST['wc']
                ob1 = obt1ba.get(id=pid1)
                obow = obt2bo.get(id = stbow)
                ob1.balls += 1
                ob1.bowler = bowler
                ob1.wicket = wc
                if obow.overs == 0.5:
                    obow.overs = 1
                    bowo = round(round(obow.overs,1),1)
                    if request.POST['rc'] != 'no ball':
                        stbow += 1
                else:   
                    obow.overs += round(round(0.1,1),1)
                    bowo = round(round(obow.overs,1),1)
                obow.runs += runs
                obow.wickets += 1
            
                indba = ind.get(id = pid1)
                indba.runs += runs
                obow.save()
                ob1.save()
                indba.save()
        
                wickets += 1 
            
            
                gone += 1
                pid1 = gone
                ob1 = obt1ba.get(id=pid1)
                striker = ob1.name
                op1b = 0
                op1r = 0
            

            
                ob1.save()
                obow.save()
                indba.save()




                
                tbr =  obtab.get(id = stbow)  #For Bowler Runs and  Wickets
                bowr = tbr.runs
                boww = tbr.wickets
                
            else:
                wc = request.POST['wc']
                ob2 = obt1ba.get(id=pid2)
                obow = obt2bo.get(id = stbow)
                ob2.balls += 1
                ob2.bowler = bowler
                ob2.wicket = wc
                if obow.overs == 0.5:
                    obow.overs = 1
                    bowo = round(round(obow.overs,1),1)
                    if request.POST['rc'] != 'no ball':
                        stbow += 1
                else:
                    
                        
                    obow.overs += round(round(0.1,1),1)
                    bowo = round(round(obow.overs,1),1)
                obow.runs += runs
                obow.wickets += 1
            
                indba = ind.get(id = pid1)
                indba.runs += runs
                obow.save()
                ob2.save()
                indba.save()
        
                wickets += 1 
            
            
                gone += 1
                pid2 = gone
                ob2 = obt1ba.get(id=pid2)
                non_striker = ob2.name
                op2b = 0
                op2r = 0
            

            
                ob2.save()
                obow.save()
                indba.save()




                
                tbr =  obtab.get(id = stbow)  #For Bowler Runs and  Wickets
                bowr = tbr.runs
                boww = tbr.wickets

        elif request.POST['wc'] == 'striker' :
            
            if sp1 == '*':
                wc = request.POST['wc']
                ob1 = obt1ba.get(name = striker)
                obow = obt2bo.get(id = stbow)
                ob1.balls += 1
                ob1.bowler = bowler
               
                if obow.overs == 0.5:
                    obow.overs = 1
                    bowo = round(round(obow.overs,1),1)
                    stbow += 1
                else:
                    
                    obow.overs += round(round(0.1,1),1)
                    bowo = round(round(obow.overs,1),1)
                obow.runs += runs
                
            
                indba = ind.get(id = pid1)
                indba.runs += runs
                obow.save()
                ob1.save()
                indba.save()
        
                wickets += 1 
            
            
                gone += 1
                pid1 = gone
                ob1 = obt1ba.get(id=pid1)
                striker = ob1.name
                op1b = 0
                op1r = 0
            

            
                ob1.save()
                obow.save()
                indba.save()




                
                tbr =  obtab.get(id = stbow)  #For Bowler Runs and  Wickets
                bowr = tbr.runs
                boww = tbr.wickets

            else:
                wc = request.POST['wc']
                ob2 = obt1ba.get(name = striker)
                obow = obt2bo.get(id = stbow)
                ob2.balls += 1
                ob2.bowler = bowler
                ob2.wicket = wc
                if obow.overs == 0.5:
                    obow.overs = 1
                    bowo = round(round(obow.overs,1),1)
                    stbow += 1
                else:
                    obow.overs += round(round(0.1,1),1)
                    bowo = round(round(obow.overs,1),1)
                obow.runs += runs
                
            
                indba = ind.get(id = pid1)
                indba.runs += runs
                obow.save()
                ob2.save()
                indba.save()
        
                wickets += 1 
            
            
                gone += 1
                pid2 = gone
                ob2 = obt1ba.get(id=pid2)
                striker = ob2.name
                op2b = 0
                op2r = 0
            

            
                ob2.save()
                obow.save()
                indba.save()


                
                tbr =  obtab.get(id = stbow)  #For Bowler Runs and  Wickets
                bowr = tbr.runs
                boww = tbr.wickets
                
            
        elif request.POST['wc'] == 'non striker':
            if sp2 == ' ':
                wc = request.POST['wc']
                ob2 = obt1ba.get(name = non_striker)
                obow = obt2bo.get(id = stbow)
                ob2.balls += 1
                ob2.bowler = bowler
               
                if obow.overs == 0.5:
                    obow.overs = 1
                    bowo = round(round(obow.overs,1),1)
                    stbow += 1
                else:
                    
                    obow.overs += round(round(0.1,1),1)
                    bowo = round(round(obow.overs,1),1)
                obow.runs += runs
                
            
                indba = ind.get(id = pid1)
                indba.runs += runs
                obow.save()
                ob2.save()
                indba.save()
        
                wickets += 1 
            
            
                gone += 1
                pid2 = gone
                ob2 = obt1ba.get(id=pid2)
                non_striker = ob2.name
                op2b = 0
                op2r = 0
            

            
                ob2.save()
                obow.save()
                indba.save()




                
                tbr =  obtab.get(id = stbow)  #For Bowler Runs and  Wickets
                bowr = tbr.runs
                boww = tbr.wickets
            
            else:
                wc = request.POST['wc']
                ob1 = obt1ba.get(name = non_striker)
                obow = obt2bo.get(id = stbow)
                ob1.balls += 1
                ob1.bowler = bowler
                ob1.wicket = wc
                if obow.overs == 0.5:
                    obow.overs = 1
                    bowo = round(round(obow.overs,1),1)
                    stbow += 1
                else:
                    obow.overs += round(round(0.1,1),1)
                    bowo = round(round(obow.overs,1),1)
                obow.runs += runs
                
            
                indba = ind.get(id = pid1)
                indba.runs += runs
                obow.save()
                ob1.save()
                indba.save()
        
                wickets += 1 
            
            
                gone += 1
                pid1 = gone
                ob1 = obt1ba.get(id=pid1)
                striker = ob1.name
                op1b = 0
                op1r = 0
            

            
                ob1.save()
                obow.save()
                indba.save()


                
                tbr =  obtab.get(id = stbow)  #For Bowler Runs and  Wickets
                bowr = tbr.runs
                boww = tbr.wickets
                
            
                
        
        temp = obtab.get(id = stbow)
        bowler = temp.name


        
        bowo = round(round(temp.overs,1),1)
        


        s1 = obj.get(id=pid1)
        s2 = obj.get(id=pid2)
        p1 = s1.name
        p2 = s2.name


                      #For Changing Bowler After Over Completed....


        if runs == 0 and request.POST['wc'] == 'none':          #For Rotating Strike....
            if sp1 == '*' :  
                if covers == 1 or covers == 2  or covers == 3 or covers == 4 or covers == 5 or covers == 6 or covers == 7 or covers == 8 or covers == 9 or covers == 10 :
                    sp1 = ' '
                    sp2 = '*'
                   
                    
                else:
                    sp1 = '*'
                    sp2 = ' '
            elif sp1 == '*' :  
                if covers == 1 or covers == 2  or covers == 3 or covers == 4 or covers == 5 or covers == 6 or covers == 7 or covers == 8 or covers == 9 or covers == 10 :
                    sp1 = '*'
                    sp2 = ' '
                   
                
                else:
                    sp1 = ' '
                    sp2 = '*'
                
        
            return render(request,'delete2.html',{'team1':team1,'team2':team2,'overs':overs,'score':score,'wickets':wickets,'covers':covers,'bowler':bowler,'striker':striker,'non_striker':non_striker,'pid1':pid1,'pid2':pid2,'gone':gone,'stbow':stbow,'op1r':op1r,'op2r':op2r,'op1b':op1b,'op2b':op2b,'b1':b1,'b2':b2,'b3':b3,'b4':b4,'b5':b5,'b6':b6,'sp1':sp1,'sp2':sp2, 'bowo':bowo  ,'bowr':bowr,'boww':boww })

        if runs == 0 and request.POST['wc'] != 'none':          #For Rotating Strike....
            if sp1 == '*' :  
                if covers == 1 or covers == 2  or covers == 3 or covers == 4 or covers == 5 or covers == 6 or covers == 7 or covers == 8 or covers == 9 or covers == 10 :
                    sp1 = ' '
                    sp2 = '*'
                   
                    
                else:
                    sp1 = '*'
                    sp2 = ' '
            elif sp2 == '*' :  
                if covers == 1 or covers == 2  or covers == 3 or covers == 4 or covers == 5 or covers == 6 or covers == 7 or covers == 8 or covers == 9 or covers == 10 :
                    sp1 = '*'
                    sp2 = ' '
                   
                
                else:
                    sp1 = ' '
                    sp2 = '*'
                
        
            return render(request,'delete2.html',{'team1':team1,'team2':team2,'overs':overs,'score':score,'wickets':wickets,'covers':covers,'bowler':bowler,'striker':striker,'non_striker':non_striker,'pid1':pid1,'pid2':pid2,'gone':gone,'stbow':stbow,'op1r':op1r,'op2r':op2r,'op1b':op1b,'op2b':op2b,'b1':b1,'b2':b2,'b3':b3,'b4':b4,'b5':b5,'b6':b6,'sp1':sp1,'sp2':sp2, 'bowo':bowo ,'bowr':bowr,'boww':boww })

    

        if runs == 1 or runs == 3 :          #For Rotating Strike....
            if sp1 == '*' :  
                if covers == 1 or covers == 2  or covers == 3 or covers == 4 or covers == 5 or covers == 6 or covers == 7 or covers == 8 or covers == 9 or covers == 10 :
                    sp1 = '*'
                    sp2 = ' '
                    
                    
                else:
                    sp1 = ' '
                    sp2 = '*'
                    
            elif sp2 == '*' :  
                if covers == 1 or covers == 2  or covers == 3 or covers == 4 or covers == 5 or covers == 6 or covers == 7 or covers == 8 or covers == 9 or covers == 10 :
                    sp1 = ' '
                    sp2 = '*'
                
                else:
                    sp1 = '*'
                    sp2 = ' '
                    
                
        
            return render(request,'delete2.html',{'team1':team1,'team2':team2,'overs':overs,'score':score,'wickets':wickets,'covers':covers,'bowler':bowler,'striker':striker,'non_striker':non_striker,'pid1':pid1,'pid2':pid2,'gone':gone,'stbow':stbow,'op1r':op1r,'op2r':op2r,'op1b':op1b,'op2b':op2b,'b1':b1,'b2':b2,'b3':b3,'b4':b4,'b5':b5,'b6':b6,'sp1':sp1,'sp2':sp2,'bowo':bowo ,'bowr':bowr,'boww':boww })
    

        elif runs == 2 or runs == 4 or runs == 6:
            if sp1 == '*' :
                if covers == 1 or covers == 2  or covers == 3 or covers == 4 or covers == 5 or covers == 6 or covers == 7 or covers == 8 or covers == 9 or covers == 10 :
                    sp1 = ' '
                    sp2 = '*'
                   
                else:
                    sp1 = '*'
                    sp2 = ' '
            elif sp2 == '*' :
                if covers == 1 or covers == 2  or covers == 3 or covers == 4 or covers == 5 or covers == 6 or covers == 7 or covers == 8 or covers == 9 or covers == 10 :
                    sp1 = '*'
                    sp2 = ' '
                   
                
                else:
                    sp1 = ' '
                    sp2 = '*'

            return render(request,'delete2.html',{'team1':team1,'team2':team2,'overs':overs,'score':score,'wickets':wickets,'covers':covers,'bowler':bowler,'striker':striker,'non_striker':non_striker,'pid1':pid1,'pid2':pid2,'gone':gone,'stbow':stbow,'op1r':op1r,'op2r':op2r,'op1b':op1b,'op2b':op2b,'b1':b1,'b2':b2,'b3':b3,'b4':b4,'b5':b5,'b6':b6,'sp1':sp1,'sp2':sp2,'bowo':bowo ,'bowr':bowr,'boww':boww })

        return render(request,'delete2.html',{'team1':team1,'team2':team2,'overs':overs,'score':score,'wickets':wickets,'covers':covers,'bowler':bowler,'striker':striker,'non_striker':non_striker,'pid1':pid1,'pid2':pid2,'gone':gone,'stbow':stbow,'op1r':op1r,'op2r':op2r,'op1b':op1b,'op2b':op2b,'b1':b1,'b2':b2,'b3':b3,'b4':b4,'b5':b5,'b6':b6,'sp1':sp1,'sp2':sp2,'bowo':bowo,'bowr':bowr,'boww':boww })


def delete(request):
    team1 = request.POST['dropdown']
    team2 = request.POST['dropdown2']

    if team1 == 'india':
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
        gone = 2
        obt1ba = team1_batting.objects.all()
        obt2ba = team2_batting.objects.all()

        obt1bo = team1_bowling.objects.all()
        obt2bo = team2_bowling.objects.all()


        obp1 = obt1ba.get(id=pid1)
        obp2 = obt1ba.get(id=pid2)

        op1r = obp1.runs
        op2r = obp2.runs

        op1b = obp1.balls
        op2b = obp2.balls

        stbow = 7

        b1 = ' '
        b2 = ' '
        b3 = ' '
        b4 = ' '
        b5 = ' '
        b6 = ' '
    

        sp1 = '*'
        sp2 = ' '




        tempbo  = obt2bo.get(id = stbow)
        bowo = round(round(tempbo.overs,1),1)
        bowr = tempbo.runs
        boww = tempbo.wickets
    

    

    
    
        check1 = request.POST['c1']


        ob2 =australia.objects.all()
        temp = ob2.get(id=7)
        bowler = temp.name
        
           
        
        if check1 == 'c1':
            overs = 5
        else:
            overs = 2

        return render(request,'delete.html',{'team1':team1,'team2':team2,'overs':overs,'score':score,'wickets':wickets,'covers':covers,'bowler':bowler,'striker':striker,'non_striker':non_striker,'pid1':pid1,'pid2':pid2,'gone':gone,'stbow':stbow,'op1r':op1r,'op2r':op2r,'op1b':op1b,'op2b':op2b,'b1':b1,'b2':b2,'b3':b3,'b4':b4,'b5':b5,'b6':b6,'sp1':sp1,'sp2':sp2,'bowo':bowo,'bowr':bowr,'boww':boww })

    

    if team1 == 'australia':
        obj = australia.objects.all()
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
        gone = 2
        obt1ba = team1_batting.objects.all()
        obt2ba = team2_batting.objects.all()

        obt1bo = team1_bowling.objects.all()
        obt2bo = team2_bowling.objects.all()


        obp1 = obt1ba.get(id=pid1)
        obp2 = obt1ba.get(id=pid2)

        op1r = obp1.runs
        op2r = obp2.runs

        op1b = obp1.balls
        op2b = obp2.balls

        stbow = 7

        b1 = ' '
        b2 = ' '
        b3 = ' '
        b4 = ' '
        b5 = ' '
        b6 = ' '
    

        sp1 = '*'
        sp2 = ' '




        tempbo  = obt2bo.get(id = stbow)
        bowo = round(round(tempbo.overs,1),1)
        bowr = tempbo.runs
        boww = tempbo.wickets
    

    

    
    
        check1 = request.POST['c1']


        
        ob2 =australia.objects.all()
        temp = ob2.get(id=7)
        bowler = temp.name
        
        
        if check1 == 'c1':
            overs = 5
        else:
            overs = 2

        return render(request,'delete2.html',{'team1':team1,'team2':team2,'overs':overs,'score':score,'wickets':wickets,'covers':covers,'bowler':bowler,'striker':striker,'non_striker':non_striker,'pid1':pid1,'pid2':pid2,'gone':gone,'stbow':stbow,'op1r':op1r,'op2r':op2r,'op1b':op1b,'op2b':op2b,'b1':b1,'b2':b2,'b3':b3,'b4':b4,'b5':b5,'b6':b6,'sp1':sp1,'sp2':sp2,'bowo':bowo,'bowr':bowr,'boww':boww })




def allemployes(request):

    obj = employe.objects.all()
    return render(request,'allemployes.html',{'obj':obj})


def insert(request):

    ob = employe()
    return render(request,'insert.html')