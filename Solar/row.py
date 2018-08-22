
def pFloat(f):
    return float(f.replace(',','.')) if f!='' else None

class row(object):
    def __init__(self,r=['nan','nan','nan','nan','nan','nan','nan','nan','nan'],i=0):
        self._dict={
            "timestamp":r[0],
            "ARFISOL":pFloat(r[1]),
            "BSRN":pFloat(r[2]),
            "CESA":pFloat(r[3]),
            "DISS":pFloat(r[4]),
            "KONTAS":pFloat(r[5]),
            "PSA":pFloat(r[6]),
            "TSA1":pFloat(r[7]),
            "TSA2":pFloat(r[8]),
            "rowNum":i
            }
    def add(self,values):
        for pair in values:
            self._dict[pair[0]]=pair[1]
        return self
    def get(self,key,default=float(0.0)):
        return self._dict.get(key,default)
