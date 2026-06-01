# =====================================================================
# INFORME DE INVESTIGACIÓN E IMPLEMENTACIÓN DE INTELIGENCIA ARTIFICIAL
# Materia: Nuevas Tecnologías
# Estudiante: Amanqui Curi Lanchimba Fernandez
# =====================================================================

# 1. CONFIGURACIÓN DE DATOS HISTÓRICOS (Conocimiento de la IA)
# Datos reales tomados del control del mes pasado
past_clients = 100.0
past_sales = 200.0

# 2. FASE DE APRENDIZAJE (Cálculo de la pendiente de la línea recta)
# Determinamos el valor promedio de ingresos que representa cada cliente
sales_factor_per_client = past_sales / past_clients

print(" SISTEMA DE IA: REGRESION LINEAL INTERACTIVA")
print("Entrenando el modelo predictivo con datos historicos...")
print(f"Datos de control: ${past_sales} recaudados con {past_clients} clientes.")
print(f"Analisis completado. Cada cliente aporta un promedio de: ${sales_factor_per_client}\n")

# 3. ENTRADA DE DATOS INTERACTIVA (Interacción directa con el usuario)
try:
    new_clients = float(input("Ingrese la cantidad de clientes estimados para el día de hoy: "))
    
    # 4. TRATAMIENTO PREDICTIVO (Aplicación del modelo matemático)
    predicted_sales = new_clients * sales_factor_per_client
    
    # 5. DESPLIEGUE DE RESULTADOS FINALES
    print("\n--------------------------------------------------")
    print("                RESULTADO DE LA IA                ")
    print("--------------------------------------------------")
    print(f"Para un flujo proyectado de {new_clients} clientes nuevos,")
    print(f"el algoritmo estima una recaudacion economica de: ${predicted_sales:.2f}")
    print("--------------------------------------------------")

except ValueError:
    print("\nError: Por favor, ingrese un número válido para la cantidad de clientes.")