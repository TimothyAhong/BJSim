#!/usr/bin/python
import sys
import subprocess
from threading import Thread

#get target trial 
trial = sys.argv[1]
#total number of threads, get from config file later
num_threads = 5

#runs the specified trial with the specified trial number
def runeth(trial,thread,*args):
    print "New thread("+thread+") running "+trial
    subprocess.call([sys.executable, trial, thread])

#runeth unto thy thread
for i in range(1,num_threads+1):
    Thread(target=runeth, args=(trial,str(i),2)).start()
