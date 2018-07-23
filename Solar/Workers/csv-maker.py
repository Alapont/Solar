class CsvMaker(object):
    #gets a lot of workers and serializes them to work united as one
    def start(self,fileName=None,headder="TIMESTAMP,ARFISOL,BSRN,CESA,DISS,KONTAS,PSA,TSA-1,TSA-2,"):
        if fileName == None:
            self=None
        else:
            self._fileName=fileName;
    def input(self,data):
        for worker in self.workers:
            worker.input(data);
    def results(self):
        for worker in self.workers:
            worker.results();
