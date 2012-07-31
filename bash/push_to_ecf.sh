#!/bin/bash

#Build with chmod +x ./push_to_ecf.sh
#Run with ./push_to_ecf.sh 

#A script for mac os x that copies over the bj simulation files over to the ahongtim directory on ecf
#To be safe run this before running any tests
ssh ahongtim@remote.ecf.utoronto.ca 'rm -rf bjsimpy/'
scp -r ~/Documents/Projects/bjsimpy/  ahongtim@remote.ecf.utoronto.ca:bjsimpy