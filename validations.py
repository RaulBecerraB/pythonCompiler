import re

# Función para validar la sintaxis de la expresión infija
def validar_expresion(expresion):
    # Eliminar espacios en blanco
    expresion = expresion.replace(" ", "")
    
    # Verificar paréntesis balanceados
    pila = []
    parentesis_abiertos = "([{"
    parentesis_cerrados = ")]}"
    pares_parentesis = {')': '(', ']': '[', '}': '{'}
    
    for char in expresion:
        if char in parentesis_abiertos:
            pila.append(char)
        elif char in parentesis_cerrados:
            if not pila or pila.pop() != pares_parentesis[char]:
                return False, "Error: Paréntesis desbalanceados"
    
    if pila:
        return False, "Error: Paréntesis desbalanceados"
    
    # Verificar operadores y operandos
    # Patrones inválidos: operadores consecutivos, operadores al inicio/fin, etc.
    if re.search(r'[+\-*/^√][+*/^√]', expresion):
        return False, "Error: Operadores consecutivos no permitidos"
    
    if re.search(r'^[+*/^√]', expresion) or re.search(r'[+\-*/^√]$', expresion):
        return False, "Error: Expresión no puede comenzar/terminar con operador (excepto -)"
    
    # Verificar que no haya paréntesis vacíos o conteniendo solo operadores
    if re.search(r'[\(\[\{][\)\]\}]', expresion) or re.search(r'[\(\[\{][+\-*/^√][\)\]\}]', expresion):
        return False, "Error: Paréntesis vacíos o con solo operadores"
    
    # Verificar caracteres no válidos
    validos = set("0123456789+-*/^√()[]{}.")
    for char in expresion:
        if char not in validos:
            return False, f"Error: Carácter no válido '{char}'"
    
    return True, "Expresión válida"

# Función para tokenizar la expresión infija (separar en tokens sin espacios)
def tokenizar(expresion):
    expresion = expresion.replace(" ", "")
    tokens = []
    i = 0
    
    while i < len(expresion):
        # Si es un dígito, extraer el número completo
        if expresion[i].isdigit() or (expresion[i] == '.' and i+1 < len(expresion) and expresion[i+1].isdigit()):
            j = i
            punto_encontrado = False
            
            while j < len(expresion) and (expresion[j].isdigit() or expresion[j] == '.'):
                if expresion[j] == '.':
                    if punto_encontrado:  # Ya había un punto, no puede haber dos
                        break
                    punto_encontrado = True
                j += 1
            
            tokens.append(expresion[i:j])
            i = j
        # Si es un paréntesis o operador, agregar como token individual
        elif expresion[i] in '+-*/^√()[]{}':
            tokens.append(expresion[i])
            i += 1
        else:
            i += 1
    
    return tokens 