import pandas as pd
import numpy as np
import glob, os
import PyPDF2


from os.path import isfile, join
from tkinter import Tk, Label , Button




#Funcionalidad del boton start ==================================================================================================
def convertToCsv():

    # Lecturas de archivos ==================================================================================================
    ruta = 'PDF_FILES/'

    contenido = os.listdir(ruta)
    archivos = [nombre for nombre in contenido if isfile(join(ruta , nombre)) ]
    
    for file in archivos:
        print(file[0:len(file)-4])

        #=========================================================================================================================


        #Variables del dataframe============================================================================================
        positions = []
        descriptions = []
        executions = []
        codes = []
        groupsNumbers = []
        groups = []
        subgroups = []
        addinfos = []
        uom = []
        mtml_uom = []
        quantities = []
        pricesUnites = []
        totals = []

    
        # Escaneando pdf =========================================================================================================
        pdf_file_obj = open('PDF_FILES/' + file , 'rb')

        #Obtener la metadata
        pdf_reader = PyPDF2.PdfReader(pdf_file_obj)
        #print(pdf_reader.metadata)

        #Obtener el total de paginas
        total_pages = len(pdf_reader.pages)

        #Podemos obtener cualquier pagina usando el metodo pages y ya que este es un arreglo podemos llamar al numero de pagina solo indicando su indice entre conrchetes
        #page_obj = pdf_reader.pages[0]

        #Recorremos las paginas
        for  i , page in enumerate(pdf_reader.pages):

            #Omitimos la primera pagina
            if(i > 0):
                #Obtenemos la pagina
                page_obj = pdf_reader.pages[i]

                #Ahora tenemos el texto completo (la contactenacion final solo la agregamos si queremos separar lineas en arreglo usando split() )
                text = page_obj.extract_text() + "\n"

                #Separamos por lineas
                content = text.split("\n")


                for j , item in enumerate(content):
                    #Seteamos a cero los auxiliares
                    auxDescription = ""

                    #Informacion reelevante empieza desde el 15
                    if(j > 14):
                        
                        #Revisar si el item comienza con un numero de tres indice, de ser asi comienza el item
                        if(len(item) > 2):
                            #Verificar si los primeros tres caracteres son numeros y el cuarto un espacio
                            if(
                                ( ord(item[0]) == 48 or ord(item[0]) == 49 or ord(item[0]) == 50 or ord(item[0]) == 51 or ord(item[0]) == 52 or ord(item[0]) == 53 or ord(item[0]) == 54 or ord(item[0]) == 55 or ord(item[0]) == 56 or ord(item[0]) == 57 ) and
                                ( ord(item[1]) == 48 or ord(item[1]) == 49 or ord(item[1]) == 50 or ord(item[1]) == 51 or ord(item[1]) == 52 or ord(item[1]) == 53 or ord(item[1]) == 54 or ord(item[1]) == 55 or ord(item[1]) == 56 or ord(item[1]) == 57 ) and
                                ( ord(item[2]) == 48 or ord(item[2]) == 49 or ord(item[2]) == 50 or ord(item[2]) == 51 or ord(item[2]) == 52 or ord(item[2]) == 53 or ord(item[2]) == 54 or ord(item[2]) == 55 or ord(item[2]) == 56 or ord(item[2]) == 57 ) and
                                item[3]==" "
                                ):

                                # Columna position ==================================================================== 
                                positions.append( str(item[0]) + str(item[1]) + str(item[2]) )

                                # Columna description ====================================================================
                                descriptions.append( item[3:len(item)] )
                            
                                #Verificamos que el siguiente no contenga el code (puede estar en los ultimos 5 caracteres que son numericos)
                                if( 
                                    (ord(content[j+1][len(content[j+1])-1]) == 48 or ord(content[j+1][len(content[j+1])-1]) == 49 or ord(content[j+1][len(content[j+1])-1]) == 50 or ord(content[j+1][len(content[j+1])-1]) == 51 or ord(content[j+1][len(content[j+1])-1]) == 52 or ord(content[j+1][len(content[j+1])-1]) == 53 or ord(content[j+1][len(content[j+1])-1]) == 54 or ord(content[j+1][len(content[j+1])-1]) == 55 or ord(content[j+1][len(content[j+1])-1]) == 56 or ord(content[j+1][len(content[j+1])-1]) == 57 ) and
                                    (ord(content[j+1][len(content[j+1])-2]) == 48 or ord(content[j+1][len(content[j+1])-2]) == 49 or ord(content[j+1][len(content[j+1])-2]) == 50 or ord(content[j+1][len(content[j+1])-2]) == 51 or ord(content[j+1][len(content[j+1])-2]) == 52 or ord(content[j+1][len(content[j+1])-2]) == 53 or ord(content[j+1][len(content[j+1])-2]) == 54 or ord(content[j+1][len(content[j+1])-2]) == 55 or ord(content[j+1][len(content[j+1])-2]) == 56 or ord(content[j+1][len(content[j+1])-2]) == 57 ) and
                                    (ord(content[j+1][len(content[j+1])-3]) == 48 or ord(content[j+1][len(content[j+1])-3]) == 49 or ord(content[j+1][len(content[j+1])-3]) == 50 or ord(content[j+1][len(content[j+1])-3]) == 51 or ord(content[j+1][len(content[j+1])-3]) == 52 or ord(content[j+1][len(content[j+1])-3]) == 53 or ord(content[j+1][len(content[j+1])-3]) == 54 or ord(content[j+1][len(content[j+1])-3]) == 55 or ord(content[j+1][len(content[j+1])-3]) == 56 or ord(content[j+1][len(content[j+1])-3]) == 57 ) and
                                    (ord(content[j+1][len(content[j+1])-4]) == 48 or ord(content[j+1][len(content[j+1])-4]) == 49 or ord(content[j+1][len(content[j+1])-4]) == 50 or ord(content[j+1][len(content[j+1])-4]) == 51 or ord(content[j+1][len(content[j+1])-4]) == 52 or ord(content[j+1][len(content[j+1])-4]) == 53 or ord(content[j+1][len(content[j+1])-4]) == 54 or ord(content[j+1][len(content[j+1])-4]) == 55 or ord(content[j+1][len(content[j+1])-4]) == 56 or ord(content[j+1][len(content[j+1])-4]) == 57 ) and
                                    (ord(content[j+1][len(content[j+1])-5]) == 48 or ord(content[j+1][len(content[j+1])-5]) == 49 or ord(content[j+1][len(content[j+1])-5]) == 50 or ord(content[j+1][len(content[j+1])-5]) == 51 or ord(content[j+1][len(content[j+1])-5]) == 52 or ord(content[j+1][len(content[j+1])-5]) == 53 or ord(content[j+1][len(content[j+1])-5]) == 54 or ord(content[j+1][len(content[j+1])-5]) == 55 or ord(content[j+1][len(content[j+1])-5]) == 56 or ord(content[j+1][len(content[j+1])-5]) == 57 ) and
                                    (ord(content[j+1][len(content[j+1])-6]) == 48 or ord(content[j+1][len(content[j+1])-6]) == 49 or ord(content[j+1][len(content[j+1])-6]) == 50 or ord(content[j+1][len(content[j+1])-6]) == 51 or ord(content[j+1][len(content[j+1])-6]) == 52 or ord(content[j+1][len(content[j+1])-6]) == 53 or ord(content[j+1][len(content[j+1])-6]) == 54 or ord(content[j+1][len(content[j+1])-6]) == 55 or ord(content[j+1][len(content[j+1])-6]) == 56 or ord(content[j+1][len(content[j+1])-6]) == 57 )
                                    ):
                                    executions.append(content[j+1][4:len(content[j+1])-6])
                                    codes.append(str(content[j+1][ len(content[j+1])-6])  +  str(content[j+1][ len(content[j+1])-5]) + str(content[j+1][ len(content[j+1])-4]) + str(content[j+1][ len(content[j+1])-3]) + str(content[j+1][ len(content[j+1])-2]) + str(content[j+1][ len(content[j+1])-1])) 
                                    groupsNumbers.append(content[j+2])
                                    groups.append(content[j+3])
                                    subgroups.append(content[j+4])
                                    #Add info son dos items juntos asi que los concatenamos
                                    addinfos.append( content[j+5] + content[j+6] ) 
                                    uom.append(content[j+7])
                                elif(
                                    (ord(content[j+2][len(content[j+2])-1]) == 48 or ord(content[j+2][len(content[j+2])-1]) == 49 or ord(content[j+2][len(content[j+2])-1]) == 50 or ord(content[j+2][len(content[j+2])-1]) == 51 or ord(content[j+2][len(content[j+2])-1]) == 52 or ord(content[j+2][len(content[j+2])-1]) == 53 or ord(content[j+2][len(content[j+2])-1]) == 54 or ord(content[j+2][len(content[j+2])-1]) == 55 or ord(content[j+2][len(content[j+2])-1]) == 56 or ord(content[j+2][len(content[j+2])-1]) == 57 ) and
                                    (ord(content[j+2][len(content[j+2])-2]) == 48 or ord(content[j+2][len(content[j+2])-2]) == 49 or ord(content[j+2][len(content[j+2])-2]) == 50 or ord(content[j+2][len(content[j+2])-2]) == 51 or ord(content[j+2][len(content[j+2])-2]) == 52 or ord(content[j+2][len(content[j+2])-2]) == 53 or ord(content[j+2][len(content[j+2])-2]) == 54 or ord(content[j+2][len(content[j+2])-2]) == 55 or ord(content[j+2][len(content[j+2])-2]) == 56 or ord(content[j+2][len(content[j+2])-2]) == 57 ) and
                                    (ord(content[j+2][len(content[j+2])-3]) == 48 or ord(content[j+2][len(content[j+2])-3]) == 49 or ord(content[j+2][len(content[j+2])-3]) == 50 or ord(content[j+2][len(content[j+2])-3]) == 51 or ord(content[j+2][len(content[j+2])-3]) == 52 or ord(content[j+2][len(content[j+2])-3]) == 53 or ord(content[j+2][len(content[j+2])-3]) == 54 or ord(content[j+2][len(content[j+2])-3]) == 55 or ord(content[j+2][len(content[j+2])-3]) == 56 or ord(content[j+2][len(content[j+2])-3]) == 57 ) and
                                    (ord(content[j+2][len(content[j+2])-4]) == 48 or ord(content[j+2][len(content[j+2])-4]) == 49 or ord(content[j+2][len(content[j+2])-4]) == 50 or ord(content[j+2][len(content[j+2])-4]) == 51 or ord(content[j+2][len(content[j+2])-4]) == 52 or ord(content[j+2][len(content[j+2])-4]) == 53 or ord(content[j+2][len(content[j+2])-4]) == 54 or ord(content[j+2][len(content[j+2])-4]) == 55 or ord(content[j+2][len(content[j+2])-4]) == 56 or ord(content[j+2][len(content[j+2])-4]) == 57 ) and
                                    (ord(content[j+2][len(content[j+2])-5]) == 48 or ord(content[j+2][len(content[j+2])-5]) == 49 or ord(content[j+2][len(content[j+2])-5]) == 50 or ord(content[j+2][len(content[j+2])-5]) == 51 or ord(content[j+2][len(content[j+2])-5]) == 52 or ord(content[j+2][len(content[j+2])-5]) == 53 or ord(content[j+2][len(content[j+2])-5]) == 54 or ord(content[j+2][len(content[j+2])-5]) == 55 or ord(content[j+2][len(content[j+2])-5]) == 56 or ord(content[j+2][len(content[j+2])-5]) == 57 ) and
                                    (ord(content[j+2][len(content[j+2])-6]) == 48 or ord(content[j+2][len(content[j+2])-6]) == 49 or ord(content[j+2][len(content[j+2])-6]) == 50 or ord(content[j+2][len(content[j+2])-6]) == 51 or ord(content[j+2][len(content[j+2])-6]) == 52 or ord(content[j+2][len(content[j+2])-6]) == 53 or ord(content[j+2][len(content[j+2])-6]) == 54 or ord(content[j+2][len(content[j+2])-6]) == 55 or ord(content[j+2][len(content[j+2])-6]) == 56 or ord(content[j+2][len(content[j+2])-6]) == 57 )
                                    ):
                                    #En esta secuencia al saltarnos una linea concatenamos la execution
                                    executions.append(content[j+1][4:len(content[j+1])] + content[j+2][0:len(content[j+2])-6])
                                    codes.append(  str(content[j+2][ len(content[j+2])-6]) + str(content[j+2][ len(content[j+2])-5]) + str(content[j+2][ len(content[j+2])-4]) + str(content[j+2][ len(content[j+2])-3]) + str(content[j+2][ len(content[j+2])-2])  + str(content[j+2][ len(content[j+2])-1]) )
                                    groupsNumbers.append(content[j+3])
                                    groups.append(content[j+4])
                                    subgroups.append(content[j+5])
                                    #Add info son dos items juntos asi que los concatenamos
                                    addinfos.append( content[j+6] + content[j+7] ) 
                                    uom.append(content[j+8])
                                
                            

        
        #Creamos la dataset en formato diccionario a partir de los valores
        data = {
            'Position': positions , 
            'Description': descriptions , 
            "Executions": executions  , 
            'Code No' : codes , 
            "Group No": groupsNumbers , 
            "Group": groups , 
            "Subgroup": subgroups , 
            "Add info": addinfos ,
            "UOM": uom 
        }
                
        dataframe = pd.DataFrame(data)
                
        dataframe.to_csv('EXPORTS_CSV/'+file[0:len(file)-4] + '.csv' , index=False)
        #print(dataframe)
            

    #=========================================================================================================================

#END Funcionalidad del boton start ==================================================================================================



#--------------------------------------------------------------------------
#Crear una ventana, 
#Instancia del objeto Tk() es una ventana
ventana = Tk()
#Tamano por defecto
ventana.geometry("400x280")
#Titulo de la ventana
ventana.title("Invoices to CSV")

#----------------------------------------------------------------------------
#Creando primeros elementos
#Crear un texto en pantalla instancia de Label()
lbl = Label(ventana , text='Welcome to incoice to CSV' , font=('Verdana', 15, 'bold') ,  height=5)
#Cada elemento cuenta con su metodo pack y es para posicionar en pantalla
lbl.pack()

#Botones instancias de Button()
#los botones reciben el texto y el Evento que es la funcion que esta arriba
btn_start = Button(ventana, text='Start Convert' , command = convertToCsv , font=('Verdana', 15 ) , bg="white" , fg="black" )
#Cada elemento cuenta con su metodo pack y es para posicionar en pantalla
btn_start.pack()

#mainloop() esta monitoriando los eventos de usuario
ventana.mainloop()