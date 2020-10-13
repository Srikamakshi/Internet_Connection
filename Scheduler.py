# -*- coding: utf-8 -*-
"""
Created on Mon Oct 12 00:10:47 2020

@author: Srikamakshi
"""

import time
import schedule
from datetime import datetime
import csv
import speedtest

with open("Newfile.csv", "w+") as f:
    writer = csv.writer(f)
    writer.writerow(["Time","Download","Upload"])

def speed_testing():
    speed_test = speedtest.Speedtest()
    dt=datetime.now()
    d3=dt.time()
    download = speed_test.download()
    dl = round(download/(10**6),2)
    upload = speed_test.upload()
    ul = round(upload/(10**6),2)
    with open("Newfile.csv", "a") as f:
        writer = csv.writer(f)
        writer.writerow([d3,dl,ul])
    
schedule.every(2).minutes.do(speed_testing)


while 1:
    schedule.run_pending()
    time.sleep(1)
