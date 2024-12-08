# Mootiv Odoo Entities

Este proyecto representa la adaptación de las entidades de dominio del problema planteado en la plataforma **Mootiv** a **Odoo**. Mootiv es una plataforma diseñada para gestionar entrenamientos, usuarios, entrenadores y objetivos, con un enfoque modular y escalable. Este repositorio contiene la definición de los modelos de datos de Mootiv implementados en Odoo, siguiendo las mejores prácticas para su integración y uso en esta plataforma.

## Propósito del Proyecto

El propósito principal es modelar las **entidades del dominio de Mootiv** y adaptarlas al ecosistema de **Odoo**, aprovechando las capacidades de esta plataforma para manejar relaciones, vistas, y lógica de negocio. Esto incluye la implementación de:

- **Modelos de Datos:** Traducción de las entidades Java originales a modelos de Odoo.
- **Relaciones:** Mapeo de relaciones entre entidades, como `One2many`, `Many2one` y `Many2many`.
- **Vistas:** Creación de vistas `Tree`, `Form`, y otros componentes visuales para interactuar con los datos.
- **Lógica de Negocio:** Inclusión de lógica personalizada y cálculos automáticos utilizando métodos y campos computados en Odoo.

## Entidades Principales

El proyecto incluye las siguientes entidades principales adaptadas a Odoo:

- **Personas:** `Trainer`, `Student`
- **Planes y Ciclos:** `TrainingPlan`, `TrainingCycle`, `TrainingWeek`, `TrainingDay`
- **Ejercicios y Equipos:** `Exercise`, `ExerciseRoutine`, `Equipment`, `TrainingPlace`
- **Objetivos:** `Goal`, `ScheduleGoal`
- **Atributos y Estados:** Representados mediante campos de selección (`Selection`) y relaciones.
