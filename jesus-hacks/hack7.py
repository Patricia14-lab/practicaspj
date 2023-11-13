    #  * HACK-7 
    #  //remplazar el item 300 
    #  //por tú alias
    #  [100,200,300,400,500,600,700]  result >  [100,200,foo,400,500,600,700]
    
result = [100,200,300,400,500,600,700]
for index, elemento in enumerate(result):
    if elemento == 300:
        result[index] = "alfa"
        print(result)