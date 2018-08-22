from Workers import worker
import row

class Delta(worker.Worker):
    """appends increment"""
    def start(self, config=None):
        self._last=None
    def input(self, data):
        def delta(cur,last,atribute):
            pass
            a=cur.get(atribute)
            b=last.get(atribute)
            if None in [a,b]:
                return None
            else:
                return a-b
            

        if self._last!=None :
            delta=[
                ["dARFISOL",delta(data,self._last,"ARFISOL")],
                ["dBSRN",delta(data,self._last,"BSRN")],
                ["dCESA",delta(data,self._last,"CESA")],
                ["dDISS",delta(data,self._last,"DISS")],
                ["dKONTAS",delta(data,self._last,"KONTAS")],
                ["dPSA",delta(data,self._last,"PSA")],
                ["dTSA1",delta(data,self._last,"TSA1")],
                ["dTSA2",delta(data,self._last,"TSA2")]
            ]
            new=self._last.add(delta)
            self._last=data
            return new
        else: 
            self._last=data
    def results(self): pass
    def addOutput(sefl, worker): pass