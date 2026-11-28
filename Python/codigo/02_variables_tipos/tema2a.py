a = 17
b = 5
print(a % b)            # 1
print(2 ** 3)           # 2
print(int(3.9))         # 3
print("3" + "4")        # 4  ← trampa
print(int("3") + 4)     # 5
print("ja" * 3)         # 6
texto = "Python"
print(texto[0], texto[-1])   # 7
print(texto[1:4])            # 8  ← cuidado con el final
print(5 == 5.0)              # 9
print(True and not False)    # 10
print("th" in texto)         # 11
x = 10
x += 5
x //= 4
print(x)                     # 12
print(type(True))            # 13