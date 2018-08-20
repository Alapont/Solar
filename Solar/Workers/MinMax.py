from Workers import worker
from Solar import row
#import row
class minMax(object):
    """worker to know min and max in any given point of all the data providen up to that moment"""
    #to do remove all debugging data and operations
    def start(self): 
        self._result=[]
        self._mins=row()
        self._maxs=row()
        self._trys=0
        self._entries=0
        
    def input(self, data):
        #for each row compares it to local mins and max and replaces if needed
        self._trys+=1
        input=data[1:] #avoids timestamp
        try:
            for i in range (0, len(input)):
                self._mins[i]=_min(self._mins[i],input[i])
                self._maxs[i]=_max(self._maxs[i],input[i])
        except Exception:
            print("error");
        self._entries +=1
        return data
    def results(self):
        #for now is just a proof of work and a results print
        print("Days processed: "+str(self._trys)+"/"+str(self._entries)+" "+str(self._trys/self._entries*100)+"%")
        print("mins: "+str(self._mins));
        print("maxs: "+str(self._maxs));
        for item in self._result:
            item.input(_mins)
            item.input(_maxs)
        
    def addOutput(self, next):
        self._result.append(next)

#utilities    
def _min(a,b):
    if(a in ['nan','']): return b
    if(b in ['nan','']): return a
    if(a<b):
        return a;
    return b;

def _max(a,b):
    if(a in ['nan','']): return b
    if(b in ['nan','']): return a
    if(a>b):
        return a;
    return b;
