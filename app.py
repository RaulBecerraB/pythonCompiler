from collections import deque

# Convierte una expresión infija a postfija
def infija_posfija(expresion):
    salida = []
    pila = deque()
    precedencia = {'+': 1, '-': 1, '*': 2, '/': 2, '^': 3, '√': 3, '(': 0}
    tokens = expresion.split()
    
    for token in tokens:
        if token.isnumeric():
            salida.append(token)
        elif token == '(':
            pila.append(token)
        elif token == ')':
            while pila and pila[-1] != '(':
                salida.append(pila.pop())
            pila.pop()  # Eliminar el '(' de la pila
        else:
            while pila and precedencia[pila[-1]] >= precedencia[token]:
                salida.append(pila.pop())
            pila.append(token)
    
    while pila:
        salida.append(pila.pop())
    
    return ' '.join(salida)

# Resuelve una expresión en notación postfija
def res_postfija(expresion):
    stack = []
    tokens = expresion.split()
    
    for token in tokens:
        if token.isnumeric():
            stack.append(int(token))
        else:
            b = stack.pop()
            a = stack.pop()
            if token == '+':
                stack.append(a + b)
            elif token == '-':
                stack.append(a - b)
            elif token == '*':
                stack.append(a * b)
            elif token == '/':
                stack.append(a / b)
            elif token == '^':
                stack.append(a ** b)
            elif token == '√':
                stack.append(a ** (1/b))
    
    return stack.pop()

#expresion_infija = "( 3 + 4 / 3 - 1 * 5 ) + 8 / 2"
#expresion_postfija = infija_posfija(expresion_infija)
#print(f"Expresión postija: {expresion_postfija}")

posfija = "3 5 + 2 * 8 4 / -"
print(res_postfija(posfija))