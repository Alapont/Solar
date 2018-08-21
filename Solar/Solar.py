import csv
from Workers import worker, Union, MinMax
import row
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

def isDay(timeStamp,dawn=6,dusk=23):
    #for now will just check if timestam is between dawn and dusk
    day,hour=timeStamp.split(' ');
    hours,mins,secs=hour.split(':');
    return dawn <= int(hours) < dusk;




def createArray(r,i):
    #used to get only the usefull data and errase night data
    #should get deprecated
    if (r[0]=='TIMESTAMP'):
        pass
        #print("Estamos en un header y hacemos cosas de Header")
    elif isDay(r[0]):       #need to skip rows from night¿setted by param?
        R=[None]*(len(r))
        R[0]=r[0]
        for i in range (1,8):
            #cleaning the data to use floats for everything
            R[i]= float(r[i].replace(',','.')) if r[i]!='' else None
        return r[0:8];
    else: 
       #debería devolver algo que le diga al de arriba que no procese la fila
       return None;

def createDict(r,i):
    if r[0]!='TIMESTAMP':
        return row.row(r,i)

def getDataCsv(route):
    #gets data and pass it to the worker system through the union worker
    ext=".csv"
    union=Union.Union()
    m=MinMax.MinMax()
    union.start(MinMax.MinMax())
    data=route+"2015"+ext
    print("getting "+ data)
    with open(data, encoding='utf-8') as f:
        union.start()
        reader = csv.reader(f)
        for i, row in enumerate(reader):
            if row[0]=='TIMESTAMP':
                pass
            else:
                result=createDict(row,i)
                union.input(result)
    union.results();


def main():
    route=r"C:\Users\pablo\OneDrive - Universidad Complutense de Madrid (UCM)\2017-18\TFG Solar\solar\\";   #\\ needed instead of just \  //really python?, really
    getDataCsv(route);
    input("Press Enter to continue...")
    

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
