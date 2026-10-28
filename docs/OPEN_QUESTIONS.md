# Preguntas abiertas

Estas preguntas surgen de una revisión sin intervención del usuario de los documentos, reglas, comandos y directorios de estructura inicial existentes, realizada el 2026-10-28. Las opciones predeterminadas sugeridas son propuestas, no decisiones aceptadas ni comportamientos implementados. Resuelve cada pregunta pertinente antes de implementar o poner en funcionamiento el flujo afectado.

## Resultado de la revisión

La revisión siguió este orden: propósito → alcance del piloto → reglas del dominio → límites de ejecución → operación. La documentación existente establece el ciclo de Inventory Truth, la confirmación antes de modificar existencias, el registro inmutable de movimientos, el aislamiento entre organizaciones, las evidencias privadas, los módulos hexagonales, el alojamiento en Railway y Better Auth. Las cuestiones pendientes se enumeran a continuación. Esta revisión no implica nuevas aprobaciones de producto.

## Q01. Ubicaciones de inventario del piloto

Pregunta: La incorporación de una obra y el registro de movimientos utilizan ubicaciones, pero el alcance del piloto las pospone hasta el MVP comercial. ¿Qué modelo de ubicaciones se necesita?

Por qué importa: Determina cómo se agrupan los saldos iniciales, las consultas, los conteos y el alcance de la interfaz.

Opción predeterminada sugerida: Usar una única ubicación de inventario predeterminada por obra y posponer los flujos con varias ubicaciones.

## Q02. Alcance de las transferencias y los ingresos

Pregunta: ¿Las transferencias forman parte del piloto? ¿El ingreso de existencias se distingue de la gestión de recepciones de proveedores?

Por qué importa: El glosario anterior incluye las transferencias en «piloto y fases posteriores», mientras que las recepciones de proveedores y las recepciones parciales se posponen.

Opción predeterminada sugerida: Mantener el ingreso como `RECEIPT` y posponer las transferencias y los registros de entregas de proveedores.

## Q03. Autoridad de aprobación

Pregunta: ¿Quién puede aprobar el inventario inicial, las reversiones y los ajustes, y con qué umbrales?

Por qué importa: Las reglas de seguridad separan los permisos de registrar, aprobar y administrar, pero no existe una matriz de permisos.

Opción predeterminada sugerida: Exigir la aprobación explícita de un supervisor para el inventario inicial y los ajustes. Definir quién puede aprobar reversiones antes de utilizarlas. No aprobar automáticamente.

## Q04. Momento de corte del conteo y movimientos simultáneos

Pregunta: ¿Con qué momento de corte del registro de movimientos se compara un conteo? ¿Cómo se gestionan los movimientos realizados durante el conteo?

Por qué importa: Comparar cantidades de momentos distintos puede generar diferencias falsas.

Opción predeterminada sugerida: Registrar el momento de corte y la fecha y hora del conteo. Ejecutar secuencialmente la aprobación del conteo y los movimientos afectados hasta diseñar un protocolo de concurrencia.

## Q05. Tolerancia y confianza

Pregunta: ¿Qué tolerancia, antigüedad del conteo y prioridad entre transiciones definen cada estado de confianza?

Por qué importa: Las etiquetas actuales no definen una máquina de estados operativa ni cómo se mide el objetivo de precisión del 95 %.

Opción predeterminada sugerida: No tolerar provisionalmente diferencias sin explicación y mostrar la fecha y hora del último conteo. Acordar las tolerancias y la antigüedad máxima del conteo por material antes del lanzamiento.

## Q06. Existencias negativas

Pregunta: ¿Qué roles pueden permitir existencias negativas? ¿Esta posibilidad está habilitada de forma predeterminada?

Por qué importa: Las reglas del registro de movimientos las permiten con advertencia, motivo y permiso configurado, pero no establecen un comportamiento predeterminado.

Opción predeterminada sugerida: Rechazar las existencias negativas salvo que se habiliten explícitamente para un rol autorizado, con advertencia y motivo.

## Q07. Cantidades y correcciones

Pregunta: ¿Qué precisión decimal y reglas de conversión se aplican? ¿Se permiten reversiones parciales o repetidas?

Por qué importa: El redondeo y las reversiones que exceden la cantidad original pueden generar inconsistencias en los totales del registro de movimientos.

Opción predeterminada sugerida: Usar cantidades decimales exactas, conversiones revisadas a la unidad base y una única reversión completa vinculada al movimiento original hasta acordar una política de reversiones parciales.

## Q08. Ciclo de vida de la confirmación

Pregunta: ¿Cuándo vencen las propuestas? ¿Qué ocurre si las existencias o el contexto de la obra cambian antes de la confirmación?

Por qué importa: Una confirmación aislada no debe aprobar datos desactualizados ni un movimiento distinto del presentado.

Opción predeterminada sugerida: Vincular la confirmación a una propuesta identificada y a una obra. Exigir una nueva revisión tras cambios sustanciales o el vencimiento. Definir el plazo de vencimiento antes de implementar.

## Q09. Identidad telefónica y contexto de la obra

Pregunta: ¿Cómo se vinculan, revocan y autorizan los números de WhatsApp entre organizaciones?

Por qué importa: Un número de teléfono o el contexto guardado de una conversación no bastan para autorizar el acceso a una organización.

Opción predeterminada sugerida: Exigir una vinculación gestionada por un administrador, comprobar la membresía activa en cada acción y mantener visible la obra seleccionada.

## Q10. Medición del piloto

Pregunta: ¿Cómo se miden el registro de movimientos, la precisión, la retención y la continuidad de pago para entre uno y tres socios de diseño?

Por qué importa: Medir el registro en el mismo día requiere un denominador independiente. El criterio de pago de dos de tres socios no contempla grupos más pequeños.

Opción predeterminada sugerida: Acordar las definiciones antes de incorporar las obras. Contrastar los registros diarios de campo con los movimientos confirmados, explicar las diferencias por material e informar cuántos socios pagan respecto del total del grupo, sin afirmar que equivale al umbral original.

## Q11. Alcance de la exportación e importación

Pregunta: ¿El piloto requiere solo CSV o también exportación nativa a Excel?

Por qué importa: El alcance del piloto menciona CSV y Excel, mientras que `scope-gate` incluye CSV y pospone la importación desde Excel.

Opción predeterminada sugerida: Empezar con la exportación a CSV y mantener pendiente la decisión sobre la exportación a Excel. La configuración asistida no implica ofrecer una importación de autoservicio.

## Q12. Recepción persistente de eventos e idempotencia

Pregunta: ¿Qué biblioteca de colas, punto de aceptación persistente, alcance de claves, plazo de conservación y protocolo de reprocesamiento se utilizarán?

Por qué importa: Confirmar la recepción antes de guardar el evento de forma recuperable puede causar su pérdida. La caducidad de claves en Redis puede permitir escrituras duplicadas de existencias.

Opción predeterminada sugerida: Evaluar una bandeja de entrada de eventos en Postgres y restricciones transaccionales de unicidad para el inventario, junto con tareas en Redis. Confirmar la recepción solo cuando el evento sea recuperable. Verificar los contratos de firmas y eventos de Kapso durante la implementación.

## Q13. Persistencia y puesta en marcha del worker

Pregunta: ¿Qué esquema, migraciones, ruta del worker, rutas de API y comprobaciones de salud forman el primer flujo ejecutable?

Por qué importa: No existen manifiestos de paquetes ni contratos de ejecución que se puedan desplegar o probar.

Opción predeterminada sugerida: Implementar un flujo de ingreso y salida con confirmación, inyección de dependencias mediante funciones de fábrica y pruebas locales con Postgres antes de ampliar el alcance. Considerar BullMQ como candidato, no como dependencia definitiva.

## Q14. Recuperación y operación

Pregunta: ¿Quién se encarga de los incidentes? ¿Cuáles son los objetivos de punto de recuperación y tiempo de recuperación, RPO y RTO? ¿Cómo se restauran conjuntamente Postgres, R2 y las tareas en cola?

Por qué importa: La guía actual para volver a una versión anterior no es un procedimiento de recuperación probado.

Opción predeterminada sugerida: Asignar un responsable de incidentes y exigir un simulacro de restauración en el entorno de pruebas, junto con un reprocesamiento idempotente, antes de habilitar escrituras en producción. Acordar con el socio los objetivos de recuperación y la conservación de copias de seguridad.

## Q15. Evidencias y datos personales

Pregunta: ¿Qué políticas se aplican a los tipos y tamaños de archivos, la vigencia de las URL firmadas, la conservación de datos, la exportación y la eliminación?

Por qué importa: Las evidencias privadas y los mensajes originales contienen información personal y empresarial.

Opción predeterminada sugerida: Recopilar solo los datos necesarios, mantener privadas las evidencias, autorizar cada URL firmada y acordar reglas explícitas de conservación y eliminación antes de recopilar datos.

## Q16. Proveedores de mensajería y costos

Pregunta: ¿Qué eventos de Kapso, plantillas, ventanas de atención, proveedor de LLM para interpretación alternativa y límites de gasto se configurarán?

Por qué importa: Los resúmenes proactivos y la interpretación alternativa requieren contratos reales con los proveedores y un responsable del presupuesto.

Opción predeterminada sugerida: Empezar con flujos de texto deterministas y resolución manual de ambigüedades. Validar los contratos y costos vigentes de los proveedores antes de habilitar funciones proactivas o basadas en LLM.
