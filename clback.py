def mafonction():
    print("test")
    return 6

a = 5
b = mafonction

print("a:", a, "| b:",b())
print()


# def add_callback(n, operateur):
def add_callback(a, b):
    return a+b

def mult_callback(a, b):
    return a*b

def sous_callback(a, b):
    return a-b

def power_callback(a, b):
    return pow(a, b)

def afficher_table(n, operateur, opclbk):
    for i in range(1, 10):
        print(n, operateur, i, "=", opclbk(n, i))

afficher_table(5, "+", add_callback)
print()
afficher_table(6, "*", mult_callback)
print()
afficher_table(7, "-", lambda a, b : a-b) # Lambda Anonymous function
print()
afficher_table(2, "^", power_callback)
