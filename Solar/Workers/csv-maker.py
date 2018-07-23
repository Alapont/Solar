from Workers import worker
class CsvMaker(worker):
    #gets a lot of workers and serializes them to work united as one
    def start(self,fileName=None,headder="TIMESTAMP,ARFISOL,BSRN,CESA,DISS,KONTAS,PSA,TSA-1,TSA-2,"):
        if fileName == None:
            self=None #seppuku
        else:
            self._fileName=fileName;
    def input(self,data):
        with open(self._fileName, 'a') as fd:
          fd.write(_buildLine(data))
    def results(self):
        #if one file is opened for the whole writting duration, close it.
        #multiple oppenings are concerning
        pass

    def _buildLine(atributes,timestamp='TIMESTAMP',separator=','):
        if (timestamp=='TIMESTAMP'):
            return headder
        line='\n'+timestamp
        for elem in atributes:
            line+=','+_ftos(elem)
        return line
    def _ftos(num):#needed to maintain style with libreOffice. who am I to argue
        return ('"'+str(num).replace('.',',')+'"')