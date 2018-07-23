import csv;
from Workers import workers,MinMax;
#import png;                #Love this dual window thing in VS 

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




def createArray(r):
    #used to get only the usefull data and errase night data
    #should get deprecated
    if (r[0]=='TIMESTAMP'):
        pass
        #print("Estamos en un header y hacemos cosas de Header")
    elif isDay(r[0]): #need to skip rows from night¿setted by param?
        #print("La fila es la numero " + str(num) +" Timestamp:"+r[0]);
        A=munch(r[1]);             #ARFISOL
        B=munch(r[2]);             #BSRN
        C=munch(r[3]);             #CESA
        D=munch(r[4]);             #DISS
        K=munch(r[5]);             #KONTAS
        P=munch(r[6]);             #PSA
        T=dualMunch(r[7],r[8]);    #TSA
        #ahora nos toca ordenar los datos (mas o menos) físicamente(~ish)
        #print("A: %4d, B: %4d, C: %4d, D: %4d, K: %4d, P: %4d, T: %4d" % (A,B,C,D,K,P,T));
        return r[1:8];
    else: 
       #debería devolver algo que le diga al de arriba que no procese la fila
       return None;
       

def getDataCsv(route):
    #gets data and pass it to the worker system through the union worker
    ext=".csv"
    union = workers.Workers()
    union.start(MinMax.minMax())
    for i in range (2, 12):
        index = str(i) if i>9 else '0'+str(i)
        data=route+"2015"+index+ext
        print("getting "+ data)
        with open(data, encoding='utf-8') as f:
            union.start()
            reader = csv.reader(f)
            for i, row in enumerate(reader):
                if row[0]=='TIMESTAMP':
                    pass
                else:
                    result=createArray(row,i)
                    if isDay(row[0]):
                        union.input(result)
        union.results();
            
    #There are reedings \ ^^ /




def getDataXlsx(route): # doomed after 20 minutes (let me believe it has been 20 min) it wasn't wasted time
    #open files, get data, close files, return data
    ext=".xlsx";
    wb=openpyxl.load_workbook(route+"201502"+ext);#file is big and no verbose T_T thats the deal with unix-like commands, no output can mean "all ok" or "crashed"
    print("end getData");
    #tanto se tarda en abrir un p*t* archivo de 2MB? O_O

def main():
    route=r"C:\Users\pablo\OneDrive - Universidad Complutense de Madrid (UCM)\2017-18\TFG Solar\solar\\";   #\\ needed instead of just \  //really python?, really
    #print("main");
    getDataCsv(route);
    input("Press Enter to continue...")
    #do something with de data



main();
# he puesto que lea un fichero que casualmente es el source del video del fuego de youtube. paso de hacer mas mágia que no me apetece una 💩
#       He cocinado un link de youtube, con autoplay, sin botones, sin interfaz, solo el video
# que les follen, no se abrir una consola de python en un punto concreto de la ejecución, mas 💩 pa ellos
# maybe (and just maybe) xlsx isn't the best format
# maybe (and just maybe) xml  isn't the best format either (but better)
# can I just work with csv (csv are spreadsheets for computers)
# cooooooño y yo preocupándome de mierdas cuando lo puede hacer otro por mi? // no recuerdo a qué venía esto
# lets see how it is to read csv from python
# it's easier to bash-fu your way to csv all the values and do magic with them
# god bless default values, aunque me toca un poco que espere un separador distinto.

#   TIMESTAMP,           ARFISOL  ,BSRN, CESA,DISS,KONTAS,  PSA,TSA-1,TSA-2
#['2015-02-04 13:20:00', '663,949', '' , '680,513', '661', '636',  '', '644,202', '643,348']
