### Codigo para tranformar un AFND a un AFD

**Requisitos**

python >= 3.5

**Como Ejecutarlo**
```
python3 main.py

```

**Ejemplo de Ejecucion**

Primero solicita la cantidad de nodos y cantidad de letras del lenguaje .
por defecto y para fines de practicidad el crea los nombres de los nodos, pero generalmente como 
siempre es en orden,  es pasarlos a sus variables 


![](http://i.prntscr.com/XO2smrlQSLe_67uc0IcjAg.png)

Luego de digitar la cantidad nos solicita que ingresemos  las letras del lenguaje , despues de digitarlas
nos crea los nodos usando la nomenclatura 'q0', 'q1' , 'q2' ....


![](http://i.prntscr.com/az67WDmpTf6AgBpNyMoh6Q.png)

Elegimos el nodo inicial o nodo de entrada y los nodos terminales es importante que se llamen igual
a la nomenclatura mostrada anteriormente , y el nodo de entrada debe ser uno solo y seguido se digitan las reglas 
de generacion que cumple con el formato

'q0,0->q1,q2' donde q0 es el nodo a analisar , 0 es la letra del lenguaje y q1,q2 los destinos al ser
valores multiples deben separarse con ',' 


![](http://i.prntscr.com/XzyYArsiSaWyEiYKQZBUSQ.png)

**Resultado**

Al final el programa generara el AFD resultante , diciendonos cuales son los terminales y cual es el nodo
de entrada

![](http://i.prntscr.com/hcFdksViQoeDy9rTbAURoA.png)


El resultado tiene el siguiente formato

```
q1,1---> q1
q1,0---> q0
q1 es un Terminal

```

**y si es el nodo inicial se agregara**

```
q0 Es el nodo inicial

```

Cualquier problema o bug no dude en reportarlo