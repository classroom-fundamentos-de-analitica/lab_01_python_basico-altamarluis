"""
Laboratorio de Programación Básica en Python para Manejo de Datos
-----------------------------------------------------------------------------------------

Este archivo contiene las preguntas que se van a realizar en el laboratorio.

No puede utilizar pandas, numpy o scipy. Se debe utilizar solo las funciones de python
básicas.

Utilice el archivo `data.csv` para resolver las preguntas.


"""


def pregunta_01():
    """
    Retorne la suma de la segunda columna.

    Rta/
    214

    """
    a = 0
    with open("data.csv") as f:
        for l in f:
            l = l.split()
            a+=int(l[1])
    
    return a



def pregunta_02():
    """
    Retorne la cantidad de registros por cada letra de la primera columna como la lista
    de tuplas (letra, cantidad), ordendas alfabéticamente.

    Rta/
    [
        ("A", 8),
        ("B", 7),
        ("C", 5),
        ("D", 6),
        ("E", 14),
    ]

    """
    count ={}
    with open("data.csv") as f:
        for l in f:
            l = l.split()
            if l[0] in count:
                count[l[0]]+=1
            else:
                count[l[0]]=1
    return (sorted(count.items()))


def pregunta_03():
    """
    Retorne la suma de la columna 2 por cada letra de la primera columna como una lista
    de tuplas (letra, suma) ordendas alfabeticamente.

    Rta/
    [
        ("A", 53),
        ("B", 36),
        ("C", 27),
        ("D", 31),
        ("E", 67),
    ]

    """
    count ={}  
    with open("data.csv") as f:
        for l in f:
            l = l.split()
            if l[0] in count:
                count[l[0]]+=int(l[1])
            else:
                count[l[0]]=int(l[1])          
    return (sorted(count.items()))


def pregunta_04():
    """
    La columna 3 contiene una fecha en formato `YYYY-MM-DD`. Retorne la cantidad de
    registros por cada mes, tal como se muestra a continuación.

    Rta/
    [
        ("01", 3),
        ("02", 4),
        ("03", 2),
        ("04", 4),
        ("05", 3),
        ("06", 3),
        ("07", 5),
        ("08", 6),
        ("09", 3),
        ("10", 2),
        ("11", 2),
        ("12", 3),
    ]

    """
    count ={}  
    with open("data.csv") as f:
        for l in f:
            l = l.split()
            month = l[2].split("-")[1]
            if month in count:
                count[month]+=1
            else:
                count[month]=1
    return(sorted(count.items()))


def pregunta_05():
    """
    Retorne una lista de tuplas con el value maximo y minimo de la columna 2 por cada
    letra de la columa 1.

    Rta/
    [
        ("A", 9, 2),
        ("B", 9, 1),
        ("C", 9, 0),
        ("D", 8, 3),
        ("E", 9, 1),
    ]

    """
    count ={}  
    with open("data.csv") as f:
        for l in f:
            l = l.split()

            if l[0] in count:
                if int(l[1]) > int(count[l[0]][0]):
                    count[l[0]][0]=int(l[1])

                elif int(l[1]) < int(count[l[0]][1]):
                    count[l[0]][1]=int(l[1]) 

            else:
                count[l[0]]=[int(l[1]),int(l[1])]
    result = sorted(count.items())
    max_min = []
    for i in result:
        max_min.append((i[0],i[1][0],i[1][1]))
    return max_min


def pregunta_06():
    """
    La columna 5 codifica un diccionario donde cada cadena de tres letras corresponde a
    una key y el value despues del caracter `:` corresponde al value asociado a la
    key. Por cada key, obtenga el value asociado mas pequeño y el value asociado mas
    grande computados sobre todo el archivo.

    Rta/
    [
        ("aaa", 1, 9),
        ("bbb", 1, 9),
        ("ccc", 1, 10),
        ("ddd", 0, 9),
        ("eee", 1, 7),
        ("fff", 0, 9),
        ("ggg", 3, 10),
        ("hhh", 0, 9),
        ("iii", 0, 9),
        ("jjj", 5, 17),
    ]

    """
    count = {}    
    with open("data.csv") as f:
        for l in f:
            l = l.split()
            dic = l[4].split(",")
            for i in dic:
                key = i.split(":")[0]
                value = int(i.split(":")[1])
                if key in count:
                    if value > count[key][0]:
                        count[key][0] = value
                    elif value < count[key][1]:
                        count[key][1] = value
                else:
                    count[key] = [value,value]
    result = sorted(count.items())    
    max_min = []
    for i in result:
        max_min.append((i[0],i[1][1],i[1][0]))

    return max_min


def pregunta_07():
    """
    Retorne una lista de tuplas que asocien las columnas 0 y 1. Cada tupla contiene un
    valor posible de la columna 2 y una lista con todas las letras asociadas (columna 1)
    a dicho valor de la columna 2.

    Rta/
    [
        (0, ["C"]),
        (1, ["E", "B", "E"]),
        (2, ["A", "E"]),
        (3, ["A", "B", "D", "E", "E", "D"]),
        (4, ["E", "B"]),
        (5, ["B", "C", "D", "D", "E", "E", "E"]),
        (6, ["C", "E", "A", "B"]),
        (7, ["A", "C", "E", "D"]),
        (8, ["E", "D", "E", "A", "B"]),
        (9, ["A", "B", "E", "A", "A", "C"]),
    ]

    """
    count ={}
    with open("data.csv") as f:
        for l in f:
            l = l.split()
            if l[1] in count:
                count[l[1]].append(l[0])
            else:
                count[l[1]]=[l[0]]
    return sorted(count.items())


def pregunta_08():
    """
    Genere una lista de tuplas, donde el primer elemento de cada tupla contiene  el valor
    de la segunda columna; la segunda parte de la tupla es una lista con las letras
    (ordenadas y sin repetir letra) de la primera  columna que aparecen asociadas a dicho
    valor de la segunda columna.

    Rta/
    [
        (0, ["C"]),
        (1, ["B", "E"]),
        (2, ["A", "E"]),
        (3, ["A", "B", "D", "E"]),
        (4, ["B", "E"]),
        (5, ["B", "C", "D", "E"]),
        (6, ["A", "B", "C", "E"]),
        (7, ["A", "C", "D", "E"]),
        (8, ["A", "B", "D", "E"]),
        (9, ["A", "B", "C", "E"]),
    ]

    """
    count ={}
    with open("data.csv") as f:
        for l in f:
            l = l.split()
            if l[1] in count:
                if l[0] not in count[l[1]]:
                    count[l[1]].add(l[0])
            else:
                count[l[1]]={l[0]}
    

    result = []
    for i in sorted(count.items()):
        result.append((int(i[0]),sorted(list(i[1]))))
    return result


def pregunta_09():
    """
    Retorne un diccionario que contenga la cantidad de registros en que aparece cada
    valor de la columna 5.

    Rta/
    {
        "aaa": 13,
        "bbb": 16,
        "ccc": 23,
        "ddd": 23,
        "eee": 15,
        "fff": 20,
        "ggg": 13,
        "hhh": 16,
        "iii": 18,
        "jjj": 18,
    }

    """
    count ={}  
    with open("data.csv") as f: 
        for l in f:
            l = l.split()
            dic = l[4].split(",")
            for i in dic:
                key = i.split(":")[0]
                if key in count:
                    count[key]+=1
                else:
                    count[key]=1
    result = dict(sorted(count.items()))   
    return result


def pregunta_10():
    """
    Retorne una lista de tuplas contengan por cada tupla, la letra de la columna 1 y la
    cantidad de elementos de las columnas 4 y 5.

    Rta/
    [
        ("E", 3, 5),
        ("A", 3, 4),
        ("B", 4, 4),
        ...
        ("C", 4, 3),
        ("E", 2, 3),
        ("E", 3, 3),
    ]


    """
    total = []
    with open("data.csv") as f:
        for l in f:
            l = l.split()
            gg = l[3].split(",") 
            dic = l[4].split(",")            
            total.append((l[0],len(gg),len(dic)))

    return total


def pregunta_11():
    """
    Retorne un diccionario que contengan la suma de la columna 2 para cada letra de la
    columna 4, ordenadas alfabeticamente.

    Rta/
    {
        "a": 122,
        "b": 49,
        "c": 91,
        "d": 73,
        "e": 86,
        "f": 134,
        "g": 35,
    }


    """
    count ={}  
    with open("data.csv") as f:
        for l in f:
            l = l.split()
            dic = l[3].split(",")
            for i in dic:
                if i in count:
                    count[i]+=int(l[1])
                else:
                    count[i]=int(l[1])
    result = dict(sorted(count.items()))
    return result


def pregunta_12():
    """
    Genere un diccionario que contengan como clave la columna 1 y como valor la suma de
    los valores de la columna 5 sobre todo el archivo.

    Rta/
    {
        'A': 177,
        'B': 187,
        'C': 114,
        'D': 136,
        'E': 324
    }

    """
    count ={}
    with open("data.csv") as f:
        for l in f:
            l = l.split()
            key = (l[0]) 
            dic = l[4].split(",")
            for i in dic:
                value = int(i.split(":")[1])
                if key in count:
                    count[key]+=value
                else:
                    count[key]=value

    result = dict(sorted(count.items()))
    return result
