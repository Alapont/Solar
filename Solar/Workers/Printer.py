from Workers import worker
import row

class Printer(worker.Worker):
    """prints an input to cmd"""
    def start(self, config=None): pass
    def input(self, data): 
        if (data!=None) and data._dict!=None:
            line=""
            for k in data._dict:
                line=line+str(k)+": "+str(data._dict.get(k))+"\t"
            print(line)
            return data
    def results(self): pass
    def addOutput(sefl, worker): pass

