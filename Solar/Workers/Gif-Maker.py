class gifMaker(object):
    """worker to make a gif from the data"""
    def start(self): 
        self.array
        self.resultmaker=self._results_gif(self);
    def input(self, input):
        #fill array
        #take snapshot
        pass
    def results(self):
        #other results may be used
        return self.resultmaker


    #Results set
    def _results_gif(self):
        #feed snapshots to gifmaker
        pass

    #Utilities
    def _dualMunch(a,b,min=0,max=1000,range=256):
        #checks if a or b is '' munching the otherone and semisum of both if possible (and min if both '')
        if(a=='' and b==''): #really python? AND???
            return min;
        if(a=='' or b==''): #really python? AND???
            #at least one should be not null
            if (a==''):
                return munch(b,min,max,range);
            else:
                return munch(a,min,max,range);
        else:#trilema prepare data by str->float->operate->munch no last conversion by magic casting
            A=float(a.replace(',','.'));
            B=float(b.replace(',','.'));
            return munch(str((A+B)/2),min,max,range);

    def _munch(number,min=0,max=1000,range=256):
        #munches numbers to prepare them to be used as pixels
        #if the number exceeds min or max it gets truncated.
        #its just a 3-rule casted to int
        if number == '':
            return 0;
        else:
            pixel=float(number.replace(',','.')); #expects . as decimal separator
            if pixel <min:
                return min;
            elif pixel > max:
                return max;
            else:
                step=(max/range);
                return int(round((pixel/step),0));