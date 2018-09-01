from Workers import worker
import time
class CsvMaker(worker.Worker):
    #gets data and stores it to a csv

    def start(self,fileName=None,header=["timestamp","ARFISOL","BSRN","CESA","DISS","KONTAS","PSA","TSA1","TSA2","dARFISOL","dBSRN","dCESA","dDISS","dKONTAS","dPSA","dTSA1","dTSA2","sigma increment","rowNum","sigma","mean","decision"]):
        if fileName == None:
            self=None #seppuku
        else:
            self._fileName=fileName
            self._header=header
            self._buffer=""
            self._bufferSize=0
            self._bufferLimit=10000
            self._errors=0
            self._startTime=time.time()
            self._headerFlag=False
            
            with open(self._fileName, 'w') as fd:
                fd.write("")

    def input(self,data):
        if self._headerFlag==False:#headder creator
            self._headerFlag=True
            self._header=data._dict.keys()
            line=''
            for elem in self._header:
                if line =='':
                    line=str(elem)
                else:
                    line=line+',"'+str(elem)+'"'
            line=line+"\n"
            self._buffer=line
        self._bufferSize=self._bufferSize+1
        line=self._buildLine(data)
        self._buffer+= line
        if self._bufferSize==self._bufferLimit:
            self._bufferSize=0
            try:
                with open(self._fileName, 'a') as fd:
                    fd.write(self._buffer)
                    print(data.get("rowNum"))
                    self._buffer=""
            except:
                self._errors=self._errors+1
                print("error")

        return data

    def results(self,destiny):
        with open(self._fileName, 'a') as fd:
            fd.write(self._buffer)
        print("\nErrors:"+str(self._errors)+"\tStart Time:"+str(round(self._startTime,2))+"Total:"+str(round((time.time()-self._startTime)/60,2))+"min \n")
    
    def addOutput(sefl, worker): pass#To-Do

    def _buildLine(self,atributes,separator=','):
        def isNumber(n):
            if n==None:
                return False
            try:
                float(n)
                return True
            except ValueError:
                pass
            return False

        line=''
        for elem in self._header:
            value=atributes.get(elem)
            if line!='':
                line=line+','

            if isNumber(value):
                line=line+str(value)
            else:
                line=line+'"'+str(value)+'"'

        return line+'\n'
