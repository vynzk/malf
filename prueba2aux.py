def interprete_codigo(codigo):
    lineas = codigo.split('\n')  # Dividir el código en líneas
    variables = {}  # Diccionario para almacenar las variables
    iterador_lineas = iter(lineas)
    flag = True

    for linea in lineas:
        if flag:
            #print(linea)
            if linea.startswith("read"):
                # Manejar la lectura de entrada
                _, variable = linea.split("$")
                #quitar punto y coma de la variable
                valor = int(input(f"Ingrese el valor de {variable}: "))
                variables[variable] = valor


            elif linea.startswith("if"):
                # Manejar la declaración if
                _, condicion = linea.split("(")
                condicion, _ = condicion.split(") then")
                aux = condicion.split()
                variable2 = aux[0]
                comparador = aux[1]
                valor = aux[2][:-1]

                print(variables[variable])
                if comparador == "<" and variables[variable] < int(valor):
                    continue  # Continuar con la siguiente línea si la condición es verdadera
                elif comparador == ">=" and variables[variable] >= int(valor):
                    continue  # Continuar con la siguiente línea si la condición es verdadera
                else:
                    # Saltar el bloque else y continuar con la siguiente línea
                    while not linea.startswith("else") or linea.startswith("endif"):
                        linea = next(iterador_lineas)

            elif linea.startswith("else"):
                flag = False
                print("hola soy un else")
                continue
                # Manejar la declaración else
                #while not linea.startswith("endif"):
                #    linea = next(iterador_lineas)
                #    print("hola cambie linea: ",linea)

            elif linea.startswith("endif"):
                # Manejar la declaración endif
                continue
            
            elif linea.startswith("write"):
                #print("hola soy un write")
                # Manejar la impresión de salida
                _, variable2 = linea.split("")
                print(variable2)
                #print(variables[variable])

            elif linea.startswith("while"):
                # Manejar la declaración while
                _, condicion = linea.split("(")
                condicion, _ = condicion.split(") do")

                variable, comparador, valor = condicion.split()
                while variables[variable] <= int(valor):
                    # Procesar las líneas dentro del bucle while
                    for linea_bucle in lineas:
                        if linea_bucle.startswith("wend"):
                            break
                        else:
                            interprete_codigo(linea_bucle)

            elif linea.startswith("wend"):
                # Fin del bucle while, volver al inicio del bucle
                continue

            else:
                # Manejar asignaciones
                variable = linea.split()
                valor = linea.split()
                operacion = linea.split()
                if operacion == "=":
                    variables[variable] = int(valor)
                elif operacion == "+=":
                    variables[variable] += int(valor)
        elif linea.startswith("endif"):
            flag = True
        
about:blank#blocked

# Código de ejemplo
codigo = """
read $n;
if ($n < 2) then
    write $n;
else
    $fib1 = 1;
    $fib2 = 0;
    $i = 2;
    while ($i <= $n) do
        $act = $fib1 + $fib2;
        $fib2 = $fib1;
        $fib1 = $act;
        $i = $i + 1;
    wend;
write $act;
endif;
"""

interprete_codigo(codigo)
