import time

sec = int(input("Enter the no. of seconds = "))

def countdowntimer(sec):
   while sec > 0 :
        mins  = int(sec/60)
        secs = int(sec % 60) #modulo = %
        timer = "{:02d}:{:02d}".format(mins,secs)
    
        print(timer)
        time.sleep(1)
        sec -=1
    
   print("Time is up!!")
   
countdowntimer(sec)