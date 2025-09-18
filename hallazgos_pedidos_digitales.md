### **Hallazgos del Análisis Predictivo de Pedidos Digitales**

## 1. Preguntas Clave al Negocio

Antes de seguir corriendo el modelo, sentí que era crucial devolverle la pelota al negocio. Tenía que preguntar:

* ¿Por qué **realmente** queremos digitalizar a los clientes?
* ¿Es para bajar costos de operación (traducido: gastar menos en gente y procesos manuales)?
* ¿O es para mejorar la experiencia en canales digitales (porque nadie quiere una app que se sienta como Windows 95)?

Sin esas respuestas claras, sabía que corría el riesgo de perseguir fantasmas. Para mí, el *feedback loop* es lo que mantiene los proyectos vivos y enfocados. Yo me negaria  a avanzar demasido ciegas.

---

## 2. Contexto de los Datos

Aquí me topé con el clásico "faltó contexto". No sabía de dónde salían los datos, qué significaban en la operación ni qué objetivo cubrían. Tenía 8  archivos parquet, pero nadie me había contado la historia detrás. Aprendí que la **documentación** no es opcional; es la diferencia entre un análisis útil y la adivinación con Power BI. Igual se avanzo con la prueba.

---

## 3. Variables sin Documentación

Encontré varias variables que sentí que debían ser clave para cualquier negocio:

* `pais_cd`
* `region_comercial_txt`
* `tipo_cliente_cd`

Esto me llevó a preguntas que, para mí, eran de gran valor:

* ¿Las campañas de digitalización deben cambiar según el país?
* ¿Qué pasa si el problema solo está en una región específica?
* ¿Cómo sé qué tipo de cliente es prioritario si ni siquiera está definido?

Sentí que si no aclaraba esto, el modelo terminaría decidiendo por mí, y probablemente de forma incorrecta.

---

## 4. Primeros Hallazgos (EDA General)

En mi primer Análisis Exploratorio de Datos (EDA), encontré que los datos tenían poca variabilidad. Las transacciones y los canales parecían clones. Mi principal dificultad fue cómo diferenciar lo que era básicamente lo mismo.

Las variables de clientes y transacciones se veían tan uniformes que parecía que alguien las había planchado. No pude encontrar diferencias claras entre las transacciones digitales, las del vendedor o las telefónicas. Me di cuenta de que no era tan fácil como creía. La única luz al final del túnel fue la variable **`pedidos_por_cliente`** (la cual calculé), que mostró algo más de dispersión.

Sentí que si todo se veía igual, el modelo no serviría de nada. Tenía que pensar en *features* más creativos o cruzar fuentes adicionales para encontrar lo que realmente separa a un cliente digital de uno que no. Como no era posible en ese momento, tomé medidas drásticas.

📊  **Pedidos promedio por canales**
![Imagen](images/pedidos_prom_cliente_canales.png)
---

## 5. Hipótesis de Negocio y Segmentación

Dada mi frustración por no encontrar nada para segmentar o diferenciar los datos, decidí partir de una hipótesis de negocio (que podía validar rápidamente, pero era lo que me decía la intuición):

> **Es más importante analizar a los clientes que tienen menos de 60 días desde su última transacción, pues representan un mayor valor potencial para el negocio.**

Para validar esta hipótesis y enfocar mi análisis, hice lo siguiente:

* **Excluí** a los clientes **no digitales** (aquellos que nunca usaron el canal digital) y a los **solo digitales** (los que ya estaban completamente convertidos). Me pareció que los no digitales son más difíciles de digitalizar y los digitales no eran mi objetivo.
* **Me enfoqué** únicamente en clientes **multicanal** para ser más asertivo en el análisis de la elección de canal.

Con esta base, realicé un nuevo **EDA segmentado**.

📊 **Distribuccion por pido de cliente**

![Imagen](images/pie_trans_canales.png)

---

## 6. Segundo Hallazgo (EDA Segmentado)

Mi segundo análisis exploratorio, enfocado en el segmento multicanal, mostró mayor variación en variables clave, lo que me indicó que eran buenos predictores para diferenciar el comportamiento.

* `facturacion_promedio`
* `madurez_digital_cd`

Estas variables me ofrecieron un mejor potencial para diferenciar a los clientes y predecir su comportamiento. Sentí que irrumpí en los datos y, al mismo tiempo, les di una hipótesis y un norte más claro: predecir a los clientes recientes en sus transacciones que usan canales tanto digitales como no digitales.



---

### **7. Ingeniería de Datos: Enfoque y Metodología**

Para el desarrollo del modelo, prioricé las columnas de datos que identifiqué como relevantes durante el **EDA segmentado**. Con el objetivo de generar una variable objetivo para la predicción, construí el *target* del modelo a partir del comportamiento de la última transacción del cliente.

Definí el *target* de forma binaria: la última transacción digital la etiqueté como "cliente digital" y la última no digital como "cliente no digital". Utilicé esta variable para entrenar el modelo en la **predicción de la próxima transacción**. Mi enfoque se centró en la creación de una variable clara para la modelación, a partir de una simplificación del comportamiento histórico del cliente.

---

## **8. Modelado y Experimentación**

Para la fase de modelado, implementé un **proceso de experimentación exhaustivo**. A falta de herramientas de MLOps como MLflow, opté por crear una **grilla de 90 modelos** usando la librería `scikit-learn`. Este enfoque de validación masiva me permitió evaluar una amplia gama de algoritmos y configuraciones de hiperparámetros.

Mi objetivo era **identificar el modelo con el mejor rendimiento**. El mejor modelo que encontré tiene un **AUC de 0.74**, un resultado prometedor para un primer intento. Este rendimiento sugiere que el enfoque de segmentación y la ingeniería de características fueron efectivos.

---

## **9. Despliegue del Modelo y *Endpoint***

Para demostrar la viabilidad de la solución, desarrollé una API sencilla con Flask y la configuré como un *endpoint* para exponer el modelo. Este **prototipo de despliegue** permite probar las predicciones del mejor modelo en un entorno controlado, validando su funcionalidad y preparándolo para una posible integración futura.

---

## **10. Áreas de Oportunidad y Futuras Mejoras**

Identifiqué varias áreas clave para mejorar el modelo y el análisis:

* **Revisión del aporte de las variables**: Es crucial profundizar en la importancia de las variables (*feature importance*) para entender cómo contribuyen a las predicciones del modelo.
* **Exploración de la regresión**: En lugar de una clasificación binaria, se podría predecir el **nivel de digitalización del cliente** como un valor numérico (por ejemplo, el porcentaje de transacciones digitales). Esto ofrecería una visión más matizada del comportamiento del cliente.
* **Búsqueda de más datos**: Para explicar mejor el fenómeno, es fundamental buscar **variables adicionales** que no estaban disponibles en el conjunto de datos inicial. Esto podría incluir datos transaccionales más detallados, información demográfica o interacciones con campañas de marketing.

---

## **11. Conclusiones**

Mis hallazgos y el análisis del proyecto me llevaron a las siguientes conclusiones:

1.  **Contexto y conocimiento del negocio**: El éxito de cualquier proyecto de *machine learning* depende en gran medida de un profundo entendimiento del negocio y de los datos. Esta es un área clave para mejorar.
2.  **La importancia de la variabilidad**: La falta de variabilidad en los datos iniciales entre canales fue un gran desafío. El enfoque de segmentación fue crucial para superar esta limitación. Lo ideal seria tener mas datos que muestren difernecais susatnciales enter los clientes.
3.  **Mejora de los modelos predictivos**: Los modelos se pueden mejorar significativamente con un enfoque más riguroso en la segmentación (apoyo de negocio) y la ingeniería de características.
4.  **Rendimiento del modelo**: El modelo desarrollado tiene un rendimiento inicial sólido con un **AUC de 0.74**, lo que lo convierte en una base prometedora para futuras iteraciones.
5.  **Revisión del objetivo**: Si el objetivo de negocio cambia (por ejemplo, si se busca predecir qué cliente está más cerca de ser digital), el modelo y su variable objetivo deben ajustarse para reflejar esta nueva meta.
