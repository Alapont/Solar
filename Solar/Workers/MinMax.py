class minMax(object):
    """worker to know min and max in any given point of all the data providen up to that moment"""
    def start(self): 
        self._mins=['nan','nan','nan','nan','nan','nan','nan','nan'];
        self._maxs=['nan','nan','nan','nan','nan','nan','nan','nan'];
        self._trys=0;
        self._entries=0;
        
    def input(self, In):
        input=In[1:]
        if In[0]!='':
            self._trys+=1
        try:
            for i in range (0, len(input)):
                self._mins[i]=_min(self._mins[i],input[i])
                self._maxs[i]=_max(self._maxs[i],input[i])
        except Exception:
            print("error");
        self._entries +=1

    def results(self):
        print("Days processed: "+str(self._trys)+"/"+str(self._entries)+" "+str(self._trys/self._entries*100)+"%")
        print("mins: "+str(self._mins));
        print("maxs: "+str(self._maxs));

    
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
