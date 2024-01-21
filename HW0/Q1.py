a = 0 #starting point
b = 6.720592 #end point
i = 100000000 #number of rectangles 
w = (b - a) / i #width
result = sum(w * ((j*w)**3) for j in range(i)) 
print(result)