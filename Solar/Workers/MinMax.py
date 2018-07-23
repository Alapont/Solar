class minMax(object):
    """worker to know min and max in any given point of all the data providen up to that moment"""
    def start(self): 
        self.mins=['nan','nan','nan','nan','nan','nan','nan','nan'];
        self.maxs=['nan','nan','nan','nan','nan','nan','nan','nan'];
        
    def input(self, input):
        try:
            for i in range (1, 8):
                self.mins[i-1]=_min(self.mins[i],input[i])
                self.maxs[i-1]=_max(self.maxs[i],input[i])
        except Exception:
            print("error");

    def results(self):
        print("mins: "+str(self.mins));
        print("maxs: "+str(self.maxs));

    
def _min(a,b):
    if(a in ['nan','']): return b;
    if(b in ['nan','']): return a;
    if(a<b):
        return a;
    return b;

def _max(a,b):
    if(a in ['nan','']): return b;
    if(b in ['nan','']): return a;
    if(a>b):
        return a;
    return b;
