# -*- coding: utf-8 -*-
"""
Created on Sun Oct 11 16:40:06 2020

@author: kavya
"""
import pandas as pd
import matplotlib.pyplot as plot
from datetime import datetime
import speedtest
from os import system
from time import sleep

flag=0
Speed_data=pd.read_csv('Speedx24hr.csv')

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
    col1=Speed_data["Download"]
    max_dl=col1.idxmax()
    col2=Speed_data["Upload"]
    max_ul=col2.idxmax()
    col3=Speed_data["Time"]
    dl_time1=col3[max_dl]
    dl_time2=col3[max_dl+1]
    ul_time1=col3[max_ul]
    ul_time2=col3[max_ul+1]
    return(dl_time1,dl_time2,ul_time1,ul_time2)

def plot_graph():
    Speed_data.plot.bar(x="Time", y= ["Download" , "Upload"])
    plot.show()

def check_speed():
    ISP_data = pd.read_csv("isp.csv")
    asu_speed=ISP_data["Speed"]
    dl_mean=Speed_data["Download"].mean()
    ul_mean=Speed_data["Upload"].mean()
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

while(flag==0):
    
    print("Welcome, What do you want to do?")
    print(" 1.Check your internet speed")
    print(" 2.Know the best time to acess the internet")
    print(" 3.Check if the internet speed is the one assured by your ISP ")  
    print(" 4.Exit")
    choice= int(input("Please choose your option:"))

    if (choice == 1):
        [download,upload]=speed_testing()
        print(f"Your download speed: {download} Mbps")
        print(f"Your upload speed: {upload} Mbps")

    elif (choice == 2):
        [dl_time1,dl_time2,ul_time1,ul_time2,]=best_time()
        print("The best time for download is from " + dl_time1 + " to " + dl_time2 )            
        print("The best time for upload is from " + ul_time1 + " to " + ul_time2 )  
        graph=input("Do you want to see the internet speed for the past 24hrs [y/n]:")
        if((graph=='y') or (graph=='Y') or (graph=='Yes') or (graph=='yes')):
            plot_graph()


    elif (choice ==3): 
        check_speed()

    elif (choice==4):
        flag=1
    else:
        print("Your chioce is invalid")  

    sleep(5) 
    system('cls')     
        
        
  

    
