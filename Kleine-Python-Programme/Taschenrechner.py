#!/usr/bin/env python
# coding: utf-8


print("***_______(•‿•)_______***") 
print()
print("Hallo, ich bin dein kleiner Taschenrechner! :)")
print()
print("Diese Operatoren kenne ich schon:")
print("+ : Addieren")
print("- : Subtrahieren")
print("* : Multiplizieren")
print("/ : Dividieren")
print("% : Modulo Division")
print()

print("**************************") 
print()
zahl1 = int(input("Gebe bitte deine erste Zahl ein: "))

    
while True:
    operator = input("Was möchtest du mit der Zahl machen? ")
    if operator not in ('+', '-', '*', '/', '%'):
        print()
        print("Oh nein!")
        print("Den Operator kenne ich noch nicht ._.")
        print("Bitte verwende nur +, -, *, / oder %")
        continue
    zahl2 = int(input("Gebe bitte deine zweite Zahl ein: "))
    print()
    print("**************************") 
    print()
    
    if operator == "+":
        ergebnis = zahl1 + zahl2

    elif operator == "-":
        ergebnis = zahl1 - zahl2

    elif operator == "*":
        ergebnis = zahl1 * zahl2

    elif operator == "/":
        ergebnis = zahl1 / zahl2

    elif operator == "%":
        ergebnis = zahl1 % zahl2

    print()
    print(zahl1, operator, zahl2, "=", ergebnis)
    print()
    print()
    print("**************************")
    print()
    user_input = input("Möchtest du mit dem Ergebnis weiter rechnen? ")
    if user_input.lower() == "ja":
        zahl1 = ergebnis
    else:
        zahl1 = int(input("Dann gebe bitte eine neue Zahl ein: "))





