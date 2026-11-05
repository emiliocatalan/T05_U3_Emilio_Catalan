# T05 | Sensibilidad a malla y condiciones de borde

Se utiliza el solver NumPy de elementos finitos 1D entregado en la actividad. El objetivo del trabajo es analizar la sensibilidad a la malla, cuantificar el error entre nodos y estudiar el efecto de modificar una condición de borde, sin reescribir el solver suministrado.

## Procedimiento realizado

1. Se revisaron los datos de `datos/barra.json`.
2. Se registró una predicción previa en `BITACORA.md`.
3. Se completaron las funciones pendientes de `src/analisis.py`:
   - `desplazamiento_referencia()`
   - `error_puntos_medios()`
4. Se ejecutaron las pruebas del solver base mediante:

```bash
python -m pytest -q
```

Resultado obtenido:

```text
2 passed
```

5. Se ejecutó el estudio completo mediante:

```bash
python src/ejecutar.py
```

6. Se analizaron las mallas de 2, 4 y 8 elementos y el caso `BC_ALTERADO`.

## Resultados principales

Para las tres mallas del problema base, el desplazamiento del extremo se mantuvo prácticamente constante:

```text
u(L) ≈ 0,300 mm
```

El error máximo en puntos medios disminuyó al refinar la malla:

```text
n = 2:  0,00625 mm
n = 4:  0,0015625 mm
n = 8:  0,000390625 mm
```

Al duplicar el número de elementos, el error disminuyó aproximadamente a la cuarta parte.

Para el problema base, la reacción izquierda fue aproximadamente:

```text
R_izq = -40000 N
```

y el balance global fue prácticamente cero.

En el caso `BC_ALTERADO` se impuso adicionalmente `u(L)=0`. Se obtuvo:

```text
u(L) = 0 mm
R_izq = -10000 N
R_der = -30000 N
balance = 0 N
```

El equilibrio continúa cumpliéndose, pero este caso representa un problema físico diferente debido al cambio en la condición de borde.

## Archivos generados

La ejecución de `src/ejecutar.py` genera:

- `salidas/resultados.csv`: resultados de las tres mallas y del caso de contorno alterado.
- `salidas/convergencia.png`: gráfico del error máximo en puntos medios frente al número de elementos.
- `salidas/versiones.txt`: registro de versiones del entorno utilizado.

## Entorno utilizado

La actividad fue ejecutada en Windows mediante Visual Studio Code.

Versiones principales utilizadas:

```text
Python 3.13.14
NumPy 2.5.4
Matplotlib 3.11.2
```

También se utilizó `pytest` para ejecutar las pruebas suministradas.

Para reproducir el análisis desde la carpeta `T05_U3`:

```bash
python -m pytest -q
python src/ejecutar.py
```

Si las dependencias no están instaladas, utilice:

```bash
python -m pip install -r requirements.txt
```

Los tests suministrados comprueban el solver base, pero no sustituyen la interpretación de los resultados ni la verificación del modelo.

## Predicción y verificación

La predicción inicial fue que al aumentar el número de elementos el error entre nodos disminuiría y que el desplazamiento del extremo cambiaría cada vez menos.

Los resultados confirmaron la disminución del error. El desplazamiento `u(L)` se mantuvo prácticamente igual para las tres mallas, mientras que el error en puntos medios disminuyó progresivamente.

También se comprobó que agregar `u(L)=0` no corresponde a un refinamiento de malla, sino a un cambio de condición de borde y, por lo tanto, a un problema diferente.

La evidencia se encuentra en:

- `BITACORA.md`
- `salidas/resultados.csv`
- `salidas/convergencia.png`

## Uso de IA

Se utilizó ChatGPT como apoyo para interpretar la consigna y el material de clases, revisar las funciones pendientes de `src/analisis.py`, orientar la ejecución del proyecto e interpretar los resultados.

Las sugerencias utilizadas fueron contrastadas con las ecuaciones, condiciones de borde y procedimientos entregados en la actividad y en los materiales de la Unidad 3.

La declaración detallada se encuentra en:

```text
USO_IA.md
```

## Informe y entrega

El informe se prepara utilizando `informe/main.tex` y debe respetar el máximo de dos páginas indicado en la consigna.

La entrega debe conservar las entradas, código, resultados CSV, figuras, registros, versiones, `README.md`, `BITACORA.md`, `USO_IA.md` y las fuentes del informe.

Antes de la entrega se debe completar `entrega.json` con la URL real del repositorio y el hash completo del commit evaluado.

No se deben incluir `.venv`, `.git`, credenciales ni archivos binarios grandes del solver.

## Preentrega

Antes de comprimir la entrega ejecutar:

```bash
python verificar_entrega.py .
```

Este comando revisa la estructura y detecta archivos faltantes, pero no reemplaza la rúbrica ni ejecuta nuevamente el análisis.

También registrar las versiones del entorno mediante:

```bash
python -m pip freeze > requirements-lock.txt
```

La carpeta `.venv` no debe incluirse en el ZIP final.