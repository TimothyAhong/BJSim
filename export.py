import threading
import datetime
        
class export_data(threading.Thread):
    def __init__(self, data, filename):
        self.data=data
        self.filename=filename

    def run(self):
        #export to file, if fails then create another file replacing the %s in the filename with the correct number
        #if we are not done this task by 1 second then cancel
    

#for i in range(2):
#  t = ThreadClass(data,filename)
#  t.start()