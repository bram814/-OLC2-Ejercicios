# OLC2A_Display

# Entrega
Deben entregar para que quede constancia que hicieron la evaluación, la entrega será que realicen un pull request a este repositorio.

## Evaluación 15/09/2021

- Validar que el break y continue no puede aparecer afuera de un ciclo
- Validar que el break sea obligatorio en el loop

### Propuesta while

````
Linicio:
  <cod 3d cond>
cond.EV:
  <cod 3d sentencias>
goto Linicio
cond.EF:
Lsalida:
````

````
break -> goto EF o goto Lsalida
continue -> goto Linicio
````

### Propuesta Loop

#### Loop

````
Linicio:
  <cod 3d sentencias>
goto Linicio
Lsalida:
````

````
break -> goto Lsalida
continue -> goto Linicio
````
