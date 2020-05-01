def exibeMsg():
    print ("Conversor Celsius-Fahrenheit")
    print ("Digite c para converter de Celsius para Fahrenheit")
    print ("Digite f para converter de Fahrenheit para Celsius")
    comando = input("Digite aqui: ")
    return teste(comando)
    
def teste(comando):
    if comando == "c":
        start = int(input("Digite a temperatura a ser convertida Celsius-Fahrenheit: "))
        return exibeCelToFah(start,end=0)
        
    elif comando == "f":
        start = int(input("Digite a temperatura a ser convertida Fahrenheit-Celsius: "))
        return exibeFahToCel(start,end=0)

def exibeCelToFah(start,end=0):
    calculocf = (start//5) * 9 + 32
    end = calculocf
    return end
    
def exibeFahToCel(start,end=0):
    calculofc = (start - 32)//9 * 5
    end = calculofc
    return end

def main ():
    print (exibeMsg())

main()
