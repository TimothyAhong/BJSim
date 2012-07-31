#!/bin/bash

#script for mac os x that runs the specified trial a certain number of times

#Build with chmod +x ./run.sh
#Run with ./run.sh 

echo "Running trial_1.py 1000 times. Go chill for a bit..."
for i in {1..10}
do
   python trial_1.py "2"
done
echo "Simulations complete! Check your data files"