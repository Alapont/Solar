from Workers import worker
import time
class CsvMaker(worker.Worker):
    #gets data and stores it to a csv

    def start(self,fileName=None):
        if fileName == None:
            self=None #seppuku
        else:
            self._fileName=fileName
            self._header=None
            self._buffer=""
            self._bufferSize=0
            self._bufferLimit=1000
            self._errors=0
            self._startTime=time.time()
    def input(self,data):
        if self._header==None:
            self._header=data._dict.keys()
            line=''
            for elem in self._header:
                if line =='':
                    line=str(elem)
                else:
                    line=line+',"'+str(elem)+'"'
            line=line+"\n"
            with open(self._fileName, 'w') as fd:
                fd.write(line)
        self._bufferSize=self._bufferSize+1
        self._buffer=self._buffer+self._buildLine(data)
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
        print("errors:"+str(self._errors)+"\tStart Time:"+str(self._startTime)+"Total:"+str(time.time()-self._startTime)+"\n")
    
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
