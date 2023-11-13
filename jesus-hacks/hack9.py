   #  * HACK-9
    #  //agregar tú alias al inicio
    #  [100,200,300,400,500,600,700]  result >  [foo,100,200,300,400,500,600,700]
    
result = [100,200,300,400,500,600,700]
result.insert(0,"alfa")
print(result)