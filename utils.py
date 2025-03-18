from validations import validar_expresion, tokenizar
from conversions import infija_a_postfija, infija_a_prefija, evaluar_postfija

# Función que integra las conversiones y evaluación
def procesar_expresion(expresion_infija):
    # Validar la expresión
    es_valida, mensaje = validar_expresion(expresion_infija)
    if not es_valida:
        return {"error": mensaje}
    
    # Tokenizar la expresión
    tokens = tokenizar(expresion_infija)
    
    # Convertir a las diferentes notaciones
    tokens_postfija = infija_a_postfija(tokens)
    tokens_prefija = infija_a_prefija(tokens)
    
    # Mostrar las notaciones
    infija_formateada = ' '.join(tokens)
    postfija_formateada = ' '.join(tokens_postfija)
    prefija_formateada = ' '.join(tokens_prefija)
    
    # Evaluar la expresión
    resultado, error = evaluar_postfija(tokens_postfija)
    
    if error:
        return {
            "error": error,
            "infija": infija_formateada,
            "postfija": postfija_formateada,
            "prefija": prefija_formateada
        }
    
    return {
        "infija": infija_formateada,
        "postfija": postfija_formateada,
        "prefija": prefija_formateada,
        "resultado": resultado
    } 