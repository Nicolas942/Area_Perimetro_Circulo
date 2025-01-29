import math 

print("###########################")
print("area perimetro del circulo")
print("###########################")
# input

r = input("Digite el valor del radio: ")
r = int(r)

# Prosessing

p = 2 * math.pi * r
a = math.pi*r**2

# Output

print("###########################")
print("El area es: "+ str (a))
print("El perimetro es: "+ str (p))
print("###########################")