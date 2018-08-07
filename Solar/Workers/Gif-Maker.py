import tempfile
import imageio
class gifMaker(object):
    """worker to make a gif from the data"""
    """tengo 2 opciones, una es la de almacenar TODOS los datos y otra almacenarlso en disco"""
    def start(self): 
        self._array=[]
        self.index=0
        self._pics=tempfile.tempdir()

    def input(self, input):
        munchedVars=[]
        #fill array
        for i,elem in input[1:]:
            munchedVars[i]=_munch(elem)
        imageio.imwrite(_pics,str(index)+".png")
        #take snapshot

    def results(self,destiny):
        #other results may be used
        with imageio.get_writer('/path/to/movie.gif', mode='I') as writer:
            for filename in filenames:
                image = imageio.imread(filename)
                writer.append_data(image)
        return self.resultmaker


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

    def _munch(number=0,min=0,max=1000,range=256):
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

    def _grid(stations):
        A=stations[0]
        B=stations[1]
        C=stations[2]
        D=stations[3]
        K=stations[4]
        P=stations[5]
        T=stations[6]
        grid=[
            [D,D,D,D,D,D,D,D,D,K],
            [C,D,D,D,D,D,D,D,K,K],
            [C,C,D,D,D,D,D,K,K,K],
            [C,C,C,C,D,D,K,K,K,K],
            [C,C,C,C,C,D,K,K,K,K],
            [C,C,C,C,C,T,T,K,K,K],
            [B,B,C,C,T,T,T,T,K,K],
            [B,B,B,C,P,T,T,T,T,K],
            [B,B,B,P,P,P,A,A,T,T],
            [B,B,B,P,P,P,P,A,A,A],
            ]
        return grid

    def _pic(grid):
        pass