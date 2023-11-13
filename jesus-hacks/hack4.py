
    #  * HACK-4
    #  //eliminar los items 300 y 500
    #  [100,200,300,400,500,600,700]  result >  [100,200,400,600,700]
    
result =  [100,200,300,400,500,600,700] 
for elemento in result:
    if elemento == 300:
        result.remove(elemento)
    if elemento == 500:
        result.remove(elemento)
print(result)
