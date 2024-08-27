# Función para construir el array de prefijos 
def construir_array_kmp(subcadena):
    longitud = len(subcadena)
    lps = [0] * longitud  
    largo = 0  
    i = 1

    while i < longitud:
        if subcadena[i] == subcadena[largo]:
            largo += 1
            lps[i] = largo
            i += 1
        else:
            if largo != 0:
                largo = lps[largo - 1]
            else:
                lps[i] = 0
                i += 1

    return lps

# Función para buscar todas las ocurrencias de la subcadena en la cadena principal usando KMP
def kmp_busqueda(cadena_principal, subcadena):
    n = len(cadena_principal)
    m = len(subcadena)
    
    # Construir el array de prefijos para la subcadena
    lps = construir_array_kmp(subcadena)
    
    i = 0  # índice para la cadena principal
    j = 0  # índice para la subcadena
    ocurrencias = []

    while i < n:
        if cadena_principal[i] == subcadena[j]:
            i += 1
            j += 1
        
        if j == m:  # Se encontró una coincidencia completa
            ocurrencias.append(i - j)
            j = lps[j - 1]
        
        elif i < n and cadena_principal[i] != subcadena[j]:
            if j != 0:
                j = lps[j - 1]
            else:
                i += 1

    return ocurrencias

# Prueba del algoritmo
cadena_principal = "ababcababcabc"
subcadena = "abca"

ocurrencias = kmp_busqueda(cadena_principal, subcadena)
print(f'Ocurrencias de "{subcadena}" en "{cadena_principal}": {ocurrencias}')
