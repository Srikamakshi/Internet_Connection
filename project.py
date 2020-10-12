# -*- coding: utf-8 -*-
"""
Created on Sun Oct 11 16:40:06 2020

@author: kavya
"""
import pandas as pd
import matplotlib.pyplot as plot
from datetime import datetime
import speedtest


def speed_testing():
    speed_test = speedtest.Speedtest()
    dt=datetime.now()
    d3=dt.time()
    download = speed_test.download()
    dl = round(download/(10**6),2)
    upload = speed_test.upload()
    ul = round(upload/(10**6),2)
    return(dl,ul)

def best_time():
    df=pd.read_csv('User_file.csv')
    df.plot.bar(rot=15, title="internet_speed");
    plot.show(block=True);
    col1=df["Download"]
    max_dl=col1.idxmax()
    col2=df["Upload"]
    max_ul=col2.idxmax()
    col3=df["Time"]
    t1=col3[max_dl]
    t2=col3[max_ul]
    dl_time=((t1[0:2]))
    ul_time=((t2[0:2]))
    return(dl_time,ul_time)

def check_speed():
    df = pd.read_csv("User_file.csv")
    df1 = pd.read_csv("isp.csv")
    asu_speed=df1["Speed"]
    dl_mean=df["Download"].mean()
    ul_mean=df["Upload"].mean()
    avg_speed= dl_mean + ul_mean
    print("Who is your ISP")
    print("1.BSNL")
    print("2.Airtel")
    print("3.Jio")
    print("4.ACT")
    index=int(input("Enter your choice:"))

    if ((index<=4) and (not(index <=0))):
        if (avg_speed>=asu_speed[index-1]):
            print("The promised speed is provided")
        else:
            print("The promised speed is not provided")
    else:
        print("Your choice is invalid")

print("Welcome, What do you want to do?")
print(" 1.Check your internet speed")
print(" 2.Know the best time to acess the internet")
print(" 3. Check if the internet speed is the one assured by your ISP ")  
choice= int(input("Please choose your option:"))

if (choice == 1):
    [download,upload]=speed_testing()
    print(f"Your download speed: {download} Mbps")
    print(f"Your upload speed: {upload} Mbps")

elif (choice == 2):
    [dl_time,ul_time]=best_time()
    d_time=int(dl_time)
    u_time=int(ul_time)
    if (d_time==21):
        d_ntime=str('00')
    else:
        d_ntime=str(d_time+1)
                
        if (u_time==21):
            u_ntime=str('00')
        else:
            u_ntime=str(u_time+1)

    print("The best time for download is from " + dl_time + ":00 to " + d_ntime + ":00")            
    print("The best time for upload is from " + ul_time + ":00 to " + u_ntime + ":00")  

elif (choice ==3): 
    check_speed()

else:
    print("Your choice is invalid")      
        
        
        
  

    
