G=[]
for a in range(1,1000):
    if a%2!=0 and a%3!=0 and a%5!=0 and a%7!=0 and a%11 !=0 and a%a**0.5!=0:
        G.append(a)
for i in range(0,1000):
    for b in range(1,1000):
        if 4*b+117==G[i]:
            print(G[i])
        
        
    
    
    
