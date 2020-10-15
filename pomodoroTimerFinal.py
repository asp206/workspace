import time 
import datetime as date_time

import tkinter
from tkinter import messagebox
from tkinter import simpledialog
import winsound 
class pomTimer:
    def startTimer(self):
        #hide main window
        window = tkinter.Tk()
        window.withdraw()

        #empty pomodoro timer
        pomodoros = 0
        #get time information
        time_now = date_time.datetime.now() #time right now
        time_pom = 60*25 #pomodoro time
        delta_time = date_time.timedelta(0,time_pom) #time in delta mins
        time_future = time_now + delta_time #future time for planning and estimation
        delta_seconds = 1 
        time_final = time_now + date_time.timedelta(0,time_pom+delta_seconds) #time with 5 minute breaks

        #GUI Set up
        messagebox.showinfo("Pomodoro Started!", "\n Time is now" +time_now.strftime("%H:%M") + "hrs. \nTimer set for 25 mins.")
        while True:
            time.sleep(600) #checks for the timer every 10 minutes
            time_now = date_time.datetime.now() #calculate the current time
            currentTime = time_now.strftime("%H:%M")
            #start the timer basically
            if time_now < time_future:
                print('time now: ', time_now  ,  'and time left: ', + (time_future - time_now)) # gives user the current time and time left

                #calculates break/time to take a break!
            elif time_future <= time_now <= time_final:
                print('Time to Take a Breakkkkk!')

                #timer finished.. check to ready for another timer
            else:

                print('time_now > time_future - Finished')
                #add a bell to signal the end of program coz why not?
                print('\a')

                for a in range(10):
                    winsound.Beep((a+100),500)
                    print('\a')
                #get user input if they wanna start another timer    
                user_input = messagebox.askyesno("End of Pomodoro Timer!","Do you want to start another Pomodoro Counter?")

                pomodoros += 1 #keeps track of pomodoros used
                if user_input == True:
                    #new pomodoro counter
                    time_now = date_time.datetime.now() #calculate current time
                    time_future = time_now + date_time.timedelta(0,time_pom) #calcualte time for timer/future time for timer to run
                    time_final = time_now + date_time.timedelta(0, time_pom+delta_seconds)
                    continue
                elif user_input == False:
                # print(f'Pomodoro Complete!! \nYou ')
                    messagebox.showinfo(f'Pomodoro complete!!, \nTime is now {currentTime}', "\nYou finished "+str(pomodoros)+" Pomodoros today!!")
                    break 
        print('\n\nMade it to the end!!\n\n')
pomRun = pomTimer()
pomRun.startTimer()