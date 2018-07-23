from Workers import worker
class minMax(object):
    """worker to know min and max in any given point of all the data providen up to that moment"""
    #to do remove all debugging data and operations
    def start(self): 
        self._mins=['nan','nan','nan','nan','nan','nan','nan','nan'];
        self._maxs=['nan','nan','nan','nan','nan','nan','nan','nan'];
        self._trys=0;
        self._entries=0;
        
    def input(self, In):
        #for each row compares it to local mins and max and replaces if needed
        self._trys+=1
        input=In[1:] #avoids timestamp
        try:
            for i in range (0, len(input)):
                self._mins[i]=_min(self._mins[i],input[i])
                self._maxs[i]=_max(self._maxs[i],input[i])
        except Exception:
            print("error");
        self._entries +=1

    def results(self):
        #for now is just a proof of work and a results print
        print("Days processed: "+str(self._trys)+"/"+str(self._entries)+" "+str(self._trys/self._entries*100)+"%")
        print("mins: "+str(self._mins));
        print("maxs: "+str(self._maxs));

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
