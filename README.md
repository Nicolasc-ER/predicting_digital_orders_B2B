# Predicción de Pedidos Digitales en B2B

Este proyecto tiene como objetivo analizar los datos transaccionales de clientes para construir un modelo de *Machine Learning* que prediga la probabilidad de que el próximo pedido de un cliente sea a través del canal digital.  
La meta es identificar a los clientes con mayor potencial de adopción digital para enfocar los esfuerzos comerciales y de comunicación.

---

## 📂 Estructura del Repositorio

El proyecto está organizado en las siguientes carpetas, siguiendo un flujo de trabajo de **MLOps**:

- **`/EDA`** → Notebooks de análisis exploratorio de datos (general y segmentado).  
- **`/data_engineering`** → Script de limpieza, transformación y generación de *features* para el dataset de modelado.  
- **`/training`** → Notebook final de entrenamiento, optimización de hiperparámetros y registro de modelos.

---

## 🔄 Metodología y Flujo de Trabajo

El desarrollo del proyecto siguió una estrategia incremental en **cuatro fases principales**:

### 1. Análisis Exploratorio de Datos (EDA)
- **Análisis Descriptivo**: métricas generales de clientes y transacciones.  
- **Segmentación Inicial**: clientes clasificados en *Solo Digital*, *Solo No Digital* y *Multicanal*.  
- **Perfilado de Canales**: comparación de facturación y complejidad entre canales.  

### 2. EDA Segmentado y Profundo
- **Análisis RFM**: identificación de clientes de alto valor.  
- **Clientes para Convertir**: segmento clave de clientes activos cuya última transacción no fue digital.  
- **Análisis Comparativo**: características de transacciones en segmentos específicos.  

### 3. Ingeniería de Datos
- **Universo de Modelado**: clientes multicanal (quienes eligen entre canales).  
- **Creación de Features**: métricas RFM, estadísticas históricas de uso de canal y atributos del cliente.  
- **Variable Objetivo**: `target_prox_trx_digital` (binaria: 1 = digital, 0 = no digital).  
- **Exportación y Versionado**: datasets de *training* y *validation* registrados en el catálogo de Databricks.  

### 4. Modelado y Optimización
- **Framework**: `pandas` y `scikit-learn`.  
- **Preprocesamiento**: `Pipeline` con `ColumnTransformer` (escalado + one-hot encoding).  
- **Búsqueda de Hiperparámetros**: `GridSearchCV` sobre Random Forest y Gradient Boosting (50+ combinaciones).  
- **Seguimiento con MLflow**: registro automático de parámetros, métricas (AUC, Accuracy) y modelos.  

---

## ▶️ Cómo Ejecutar el Proyecto

1. Asegúrate de que los datos iniciales estén en la tabla:  
   ```
   data.client_transaction_orders
   ```
2. Ejecuta el notebook en **`/data_engineering`** para generar los datasets:  
   - `workspace.data.pedidos_distribucion_target_training_set`  
   - `workspace.data.pedidos_distribucion_target_validation_set`  

3. Ejecuta el notebook en **`/training`** para correr la búsqueda de hiperparámetros.  
4. Visualiza los resultados en **MLflow → Experiments**.  

---

## 📜 Licencia

Este proyecto está bajo la **Licencia MIT**.  

