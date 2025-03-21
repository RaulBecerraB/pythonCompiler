'''
Lenguajes y Autómatas II
"Notación Infija, Prefija y Postfija"
Becerra Barceló José Raúl. 
Diaz Sanches Edwin Ulises. 
Ferrer Chacón Diego Felipe. 
7SA 
E21080774 
E21081367 
E21080738
'''

from utils import procesar_expresion

def main():
    print("Calculadora de notaciones infija, prefija y postfija")
    print("Operaciones soportadas: +, -, *, /, ^, √")
    print("Agrupaciones soportadas: (), [], {}")
    print("Ingrese 'salir' para terminar")
    
    while True:
        expresion = input("\nIngrese una expresión infija: ")
        if expresion.lower() == 'salir':
            break
        
        resultado = procesar_expresion(expresion)
        
        if "error" in resultado:
            print(f"\n{resultado['error']}")
            if "infija" in resultado:
                print(f"Infija: {resultado['infija']}")
                print(f"Postfija: {resultado['postfija']}")
                print(f"Prefija: {resultado['prefija']}")
        else:
            print("\nNotaciones:")
            print(f"Infija: {resultado['infija']}")
            print(f"Postfija: {resultado['postfija']}")
            print(f"Prefija: {resultado['prefija']}")
            print(f"Resultado: {resultado['resultado']}")

if __name__ == "__main__":
    main()