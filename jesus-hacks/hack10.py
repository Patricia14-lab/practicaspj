    #  * HACK-10 
    #  //agregar después del item 500
    #  //los alias qux y thud
    #  [100,200,300,400,500,600,700]  result >  [100,200,300,400,500,qux,thud,600,700]
    
result = [100,200,300,400,500,600,700]
result.insert(result.index(500)+1,"qux" )
result.insert(result.index("qux")+1,"thud")
print(result)

# git branch -m main hg_2_alfa
# git fetch origin
# git branch -u origin/hg_2_alfa hg_2_alfa
# git remote set-head origin -a