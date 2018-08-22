from Workers import worker
import row
import math

class Delta(worker.Worker):
    """appends increment"""
    def start(self, config=None):
        self._last=None
    def input(self, data):

        #Utilitiesç
        def isNumber(n):
            if n==None:
                return False
            try:
                float(n)
                return True
            except ValueError:
                pass
            return False
        def delta(cur,last,atribute):
            """increment between 2 values (if possible)"""
            a=cur.get(atribute)
            b=last.get(atribute)
            if None in [a,b]:
                return None
            else:
                return a-b        
        def mean(data):
            avg=0
            count=0
            for i in data:
                if isNumber(i):
                    avg=avg+i
                    count=count+1
            avg=avg/(count)if count!=0 else None
            return avg,count
        def sigma(data):
            """standard deviation of data as an array
            σ=sqrt((sum (x-mean)^2)/N)"""
            
            avg,count=mean(data)

            #sum (x-mean^)2
            var=0
            for i in data:
                if isNumber(i):
                    var=var+(i-avg)**2

            # sqrt(sum/n)
            return math.sqrt(var/count),avg
        
        calc=[]
        #σ(x)
        s,m= sigma([
            data.get("ARFISOL"),
            data.get("BSRN"),
            data.get("CESA"),
            data.get("DISS"),
            data.get("KONTAS"),
            data.get("PSA"),
            data.get("TSA1"),
            data.get("TSA2"),
            ])
        calc=calc+[["sigma",s],["mean",m]]
        if self._last!=None :
            #Δ(x) 
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
            calc=calc+delta
            #|Δ(x)| "absolute mean increment"
            aux=[]
            for res in delta:
                aux.append(res[1])
            _,ami=mean(aux)
            calc=calc+[["absolute mean increment",ami]]
            #Δ(σ(x)) "sigma increment"
            ds,_= sigma([
                self._last.get("dARFISOL"),
                self._last.get("dBSRN"),
                self._last.get("dCESA"),
                self._last.get("dDISS"),
                self._last.get("dKONTAS"),
                self._last.get("dPSA"),
                self._last.get("dTSA1"),
                self._last.get("dTSA2"),
                ])
            calc=calc+[["sigma increment",ds]]
        
        
        self._last=data.add(calc)
        return self._last


        
        return self._last
    def results(self): pass
    def addOutput(sefl, worker): pass