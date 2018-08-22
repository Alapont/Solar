from Workers import worker
import row

class Delta(worker.Worker):
    """appends increment"""
    def start(self, config):
        self._last=None
    def input(self, data):
        if self._last!=None :
            delta=[
                ["dARFISOL",data.get("ARFISOL")-self._last.__getattribute__("ARFISOL")],
                ["dBSRN",data.get("BSRN")-self._last.__getattribute__("BSRN")],
                ["dCESA",data.get("CESA")-self._last.__getattribute__("CESA")],
                ["dDISS",data.get("DISS")-self._last.__getattribute__("DISS")],
                ["dKONTAS",data.get("KONTAS")-self._last.__getattribute__("KONTAS")],
                ["dPSA",data.get("PSA")-self._last.__getattribute__("PSA")],
                ["dTSA1",data.get("TSA1")-self._last.__getattribute__("TSA1")],
                ["dTSA2",data.get("TSA2")-self._last.__getattribute__("TSA2")]
            ]
            new,self._last=_last.add(delta),data
            return new
    def results(self): pass
    def addOutput(sefl, worker): pass