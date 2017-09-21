nums = input()
nums = nums.split(" ")

a = float(nums[0])
b = float(nums[1])
c = float(nums[2])




areaA = (a*c)/ 2
areaB = 3.14159 * c**2
areaC = ((a+b)*c)/2
areaD = b*b

areaE = a*b


print("TRIANGULO: %.3f" %areaA)
print("CIRCULO: %.3f" %areaB)
print("TRAPEZIO: %.3f" %areaC)
print("QUADRADO: %.3f" %areaD)
print("RETANGULO: %.3f" %areaE)