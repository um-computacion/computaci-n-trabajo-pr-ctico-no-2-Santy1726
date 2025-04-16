def is_palindrome(mystring):
    mystring = ''.join(c.lower() for c in mystring if c.isalnum())
    print(f"Cadena procesada: {mystring}") 
    for indice in range(0, len(mystring)):
        print(f"{mystring[indice]} --> {mystring[-(indice + 1)]}")  
        if mystring[indice] != mystring[-(indice + 1)]:
            print("no es un palíndromo")
            return False
    return True



