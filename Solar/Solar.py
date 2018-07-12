import csv;
#import png;

#  *------------------------+
#  |00:  en lugar de fuego  |
#  |01: tengo una webcam al |
#  |10:  desierto           |
#  |20:                     |
#  |30: listening to:       |
#  |40:  el gilipollas del  |
#  |50: vecino dandolo todo |
#  |60:   con el musicote   |
#  |70:                     |
#  |80:               понт  |
#  +------------------------+

def isDay(timeStamp,dawn=10,dusk=20):
    #for now will just check if timestam is between dawn and dusk
    day,hour=timeStamp.split(' ');
    hours,mins,secs=hour.split(':');
    return dawn <= int(hours) < dusk;

def dualMunch(a,b,min=0,max=1024,range=256):
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
        return munch(str((A+B)/2),min,max,range);/

def munch(number,min=0,max=1024,range=256):
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


def createArray(r, num=0):
    if (r[0]=='TIMESTAMP'):
        print("Estamos en un header y hacemos cosas de Header")
    elif isDay(r[0]): #need to skip rows from night¿setted by param?
        print("La fila es la numero " + str(num) +" Timestamp:"+r[0]);
        A=munch(r[1]);             #ARFISOL
        B=munch(r[2]);             #BSRN
        C=munch(r[3]);             #CESA
        D=munch(r[4]);             #DISS
        K=munch(r[5]);             #KONTAS
        P=munch(r[6]);             #PSA
        T=dualMunch(r[7],r[8]);    #TSA
        #ahora nos toca ordenar los datos (mas o menos) físicamente(~ish)
        print("A: %4d, B: %4d, C: %4d, D: %4d, K: %4d, P: %4d, T: %4d" % (A,B,C,D,K,P,T));
    #else:
        #row skipped for it being at night
       

def getDataCsv(route):
    ext=".csv";
    data=route+"201502"+ext;
    print("getting "+ data);
    with open(data, encoding='utf-8') as f:
        reader = csv.reader(f)
        for i, row in enumerate(reader):
            createArray(row,i);
    #There are reedings \ ^^ /




def getDataXlsx(route): # doomed after 20 minutes (let me believe it has been 20 min) it wasn't wasted time
    #open files, get data, close files, return data
    ext=".xlsx";
    wb=openpyxl.load_workbook(route+"201502"+ext);#file is big and no verbose T_T thats the deal with unix-like commands, no output can mean "all ok" or "crashed"
    print("end getData");
    #tanto se tarda en abrir un p*t* archivo de 2MB? O_O

def main():
    route=r"C:\Users\pablo\OneDrive - Universidad Complutense de Madrid (UCM)\2017-18\TFG Solar\solar"+"\\";#really python, really
    print("main");
    getDataCsv(route);
    #do something with de data



main();
#he puesto que lea un fichero que casualmente es el source del video del fuego de youtube. paso de hacer mas mágia que no me apetece una 💩
#que les follen, no se abrir una consola de python en un punto concreto de la ejecución, mas 💩 pa ellos
#maybe (and just maybe) xlsx isn't the best format
#maybe (and just maybe) xml  isn't the best format either
#can I just work with csv (csv are spreadsheets for computers)
#cooooooño y yo preocupándome de mierdas cuando lo puede hacer otro por mi?
#lets see how it is to read csv from pythob
#it's easier to bash-fu your way to csv all the values and do magic with them
#god bless default values

#   TIMESTAMP,           ARFISOL  ,BSRN, CESA,DISS,KONTAS,  PSA,TSA-1,TSA-2
#['2015-02-04 13:20:00', '663,949', '' , '680,513', '661', '636',  '', '644,202', '643,348']
