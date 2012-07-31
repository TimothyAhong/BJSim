#!/bin/bash
# Script to distribute MATLAB training jobs to multiple nodes in a system and create a screen for each job

# some helpers, stolen shamelessly from internet forums

rand() {
    printf $((  $1 *  RANDOM  / 32767   ))
}
rand_element () {
    local -a th=("$@")
    unset th[0]
    printf $'%s\n' "${th[$(($(rand "${#th[*]}")+1))]}"
}

# Initialize settings
screenname=csc401-part3
A3_DIR="abs/path/to/your/A3/dir"
nodes="greywolf b3175-18" #etc etc use as many nodes as you wish

echo 'Creating screen session'
screen -d -m -S $screenname

echo 'Now creating screen windows'

# This is how you send a job to a node
m=1 
q=2
for d in 3 4; do
    for otherparam in 5 6; do
        node=$(rand_element $nodes)
        echo "Sending job m=$m q=$q d=$d op=$otherparam to $node"
        screen -S $screenname -X screen -t "m=$m q=$q d=$d op=$otherparam" ssh $node "cd $A3_DIR && matlab -r 'M=$m; Q=$q; D=$d; someotherglobalvarformyscript=$otherparam; myAwesomeTrainingScript'"
    done
done