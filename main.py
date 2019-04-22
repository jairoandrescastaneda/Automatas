from Lenguaje import Lenguaje
from Node import Nodo
import pdb 
#pdb.set_trace()
lenguaje = []
nodoInicial = []
nodoTranformado = []


def crearNodo(listadoGeneador):
    nombre = ''
    for generador in listadoGeneador:
        if nombre:
            
            nombre=nombre+'-'+generador.getNombre()
        else:
            nombre = generador.getNombre()

    return nombre

def validateNodoTranformado(nombre):
    listaNombre = nombre.split('-')
    for nodo in nodoTranformado:
        listanombreRegistrados = nodo.getNombre().split('-')
        if len(listaNombre)==len(listanombreRegistrados):
            if validarListasNombres(listaNombre,listanombreRegistrados):
                return nodo
            
    
    return None


def validarListasNombres(listaNombreValidar,listaNombreNodo):
    match = 0
    for nombrevalidar in listaNombreValidar:
        for nombrenodo in listaNombreNodo:
            if nombrevalidar==nombrenodo:
                match+=1
    if match==len(listaNombreNodo):
        return True
    return False

    
def devolverGeneradoresNuevo():
    generador = {}
    for letra in lenguaje:
        generador[letra] = []
    
    return generador


def inicializacionNodo():
    for nodo in nodoInicial:
        generadores = nodo.getGenerador()
        for key,value in generadores.items():
            listageneradores = generadores[key]
            if len(listageneradores)>1:
                nuevoNodo = crearNodo(listageneradores)
                nodoValidado = validateNodoTranformado(nuevoNodo)
                if nodoValidado==None:
                    nuevo = Nodo(nuevoNodo)
                    nuevo.setGenerador(devolverGeneradoresNuevo())
                    generadores[key] = [nuevo]
                    nodoTranformado.append(nuevo)
                else:

                    generadores[key] = [nodoValidado]
           
        nodo.setGenerador(generadores)
        nodo.setEvaluado()
        nodoTranformado.append(nodo)



def obtenerInstancias(nombreNodo):
  
    nombreNodos = nombreNodo.split('-')
    nodos = []
    
    for nombre in nombreNodos:
        
        nodos.append(validateNodoTranformado(nombre))
    return nodos









def contactenacionNombreNodo(nodosGenera):
    concateacion = ''
    for nombre in nodosGenera:
        if concateacion:
            concateacion = concateacion+'-'+nombre
        else:
            concateacion = nombre
    
    return concateacion






def generadorinLetra(letra,nodos):
    listanombreNodos = []
    for nodo in nodos:
        
        generadores = nodo.getGenerador()
        generadorinletra = generadores[letra]
        nodoNombres = generadorinletra[0].getNombre().split('-') 

        for nombre in nodoNombres:
            listanombreNodos.append(nombre)

    return listanombreNodos
        
            

def limpiarNombreNodo(nodosNombreGenera):
    
    for contadorNodo in range(len(nodosNombreGenera)):
        if contadorNodo==(len(nodosNombreGenera)-1):
            if nodosNombreGenera[contadorNodo]==nodosNombreGenera[(len(nodosNombreGenera)-1)]:
                nodosNombreGenera.pop((len(nodosNombreGenera)-1))
        else:


            for contadorNodocompara in range(contadorNodo+1,len(nodosNombreGenera)-1):
                if nodosNombreGenera[contadorNodo]==nodosNombreGenera[contadorNodocompara]:
                    nodosNombreGenera.pop(contadorNodocompara)
    
    return nodosNombreGenera



def conversionNodos():
    contadorlenguaje = 0
    for nodo in nodoTranformado:
        
        if nodo.getEvaluado()==False:
            nodo.setEvaluado()
            
            nodos = obtenerInstancias(nodo.getNombre())
            generadores = nodo.getGenerador()
            for letra in lenguaje:
                
                nodosNombreGenera = generadorinLetra(letra,nodos)
                nodosNombreGenera = limpiarNombreNodo(nodosNombreGenera)
                nombreNodo = contactenacionNombreNodo(nodosNombreGenera)
                nodovalidado = validateNodoTranformado(nombreNodo)
                if nodovalidado == None:
                    nodoNuevo = Nodo(nombreNodo)
                    generadores[letra] = [nodoNuevo]
                    nodo.setGenerador(generadores)
                   
                    nodoTranformado.append(nodoNuevo)
                else:
                    generadores[letra] = [nodovalidado]
                    nodo.setGenerador(generadores)

                
                    


def buscarNodoInicial(nombre):
    for nodo in nodoInicial:
        if nodo.getNombre()==nombre:
            return nodo

def marcarNodoTerminal(nombreNodosTerminales):
    nodosTerminales = nombreNodosTerminales.split(',')

    for nodot in nodosTerminales:
        
        nodoTerminal = buscarNodoInicial(nodot)
        nodoTerminal.setIsTerminal()
    

def devovlerNodoTerminales():
    terminales = []
    for nodoT in nodoInicial:
        if nodoT.isTerminal():
            terminales.append(nodoT)
    return terminales





def marcarTerminalTranformado():
    terminales = devovlerNodoTerminales()
    for nodot in terminales:
        for nodos in nodoTranformado:
            listanombre = nodos.getNombre().split('-')
            if nodot.getNombre() in listanombre:
                nodos.setIsTerminal()
                


def pedirDatos():
    
    cantidadNodos = int(input('Ingrese la cantidad de nodos  (Valor numerico ): '))
    cantidadLenguaje = int(input('Ingrese la cantidad de letras del   lenguaje (Valor numerico)  :  '))

    for numlenguaje in range(cantidadLenguaje):
        entrada = raw_input("Ingrese la  letra del lenguaje #  "+str((numlenguaje)) + "   :    ")
        lenguaje.append(entrada)
        
    for numNodo in range(cantidadNodos):
        n = Nodo('q'+str(numNodo))
        nodoInicial.append(n)
        
    print('Estos son los Nodos disponibles')

    for nodo in nodoInicial:
        print(nodo.getNombre())
        
    nodoPrincipio = raw_input("Digite el nombre del nodo inicial (debe ser escrito como los nombrados arriba): ")
    
    nodTerminaless = raw_input('Digite el nombre de los nodos terminales separados por comas  eg.(q0,q1,q2) : ')

   


    nodoentrada = buscarNodoInicial(nodoPrincipio)
    if nodoentrada is None:
        print('Ha ocurrido un error el nodo inicial debe escribirse tal como esta los nodos existentes')
        
        return

    nodoentrada.setIsIinicial()
    try:

        marcarNodoTerminal(nodTerminaless)
    except:
        print(" Los nodos Terminales deben separarse con una ',' eg (q1,q0,q2)  y deben existir dentro del contexto")
        return


    print(' Porfavor digite las reglas  usando el formato eg (q0,0->q1) si genera mas de uno separe con una coma')

    for nodo in nodoInicial:
       
        generadorreglas = {}
        
        for letra in lenguaje:
            
           
            entrada = raw_input(" "+nodo.getNombre()+','+str(letra)+'--->  : ')
            reglasNodo = [] 
            listanodos = entrada.split(',')
         
            for nodoNombre in listanodos:
                
                nodoencontrado = buscarNodoInicial(nodoNombre)
                reglasNodo.append(nodoencontrado)
               
            
           
            generadorreglas[letra] = reglasNodo
           
        
            nodo.setGenerador(generadorreglas)
            
            
    inicializacionNodo()
    conversionNodos()
    marcarTerminalTranformado()

    print('           ')
    print('          El AFD resultante es :            ')
    for node in nodoTranformado:
        diccionario = node.getGenerador()
        try:
          for key,value in diccionario.items():
              print(node.getNombre()+','+str(key)+'---> '+str(value[0].getNombre()))
              
           
        except:
            print('error')

        if node.getIsIinicial():
            print(node.getNombre()+ ' Es el nodo inicial')

        if node.isTerminal():
            print(node.getNombre()+' es un Terminal ' )
        print('-----------------------------------')
            






        






def main():
    lenguaje.append('0')
    lenguaje.append('1')
    lenguaje.append('2')
    lenguaje.append('3')
    
    n = Nodo('q0')
    n1 = Nodo('q1')
    n2 = Nodo('q2')
    n3 = Nodo('q3')
    n4 = Nodo('q4')


    generador = {'0':[n1],'1':[n2],'2':[n4],'3':[n4]}

    n.setGenerador(generador)
    nodoInicial.append(n)

    generador = {'0':[n2,n3],'1':[n4],'2':[n2],'3':[n1]}
    n1.setGenerador(generador)

    
    nodoInicial.append(n1)
    generador = {'0':[n],'1':[n1,n4],'2':[n1],'3':[n1]}
    n2.setGenerador(generador)
    nodoInicial.append(n2)

    generador = {'0':[n1],'1':[n],'2':[n2],'3':[n]}
    n3.setGenerador(generador)
    n3.setIsTerminal()
    nodoInicial.append(n3)

    generador = {'0':[n1,n2],'1':[n3,n4],'2':[n1],'3':[n]}
    n4.setGenerador(generador)
    nodoInicial.append(n4)
    
    
    
   
    inicializacionNodo()
    conversionNodos()
    marcarTerminalTranformado()
    for node in nodoTranformado:
        diccionario = node.getGenerador()
        try:
            print('nombre : '+node.getNombre())
            print('Terminal ')
            print(node.isTerminal())
            #print(diccionario['1'][0].getNombre())
        except:
            print('error')



    


        

   

    
#main()
pedirDatos()
