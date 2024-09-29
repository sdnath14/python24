l1=["papaya","apple","guava"]
l2=["rose",'tulip','lili']
l3=["lemontea",'masalatea','gingertea']
map=[l1,l2,l3]
print (map[1][0])
abc=['a','b','c']
position=input("name the listposition and item you want to buy:")
findletter=abc.index(position[0])
findnumber=int(position[1])-1
map[findnumber][findletter] = "added to cart"
print(f"{l1}\n{l2}\n{l3}")

