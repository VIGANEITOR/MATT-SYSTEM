# ADR-009 — Aislamiento de credenciales y permisos de ejecución

- **Estado**: Propuesto
- **Responsable**: Responsable técnico
- **Fecha límite**: Antes de R0b

## Contexto
FB-R0-006 y SC-002. Los agentes y los procesos que se ejecutan en el sandbox no deben poder leer credenciales, y toda
conexión externa debe estar limitada y registrada (Brief Maestro v1.6 §12.2; Constitución, Arts. 29 y 39).

## Opciones consideradas
1. **Proxy de salida con inyección de credenciales**: el sandbox solo puede salir por un proxy que aplica la lista permitida, registra cada conexión e inyecta la credencial del destino fuera del sandbox. *A favor:* el proceso nunca ve el secreto; un único punto de control y registro. *En contra:* hay que operar el proxy y su terminación TLS.
2. **Credenciales temporales de alcance mínimo dentro del sandbox**: *a favor*, más simple. *En contra:* el proceso puede leerlas y filtrarlas durante su vigencia, lo que contradice FB-R0-006.
3. **Espejo interno de datos sin red**: se descargan los datos permitidos a un almacén interno y el sandbox nunca sale. *A favor:* elimina la red en el cómputo. *En contra:* no sirve para servicios que se consultan en vivo.

## Recomendación
Opción 1 como mecanismo general, complementada con la opción 3 para los datasets que se reutilizan con frecuencia.
La opción 2 se descarta.

## Decisión
Pendiente.

## Consecuencias
Pendiente. Prueba de aceptación asociada: QA-PLA-10 (ningún agente ni proceso del sandbox puede leer una credencial).
