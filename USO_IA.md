# Declaración de uso de IA

**Herramienta:** ChatGPT (OpenAI)  
**Fecha:** 05-11-2026

## Uso realizado

Se utilizó ChatGPT como apoyo durante el desarrollo del Test 1 de la Unidad 3, principalmente para:

- interpretar la consigna, la rúbrica y el material de clases;
- revisar la implementación de la función de referencia analítica;
- apoyar la implementación del cálculo del error en los puntos medios de cada elemento;
- orientar la ejecución de las pruebas y del script principal en VS Code;
- interpretar los resultados obtenidos para las mallas de 2, 4 y 8 elementos y el caso con condición de borde alterada.

## Contenido incorporado

Se incorporaron sugerencias relacionadas con las funciones `desplazamiento_referencia()` y `error_puntos_medios()` del archivo `src/analisis.py`.

La expresión utilizada para la referencia analítica se obtuvo a partir de la ecuación y las condiciones de borde entregadas en la actividad. Para el error en puntos medios se utilizó la interpolación lineal entre nodos y el error absoluto indicado en el material de clases.

## Comprobación independiente

Las sugerencias incorporadas se verificaron mediante:

- ejecución de `python -m pytest -q`, obteniendo 2 pruebas aprobadas;
- ejecución de `python src/ejecutar.py` sin errores;
- revisión de `salidas/resultados.csv`;
- comprobación del equilibrio de fuerzas;
- comparación de la tendencia del error con el material de clases, observándose que al duplicar el número de elementos el error disminuye aproximadamente a la cuarta parte;
- revisión del gráfico `salidas/convergencia.png`.

## Decisión

Se decidió utilizar únicamente las sugerencias que eran coherentes con las fórmulas, condiciones de borde y procedimientos incluidos en la consigna y en el material de la Unidad 3. No se incorporaron fórmulas externas al contenido entregado por el curso.

No se incluyeron datos personales, credenciales ni información sensible en las consultas realizadas.