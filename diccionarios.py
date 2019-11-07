print("CREACION\n")
# 1. EJEM
x=dict()
print("1. la variable 'x' es un diccionario vacio:",x)
# 2. EJEM
alimentos={"fruta":"fresa","carne":"res"}
print("2. el diccionario es:",alimentos)
# 3. EJEM
dia="domingo"
num="uno"
resul={dia:num}
print("3. el diccionario es:",resul)
# 4. EJEM
nomb_edad=dict({"jose":15,"juan":16})
print("4. nombre_edad es:",(nomb_edad))
# 5. EJEM
dato1=["nombre","edad","provincia"]
dato2=["ander",19,"chiclayo"]
datos_finales=dict(zip(dato1,dato2))
print("5. notas_finales es:",(datos_finales))
print("______..______..______..______..______..______..______..______..______..______..______..______..______\n")

print("PERTENENCIA\n")
# 1. EJEM
dias={"domingo":1,"lunes":2,"martes":3}
if "lunes" in dias:
    print("1. 'true'")
else:
    print("1. 'false'")
# 2. EJEM
meses={"enero":1,"febrero":2,"marzo":3}
if(2 not in meses):
    print("2. 'false")
else:
    print("2. 'true'")
# 3. EJEM
dni={"nombre":"ander","edad":19}
if "nombre" in dni:
    print("3. 'true'")
else:
    print("3. 'false'")
# 4. EJEM
list={"pato":2,"gato":4,"hormiga":6}
patas=4
if 4 not in list:
    print("4. '",patas,"' patas si existe en el diccionario list")
else:
    print("4. '",patas,"' patas no existe en el diccionario list")
# 5. EJEM
dat_patas={"pollo":2,"perro":4,"araña":8}
animal="araña"
if "araña" in dat_patas:
    print("5. '",animal,"' si existe en el diccionario dat_patas")
else:
    print("5. '",animal,"' no esxite en el diccionario dat_patas")
print("______..______..______..______..______..______..______..______..______..______..______..______..______\n")

print("COMPARACION\n")
# 1. EJEM
dat1={"fruta":"manzana"}
dat2={"verdura":"brocoli"}
if dat1==dat2:
    print("1. true")
else:
    print("1. false")
# 2. EJEM
n1={"matematica":11}
n2={"programacion":12}
if n1!=n2:
    print("2. true")
else:
    print("2. false")
# 3. EJEM
cod1={1:2,3:4,5:6}
cod2={1:2,3:4,4:5}
if cod1==cod2:
    print("3. true")
else:
    print("3. false")
# 4. EJEM
cand1={1:"juan"}
cand2={1:"juan"}
if cand1==cand2:
    print("4. true")
else:
    print("4. false")
# 5. EJEM
dat1={"jose":"15","juan":"16"}
dat2=dict({"jose":15,"juan":16})
if dat1==dat2:
    print("5. true")
else:
    print("5. false")
print("______..______..______..______..______..______..______..______..______..______..______..______..______\n")

print("INDEXACION\n")
# 1. EJEM
cand={1:"ander"}
print("1. ->",cand[1])
# 2. EJEM
col={"color":"negro"}
print("2. ->",col["color"])
# 3. EJEM
edad={"ander":19}
print("3. ->",edad["ander"])
# 4. EJEM
univ={"planetas":8}
print("4. ->",univ["planetas"])
# 5. EJEM
estr={"estrella":"sol"}
print("5. ->",estr["estrella"])
print("______..______..______..______..______..______..______..______..______..______..______..______..______\n")

print("LONGITUD\n")
# 1. EJEM
datos={"nombres":"ander_deyvi","apellidos":"copia_becerra"}
print("1. la longitud del diccionario datos es ->",len(datos))
# 2. EJEM
cand={1:"ander",2:"adriel",3:"tadeo","color":"negro","codigo":172386,"nota1":12,"nota2":13}
print("2. la longitud del diccionario candidatos es ->",len(cand))
# 3. EJEM
cod1={1:2,3:4,5:6}
print("3. la longitud del diccionario cod1 es ->",len(cod1))
# 4. EJEM
dato1=["nombre","edad"]
dato2=["ander",19]
datos_finales=dict(zip(dato1,dato2))
print("4. la longitud del diccionario datos_finales es ->",len(datos_finales))
# 5. EJEM
dia={"domingo":1}
print("3. la longitud del diccionario dia es ->",len(dia))
print("______..______..______..______..______..______..______..______..______..______..______..______..______\n")

print("ITERACION\n")
# 1. EJEM
candidatos={"ander":1,"adriel":2,
            "tadeo":3}
print("-> L I S T A D O")
for i in candidatos:
    print(i)
print("\n")
# 2. EJEM
pts={"pato":2,"gato":4,"hormiga":6}
print("-> L I S T A D O")
for i in pts:
    print(i)
print("\n")
#3. EJEM
pts={"pato":2,"gato":4,"hormiga":6}
print("-> L I S T A D O")
for i in pts:
    print(pts[i])
print("\n")
#4. EJEM
anim_patas={"pollo":2,"perro":4,"araña":8}
print("-> L I S T A D O")
for k,v in zip(anim_patas.keys(),anim_patas.values()):
    print(k,v)
print("\n")
#5. EJEM
alumno={"nombres   ":"ander_deyvi","apellidos":" copia_becerra",
       "codigo    ":172386,"curso ":"    programacion2","promedio  ":  11}
print("-> L I S T A D O")
for k,v in zip(alumno.keys(),alumno.values()):
    print(k,v)
print("______..______..______..______..______..______..______..______..______..______..______..______..______\n")

print("BUSQUEDA\n")
# 1. EJEM
dato={"nombres":"ander_deyvi","apellidos":"copia_becerra"}
print("1. el dato de busqueda es ->",dato.get("nombres"))
# 2. EJEM
dat1={"jose":15,"juan":16}
print("2. el dato de busqueda es ->",dat1.get("juan"))
# 3. EJEM
cod1={1:2,3:4,5:6}
print("3. el dato de busqueda es ->",cod1.get(5))
# 4. EJEM
pts={"pato":2,"gato":4,"hormiga":6}
print("4. el dato de busqueda es ->",pts.get("gato"))
# 5. EJEM
alimentos={"fruta":"fresa","carne":"res"}
print("5. el dato de busqueda es ->",alimentos.get("carne"))
