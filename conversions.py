from collections import deque
import re

# Convierte una expresión infija a postfija
def infija_a_postfija(tokens):
    salida = []
    pila = deque()
    precedencia = {'+': 1, '-': 1, '*': 2, '/': 2, '^': 3, '√': 3}
    
    for token in tokens:
        # Si es un número
        if re.match(r'^[0-9]+(\.[0-9]+)?$', token):
            salida.append(token)
        # Si es un paréntesis de apertura
        elif token in '([{':
            pila.append(token)
        # Si es un paréntesis de cierre
        elif token in ')]}':
            parentesis_correspondiente = {')', '(', ']', '[', '}', '{'}[token]
            while pila and pila[-1] not in '([{':
                salida.append(pila.pop())
            if pila and pila[-1] == parentesis_correspondiente:
                pila.pop()  # Eliminar el paréntesis de apertura
        # Si es un operador
        else:
            while (pila and pila[-1] not in '([{' and 
                   pila[-1] in precedencia and 
                   precedencia.get(pila[-1], 0) >= precedencia.get(token, 0)):
                salida.append(pila.pop())
            pila.append(token)
    
    # Vaciar la pila al final
    while pila:
        if pila[-1] in '([{':
            pila.pop()  # Ignorar paréntesis no cerrados (aunque no debería ocurrir si la validación es correcta)
        else:
            salida.append(pila.pop())
    
    return salida

# Convierte una expresión infija a prefija
def infija_a_prefija(tokens):
    # Invertir la expresión y los paréntesis
    tokens_invertidos = []
    for token in reversed(tokens):
        if token == '(':
            tokens_invertidos.append(')')
        elif token == ')':
            tokens_invertidos.append('(')
        elif token == '[':
            tokens_invertidos.append(']')
        elif token == ']':
            tokens_invertidos.append('[')
        elif token == '{':
            tokens_invertidos.append('}')
        elif token == '}':
            tokens_invertidos.append('{')
        else:
            tokens_invertidos.append(token)
    
    # Convertir a postfija la expresión invertida
    postfija_invertida = infija_a_postfija(tokens_invertidos)
    
    # Invertir el resultado
    return list(reversed(postfija_invertida))

# Evalúa una expresión postfija
def evaluar_postfija(tokens):
    stack = []
    
    for token in tokens:
        if re.match(r'^[0-9]+(\.[0-9]+)?$', token):
            stack.append(float(token))
        else:
            if len(stack) < 2:
                return None, "Error: Expresión mal formada"
            
            b = stack.pop()
            a = stack.pop()
            
            try:
                if token == '+':
                    stack.append(a + b)
                elif token == '-':
                    stack.append(a - b)
                elif token == '*':
                    stack.append(a * b)
                elif token == '/':
                    if b == 0:
                        return None, "Error: División por cero"
                    stack.append(a / b)
                elif token == '^':
                    stack.append(a ** b)
                elif token == '√':
                    if a < 0 and b % 2 == 0:
                        return None, "Error: Raíz par de número negativo"
                    stack.append(a ** (1/b))
            except Exception as e:
                return None, f"Error matemático: {str(e)}"
    
    if len(stack) != 1:
        return None, "Error: Expresión mal formada"
    
    return stack[0], None 