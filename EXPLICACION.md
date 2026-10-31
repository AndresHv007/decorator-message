# Patrón Decorator

- **Component:** `Message` define el contrato estable `render()`.
- **Concrete Component:** `PlainMessage` devuelve el texto original y se conserva sin cambios.
- **Decorator base:** `MessageDecorator` hereda de `Message`, contiene otro `Message` y delega en su método `render()`.
- **Concrete Decorators:** `UrgentDecorator` agrega `[URGENT]` y `TimestampDecorator` agrega una fecha y hora.

Como los decoradores también son un `Message`, pueden envolver tanto un mensaje simple como otro decorador.

## Ejemplo de ambos decoradores apilados

```python
from datetime import datetime

from messages.plain_message import PlainMessage
from messages.timestamp_decorator import TimestampDecorator
from messages.urgent_decorator import UrgentDecorator

message = UrgentDecorator(
    TimestampDecorator(
        PlainMessage("Deploy complete"),
        datetime(2026, 10, 30, 12, 0, 0),
    )
)

print(message.render())
# [URGENT] [2026-10-30 12:00:00] Deploy complete
```

La fecha se recibe en el constructor, en lugar de consultar el reloj dentro de `render()`. Así, el resultado es determinista y las pruebas son estables.

## ¿Importa el orden?

Sí. Ambos decoradores agregan un prefijo, por lo que el decorador exterior coloca su prefijo primero:

- `UrgentDecorator(TimestampDecorator(message, timestamp))`: `[URGENT] [2026-10-30 12:00:00] Deploy complete`.
- `TimestampDecorator(UrgentDecorator(message), timestamp)`: `[2026-10-30 12:00:00] [URGENT] Deploy complete`.

En ambos casos se conserva la misma información, pero cambia el orden del texto mostrado.

## Costo de complejidad

La cadena introduce más objetos y llamadas intermedias. Para depurar el resultado hay que seguir los decoradores y revisar el orden en que se envolvieron.

## Prueba enfocada

`test_decorators_stack_and_order_changes_prefixes` verifica las dos formas de apilar los decoradores con una fecha fija y comprueba que el mensaje original conserva su texto.

Desde la carpeta del proyecto:

```bash
python -m pip install -r requirements.txt
python -m pytest -q
```
