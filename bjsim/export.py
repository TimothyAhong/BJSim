import datetime
import socket

class Exporter:
    def __init__ (self):
        now = datetime.datetime.now()
        #FORMAT
        #hour_minute__month_day_year(machine)(thread number)
        self.date_stamp = str(now.hour)+"__"+str(now.month)+"_"+str(now.day)+"_"+str(now.year)
        self.trial_id = 0
    
    def setup(self,thread_num):    
        #get hostname to determine which folder we write to
        self.machine_name = socket.gethostname().split('.')[0]
        print "Machine: "+self.machine_name
        append = self.date_stamp +"("+self.machine_name+")"+"("+str(thread_num)+").csv"
        #if we are on an ecf machine then write data to ~/bjsimpy_data
        if socket.gethostname().find("ecf") !=-1:
            path = "../../bjsimpy_data/"
        else:
            path = "../data/"
        #define all the filenames based on the date and the thread number
        self.hands_file=path+"hands_"+append
        self.shoes_file=path+"shoes_"+append
        self.trials_file=path+"trials_"+append
        self.ptrials_file=path+"ptrials_"+append

    def open_files(self):
        #open the files
        self.hands = open(self.hands_file,'a')
        self.shoes = open(self.shoes_file,'a')
        self.trials = open(self.trials_file,'a')
        self.ptrials = open(self.ptrials_file,'a')

    def close_files(self):
        #close the files, dont forget to call this
        self.hands.close()
        self.shoes.close()
        self.trials.close()
        self.ptrials.close()

    def h(self,data):
        #USAGE
        #data must be of the format [player.id,wager,player bankroll,count,outcome,player total]
        self.w(self.hands,data)

    def s(self,data):
        #USAGE
        #data must be of the format [player.id,total wagered,player bankroll at start,net loss/gain, percent change]
        self.w(self.shoes,data)

    def t(self,data):
        #USAGE
        #data must be of the format [trial.id,date_stamp,duration(s),num decks played]
        self.w(self.trials,data)

    def pt(self,data):
        #USAGE
        #data must be of the format [player.id,dealer.id,final bankroll,starting bankroll,hands won,hands lost,hands pushed,hands until double(0),hands until ruin(0)]
        self.w(self.ptrials,data)

    def w(self,output_file,data):
        #include trial
        line=str(self.trial_id)
        for element in data:
            line+=","+str(element)
        line+="\n"
        output_file.write(line)

global exporter
exporter = Exporter()