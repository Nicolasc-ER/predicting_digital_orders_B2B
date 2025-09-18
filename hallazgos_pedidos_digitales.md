# Hallazgos del Análisis Predictivo de Pedidos Digitales  

## 1. Preguntas Claves al Negocio  
Antes de seguir corriendo con el modelo, toca devolver la pelota al negocio:  

- ¿Realmente *por qué* queremos digitalizar a los clientes?  
- ¿Es por bajar costos de operación? (traducción: gastar menos en gente y procesos manuales).  
- ¿O es por mejorar la experiencia en canales digitales? (porque nadie quiere que la app se sienta como Windows 95).  

Sin esas respuestas claras, podemos terminar persiguiendo fantasmas.  
Feedback friendly: acordémonos que el *feedback loop* es lo que mantiene los proyectos respirando y enfocados. Nada de avanzar a ciegas. 🙃  

---

## 2. Contexto de los Datos  
Aquí viene el clásico: *“faltó contexto”*.  
No sabemos bien de dónde salen los datos, qué significan en la operación, ni qué objetivo cubren. O sea, tenemos el Excel bonito pero nadie nos contó la historia detrás.  
Feedback: documentar más no es opcional, es la diferencia entre análisis útil y adivinación con Power BI.  

---

## 3. Variables sin Documentación  
Encontramos varias variables que se sienten como jeroglíficos egipcios:  

- `pais_cd`  
- `region_comercial_txt`  
- `tipo_cliente_cd`  

Y surgen las preguntas incómodas:  
- ¿Las campañas de digitalización deben cambiar según país?  
- ¿Qué pasa si el problema es solo en una región específica?  
- ¿Cómo sabemos qué tipo de cliente es prioridad si ni siquiera está definido?  

Feedback: si no aclaramos esto, el modelo terminará decidiendo por nosotros .. jumm  y probablemente mal hay. 

---

## 4. Primeros Hallazgos (EDA General)  

En el primer análisis exploratorio (a.k.a. EDA, para sonar más pro) nos dimos cuenta de lo siguiente:  

- No hay mucha variabilidad en los datos. O sea, las transacciones digitales y los canales parecen clones. Aquí apareció la primera dificultad: ¿cómo diferenciar lo que básicamente es lo mismo?  
- Las variables de clientes y transacciones se ven tan uniformes que parece que alguien pasó la plancha encima. No encontre diferencias claras entre transacciones digitales, vendedor o teléfono. Spoiler: no es tan fácil como pensábamos.  
- La única luz al final del túnel fue la variable **`pedidos_por_cliente`** (que, por cierto, se calculo ). Esa sí mostró un poco más de dispersión, algo así como “por fin alguien decidió ser diferente”.   

Feedback: si todo se ve igual, el modelo se va a aburrir. Hay que pensar en variables nuevas, features más creativos o cruzar fuentes adicionales para encontrar lo que realmente separa a un cliente digital de uno que no.  Por ahora se tomaron medidas drasticas.

📊 **[INSERTAR GRÁFICA: Distribución de la variable pedidos_por_cliente]**

---

## 5. Hipótesis de Negocio y Segmentación
Dada la frustacion de no ver nada para segmentar o diferneciar los datos que sirvan de base para un modelo predictivo se decidio  partir de la una hipótesis  negocio. :

> Es más importante analizar a los clientes que tienen menos de 60 días desde su última transacción, pues representan un mayor valor potencial para el negocio.

Para validar esta hipótesis y enfocar el análisis, se tomaron las siguientes acciones:

- Se excluyeron clientes **no digitales** (aquellos que nunca usaron el canal digital) y los **solo digitales** (aquellos que ya están completamente convertidos).  
- Se trabajó únicamente con clientes **multicanal** para ser más asertivos en el análisis del comportamiento de elección de canal.  

Con esta base se realizó un nuevo **EDA segmentado**.

📊 **[INSERTAR GRÁFICA: Proporción de Clientes por Segmento de Canal (Multicanal vs. Solo Digital vs. Solo No Digital)]**

---

## 6. Segundo Hallazgo (EDA Segmentado)
El segundo análisis exploratorio, enfocado en el segmento multicanal, mostró mayor variación en variables clave, indicando que son buenos predictores para diferenciar el comportamiento de compra. Las variables con mayor potencial de segmentación fueron:

- `facturacion_promedio`  
- `promedio_cajas_fisicas`  
- `madurez_digital_cd`  

Estas variables ofrecen un mejor potencial para diferenciar a los clientes y predecir su comportamiento, parece que inrumpimos en loos datos y al mismo timepo le dimos una hipotesis y un norte mas claro. predecir los clientes recientes en trasaccion y que usan canles digitales y no digitales..

📊 **[INSERTAR GRÁFICA: Comparativa de facturacion_promedio por Canal (Segmento Multicanal)]**  
📊 **[INSERTAR GRÁFICA: Comparativa de promedio_cajas_fisicas por Canal (Segmento Multicanal)]**  
📊 **[INSERTAR GRÁFICA: Distribución de madurez_digital_cd por Canal (Segmento Multicanal)]**