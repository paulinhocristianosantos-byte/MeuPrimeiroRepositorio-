numero1 = int(input("Digitie o primeiro numero inteiro:"))
numero2 = int(input("Digite o segundo numero inteiro:"))
numero3 = int(input("Digite o terceiro numero inteiro:"))

#Primeiro bloco condicional para achar o menor numero 
if numero1 < numero2 and numero1< numero3:
    print ("O menor numero é:", numero1)
else:
    if numero2 < numero1 and numero2 < numero3:
     print("O menor numero é:", numero2)
    else:
       if numero3 <numero1 and numero3 < numero2:
          print("O menor numero é:", numero3)

#segundo bloco condicional para achar o numero do meio, fazendo o uso de ambas condicionais 
if numero1 > numero2 and numero1 < numero3 or numero1 < numero2 and numero1 > numero3:
   print("O numero do meio é: ", numero1)
else:
   if numero2 > numero1 and numero2 < numero3 or numero2 < numero1 and numero2 > numero3:
        print("O numero do meio é: ", numero2)
    
        if numero3 > numero1 and numero3 < numero2 or numero3 < numero1 and numero3 > numero2:
            print("O numero do meio é: ", numero3)

#Terceiro bloco condicional para achar o maior numero
if numero1 > numero2 and numero1 > numero3:
    print("O maior numero é: ", numero1)
else:
    if numero2 > numero1 and numero2 > numero3:
        print("O maior numero é: ", numero2)
    else:
        if numero3 > numero1 and numero3 > numero2:
            print("O maior numero é: ", numero3)

        
        