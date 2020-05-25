"""
Created on Sun May 17 16:26:44 2020
@author: ISH KAPOOR
*************************************
#myTime[1]=hr.---myTime[0]*60*60=sec.
#myTime[1]=min.---myTime[1]*60=sec.
#mytime[2]=sec.
*************************************
"""
import time
import winsound

print("TIMER BY ISH KAPOOR")

def myAlarm():

    try:
        myTime = list(map(int, input("Enter time in 'hr.' 'min.' 'sec.'\n")))
        if len(myTime) == 3:
            total_seconds = myTime[0] * 60 * 60 + myTime[1] * 60 + myTime[2] #converting things into seconds and adding them
            if total_seconds == 1:
                print("Timer will Beep after", total_seconds ,"second")
            else:
                print("Timer will Beep after", total_seconds ,"seconds")
            time.sleep(total_seconds)
            frequency = 2500 #freq to 2500Hz
            duration = 1000 #duration is 1000m.sec. or 1sec.
            winsound.Beep(frequency, duration)
        else:
            print("Please enter time in correct format as mentioned\n")
            myAlarm()
    except Exception as e:
        print("This is the exception\n", e, "So! please enter correct details")
        myAlarm()
        
myAlarm()
