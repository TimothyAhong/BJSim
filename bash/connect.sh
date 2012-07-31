#! /bin/bash

#USAGE
# build with chmod +x ./connect.sh 
# run with ./connect.sh $arg1
# make sure to run 'screen' before running connect.sh
# arguments
#   1: Target trial (e.g. 'trial_1.py')
#
# you may need to add RSA keys for each ecf computer
# this can be done quickly by sending a command to all screens control-a :
#   at "#" stuff "yes^M"
# 
# you may need to manually close all connections
# this can also be done by sendint a command to all screens
#   at "#" stuff "????"

echo 'Distributing '$1' to all the ecf machines'
echo 'Now creating connection windows'

ecf='.ecf.utoronto.ca'
num_machines=3

for i in {1..3}; do
    #determine ecf computer number and its machine domain
    computer="p$i"
    node="$computer$ecf"
    echo "Connecting to "$node"..."

    #Opens up a new screen per connection to remote.ecf.utoronto
    #Each connection will then ssh to its designated computer and run the specified trial
    screen -X screen -t $computer bash -c "ssh ahongtim@$node \"hostname; cd ~/bjsimpy/settings; python run.py trial_1.py;hostname;python\" "
done