x=1.0
y=2.3
z=3.4
promedio=0
array= []
suma=0
array.append(x)
array.append(y)
array.append(z)

for i in range(len(array)):
    suma=suma+array[i]

promedio=suma/len(array)

print(float(promedio))