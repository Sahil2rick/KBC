import time
print('WELCOME IN THE WORLD OF QUESTIONS')
time.sleep(2)
print()
print()
print('RULE 1: There is 15+1 questions')
print('''                            !!!!!7 crore!!!!!!
                          -------1 crore--------
                         --------50 lakh----------
                        ---------25 lakh------------
                      ----------12,50,000-------------
                    -------------6,40,000----------------
                  **************3,20,000*******************
                ----------------1,60,000---------------------
              -------------------80,000-------------------------
            ---------------------40,000---------------------------
          -----------------------20,000-----------------------------
        *************************10,000*******************************
      ----------------------------5,000---------------------------------
    ------------------------------3,000-----------------------------------
  --------------------------------2,000-------------------------------------
----------------------------------1,000--------------------------------------- ''')
print()
print()
print()
print()
print()
print()
print()
print()
print()
time.sleep(5)
print('* There will be 45s for first 5 question')
print('* There will be 60s for next 5 question')
print('* There will be no time limit for last 5 question')
time.sleep(2)
print()
print()
print()
print()
print("If you need life line press 'L'")
print("press 'q 'for quit")
print()
print()
print()
print()
print()
print()
print('so..... lets start the game')
time.sleep(2)
print()
x='1(audience poll)'
y='2(50:50)'
z='3(expert advice)'
w='4(replace the question)'
ll=[x,y,z,w]
print('FIRST QUESTION')
time.sleep(2)
print()
print('Q1 who has the maximum seat in PM election held recently in 2019')
print('(a) NDA')
print('(b) BJP')      
print('(c) CONG')
print('(d) UPA')
a=input('enter the option') 
if a=='a':
    print('correct option.you have won 1000 ruppes')
elif a.lower()=='l':
    print(ll)
    for i in range(4):
     opt=int(input('enter lifeline option no.(if any further life is needed or not)press 0 for no other lifeline'))
     if opt==1 :
        print('(a)66%,(b)27%,(c)7%,(d)0%')
        a=input('enter the option')
        ll.remove(x)
     if opt==2:
        print("options 'a' and 'b' remains")
        a=input('enter the option')
        ll.remove(y)
     if opt==4:
        print('Q1 1 dozen is equal to')
        print('(a) 12')
        print('(b) 6')      
        print('(c) 1')
        print('(d) 10')
        a=input('enter the option')
        ll.remove(w)
     if opt==3:
        print('a is correct option')
        ll.remove(z)
     if opt==0:
         break
         a=input('enter the option')
elif a.lower()=='q':
   print('THANKS FOR PLAYING YOU WON 0 ruppes')
if a=='a':
    print()
    print()
    print('SECOND QUESTION')
    print()
    print('Q2 what is the weight of any body at centre of earth')
    print('(a) equal to radius of earth')
    print('(b) 0')
    print("(c) equal to its mass ")
    print('(d) infitity')
    print()
    b=input('enter the option')
    
    if b=='b':  
        print('correct option.you have won 2000 ruppes')
    elif b.lower()=='l':   
     print(ll)
     for i in range(4):
      opt=int(input('enter option no.'))
      if opt==1 :
        print('(a)6%,(b)77%,(c)7%,(d)10%')
        b=input('enter the option')
        ll.remove(x)
      if opt==2:
        print("options 'a' and 'b' remains")
        b=input('enter the option')
        ll.remove(y)
      if opt==4:
         print('Q2 1 dozen is equal to')
         print('(a) 6')
         print('(b) 12')      
         print('(c) 1')
         print('(d) 10')
         b=input('enter the option')
         ll.remove(w)
      if opt==3:
        print('b is correct option')
        ll.remove(z)
      if opt==0:
         break
         b=input('enter the option')
    elif a.lower()=='q':
     print('THANKS FOR PLAYING YOU WON 1000 ruppes')     
    if b=='b':
        print('correct answers')
    
        print()    
        print('THIRD QUESTION')    
        print()
        print('Q3 who discover electron,proton and neutron resp ')
        print('(a) rutherford,chadwick, thomson')
        print('(b) goldsten,chadwick,thomson')      
        print('(c) thomson,goldsten,chadwick')
        print('(d) bohr,chadwick,thomson')
        print()
        c=input('enter the option')
        if c=='c':
            print('correct option.you have won 3000 ruppes')
        elif c.lower()=='l':
         print(ll)
         for i in range(4):        
          opt=int(input('enter option no.'))
          if opt==1 :
           print('(a)16%,(b)27%,(c)51%,(d)6%')
           c=input('enter the option')
           ll.remove(x)       
          if opt==2:
           print("options 'c' and 'b' remains")
           c=input('enter the option')
           ll.remove(y)       
          if opt==4:
            print('Q3 which team has won the title maximum and how many')
            print('(a) MI-3')
            print('(b) CSK-4')      
            print('(c) MI-4')
            print('(d) CSK-3')
            c=input('enter the option') 
            ll.remove(w)
          if opt==3:
            print('c is correct option')
            ll.remove(z)
          if opt==0:
           break
           c=input('enter the option')
        elif a.lower()=='q':
                  print('THANKS FOR PLAYING YOU WON 2000 ruppes')   
        if c=='c':
            print('correct answers')
    
            print()
            print('FOURTH QUESTION')
            print()
            print('Q4 WHAT IS THE FULL FORM OF Ph.D')
            print('(a) PHILOSOPHY IN DOCTRATE')
            print('(b) DOCTOR OF PHILOSOPHY')      
            print('(c) PHILOSOPHY IN DOCTOR')
            print('(d) DOCTRATE OF PHILOSOPHY')
            print()
            d=input('enter the option')
            if d=='b':
               print('correct option.you have won 5000 ruppes')
            elif d.lower()=='l':
             print(ll)
             for i in range(4):   
               opt=int(input('enter option no.'))
               if opt==1 :
                print('(a)10%,(b)70%,(c)10%,(d)10%')
                d=input('enter the option')
                ll.remove(x)  
               if opt==2:
                  print("options 'a' and 'b' remains")
                  d=input('enter the option')
                  ll.remove(y)
               if opt==4:
                    print('Q4 which team has won the title maximum and how many')
                    print('(a) MI-3')
                    print('(b) MI-4')      
                    print('(c) CSK-4')
                    print('(d) CSK-3')
                    d=input('enter the option')
                    ll.remove(w)
               if opt==3:
                print('b is correct option')
                ll.remove(z)
               if opt==0:
                break
                d=input('enter the option')
            elif a.lower()=='q':
                            print('THANKS FOR PLAYING YOU WON 3000 ruppes')    
            if d=='b':
               print('correct answers')

               print()
               print('FIFTH QUESTION')
               print()
               print('Q5 FIND WHICH COMES NEXT? AGMJ,UHDN,CIOL,????')
               print('(a) BJJK')
               print('(b) NJMK')      
               print('(c) QWER')
               print('(d) WJFP')
               print()
               e=input('enter the option')
               if e=='d':
                  print('correct option.you have won 10,000 paise')
               elif e.lower()=='l':
                 print(ll)
                 for i in range(4):
                  opt=int(input('enter option no.'))
                  if opt==1 :
                   print('(a)6%,(b)17%,(c)17%,(d)60%')
                   e=input('enter the option')
                   ll.remove(x)
                  if opt==2:
                      print("options 'a' and 'd' remains")
                      e=input('enter the option')
                      ll.remove(y)
                  if opt==4:
                      print('Q5 which team has won the title maximum and how many')
                      print('(a) MI-3')
                      print('(b) CSK-3')      
                      print('(c) CSK-4')
                      print('(d) MI-4')
                      e=input('enter option')
                      ll.remove(w)
                  if opt==3:
                        print('d is correct option')
                        ll.remove(z)
                  if opt==0:
                     break
                     e=input('enter the option')
               elif a.lower()=='q':
                                  print('THANKS FOR PLAYING YOU WON 5000 ruppes')      
               if e=='d':
                  print('correct answers')
   
                  print()
                  print('SIXTH QUESTION')
                  print()
                  print('Q6 HOW MANY ELEMENTS DID PERIODIC TABLE HAVE?')
                  print('(a) 108')
                  print('(b) 118')      
                  print('(c) 136')
                  print('(d) 122')
                  print()
                  f=input('enter the option')
                  if f=='b':
                    print('correct option.you have won 20,000 ruppes')
                  elif f.lower()=='l':
                   print(ll)
                   for i in range(4):
                    opt=int(input('enter option no.'))
                    if opt==1 :
                      print('(a)25%,(b)27%,(c)25%,(d)23%')
                      f=input('enter the option')
                      ll.remove(x)
                    if opt==2:
                       print("options 'a' and 'b' remains")
                       f=input('enter the option')
                       ll.remove(y)
                    if opt==4:
                     print('Q6 which team has won the title maximum and how many')
                     print('(a) MI-3')
                     print('(b) MI-4')      
                     print('(c) CSK-4')
                     print('(d) CSK-3')
                     f=input('enter option')
                     ll.remove(w)
                    if opt==3:
                       print('b is correct option')
                       ll.remove(z)
                    if opt==0:
                     break
                     f=input('enter the option')
                  elif a.lower()=='q':
                                      print('THANKS FOR PLAYING YOU WON 10,000 ruppes')   
                  if f=='b':
                    print('correct answers')
  
                    print()
                    print('SEVENTH QUESTION')
                    print() 
                    print('Q7 ON WHICH DATE AND TIME 10TH RESULT CAME')
                    print('(a) 2TH MAY 12AM')
                    print('(b) 6TH MAY 3PM')      
                    print('(c) 6TH MAY 12AM')
                    print('(d) 2TH MAY 1PM')
                    print()
                    g=input('enter the option')
                    if g=='b':
                          print('correct option.you have won 40,000 ruppes')
                    elif g.lower()=='l':
                        print(ll)
                        for i in  range(4):
                           opt=int(input('enter option no.'))
                           if opt==1 :
                             print('(a)23%,(b)27%,(c)17%,(d)33%')
                             g=input('enter the option')
                             ll.remove(x)
                           if opt==2:
                              print("options 'a' and 'b' remains")
                              g=input('enter the option')
                              ll.remove(y)
                           if opt==4:
                             print('Q7 which team has won the title maximum and how many')
                             print('(a) MI-3')
                             print('(b) MI-4')      
                             print('(c) CSK-4')
                             print('(d) CSK-3')
                             g=input('enter option')
                             ll.remove(w)
                           if opt==3:
                              print('b is correct option')
                              ll.remove(z)
                           if opt==0:
                            break
                            g=input('enter the option')
                    elif a.lower()=='q':
                                print('THANKS FOR PLAYING YOU WON 20,000 ruppes')        
                    if g=='b':
                          print('correct answers')
      
                          print()    
                          print('EIGHTH QUESTION')    
                          print()
                          print('Q8 WHICH COUNTRY FLAG IS NOT RECTANGLE IN SHAPE ')
                          print('(a) ENGLAND')
                          print('(b) BERMUDA TRIANGLE')      
                          print('(c) NEPAL')
                          print('(d) ZIMBAWBE')
                          print()
                          H=input('enter the option')
                          if H=='c':
                              print('correct option.you have won 80,000 ruppes')
                          elif H.lower()=='l':
                             print(ll)
                             for i in range(4):
                               opt=int(input('enter option no.'))
                               if opt==1 :
                                print('(a)25%,(b)27%,(c)27%,(d)21%')
                                H=input('enter the option')
                                ll.remove(x)
                               if opt==2:
                                        print("options 'c' and 'b' remains")
                                        H=input('enter the option')
                                        ll.remove(y)
                               if opt==4:
                                     
                                     print('Q8 WHICH COUNTRY FLAG IS NOT RECTANGLE IN SHAPE ')
                                     print('(a) ENGLAND')
                                     print('(b) BERMUDA TRIANGLE')      
                                     print('(c) NEPAL')
                                     print('(d) ZIMBAWBE')
                                     print()
                                     print()
                                     print()
                                     print('HHHAAAAAAAAA LOL !!!!!!!!!!!!!!!!!')
                                     print()
                                     print()
                                     H=input('enter the option')
                                     ll.remove(w)
                                     time.sleep(2)
                               if opt==3:
                                   print('c is correct option')
                                   ll.remove(z)
                               if opt==0:
                                 break
                                 H=input('enter the option')
                          elif a.lower()=='q':
                                           print('THANKS FOR PLAYING YOU WON 40,000 ruppes')       
                          if H=='c':
                              print('correct answers')
    
                              print()
                              print('NINTH QUESTION')
                              print()
                              print('Q9 WHICH FOOTBALL CLUB HAS RECENTLY WON FA CUP ')
                              print('(a) BARCALONA')
                              print('(b) MAN CITY')      
                              print('(c) REAL MADRID')
                              print('(d) LIVERPOOL')
                              print()
                              I=input('enter the option')
                              if I=='b':
                                 print('correct option.you have won 1,60,000 ruppes')
                              elif I.lower()=='l':
                                print(ll)
                                for  i in range(4): 
                                 opt=int(input('enter option no.'))
                                 if opt==1 :
                                  print('(a)27%,(b)66%,(c)7%,(d)0%')
                                  I=input('enter the option')
                                  ll.remove(x)
                                 if opt==2:
                                   print("options 'a' and 'b' remains")
                                   I=input('enter the option')
                                   ll.remove(y)
                                 if opt==4:
                                      print('Q9 AKBAR WAS FATHER OF?')
                                      print('(a) SHAH JAHAN')
                                      print('(b) JAHAGIR')      
                                      print('(c) AURANZEEB')
                                      print('(d) BABAR')
                                      I=input('enter the option')
                                      ll.remove(w)
                                 if opt==3:
                                     print('b is correct option')
                                     ll.remove(z)
                                 if opt==0:
                                      break
                                      I=input('enter the option')
                              elif a.lower()=='q':
                                            print('THANKS FOR PLAYING YOU WON 80,000 ruppes')        
                              if I=='b':
                                 print('correct answers')
   
                                 print()
                                 print('TENTH QUESTION')
                                 print()
                                 print('Q10 which is more elastic')
                                 print('(a) steel')
                                 print('(b) rubber')      
                                 print('(c) same elasticity property')
                                 print('(d) didnot show elastic behavior at all')
                                 print()
                                 J=input('enter the option') 
                                 if J=='a':
                                      print('correct option.you have won 3,20,000 ruppes')
                                 elif J.lower()=='l':
                                     print(ll)
                                     for i in range(4):
                                      opt=int(input('enter option no.'))
                                      if opt==1 :
                                          print('(a)66%,(b)27%,(c)7%,(d)0%')
                                          J=input('enter the option')
                                          ll.remove(x)
                                      if opt==2:
                                            print("options 'a' and 'b' remains")
                                            J=input('enter the option')
                                            ll.remove(y)
                                      if opt==4:
                                           print('Q10 elastis behaviour depends upon')
                                           print('(a) ELASTIS FATIQUE')
                                           print('(b) young modulus')      
                                           print('(c) bulk modulus')
                                           print('(d) elastomers')
                                           J=input('enter the option')
                                           ll.remove(w)
                                      if opt==3:
                                          print('a is correct option')
                                          ll.remove(z)
                                      if opt==0:
                                           break
                                           J=input('enter the option')
                                 elif a.lower()=='q':
                                                   print('THANKS FOR PLAYING YOU WON 1,60,000 ruppes')            
                                 if J=='a':
                                      print('correct answers')
     
                                      print()
                                      print('CONGRATULATION!!!!!!! YOU HAVE WON THE MONEY 500 PAISE')
                                      print('THANK YOU FOR PLAYING MY KBC')
                                 else:
                                       print('INCORRECT ANSWER!!!!!!!!!!!')
                                       print('you are disqualified,10,000 ruppes')    

                              else:
                                 print('INCORRECT ANSWER!!!!!!!!!!!')
                                 print('you are disqualified,10,000 ruppes')    

                          else:
                            print('INCORRECT ANSWER!!!!!!!!!!!')
                            print('you are disqualified,10,000 ruppes')    

                    else:
                      print('INCORRECT ANSWER!!!!!!!!!!!')
                      print('you are disqualified,10,000 ruppes')    

                  else:
                     print('INCORRECT ANSWER!!!!!!!!!!!')
                     print('you are disqualified,10,000 ruppes')    

               else:
                   print('INCORRECT ANSWER!!!!!!!!!!!')
                   print('you are disqualified,0 ruppes')    

            else:
                print('INCORRECT ANSWER!!!!!!!!!!!')
                print('you are disqualified,0 ruppes')    

        else:
            print('INCORRECT ANSWER!!!!!!!!!!!')
            print('you are disqualified,0 ruppes')    
    else:
        print('INCORRECT ANSWER!!!!!!!!!!!')
        print('you are disqualified, 0 ruppes')    
else:
    print('INCORRECT ANSWER!!!!!!!!!!!')
    print('you are disqualified, 0 ruppes')
    
      
      

