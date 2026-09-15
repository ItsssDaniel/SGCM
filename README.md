# SGCM - Sistema de Gestión de Consultorio Médico

Sistema web desarrollado con Django y PostgreSQL para optimizar las operaciones de un consultorio médico, facilitando la programación de citas, seguimiento de pacientes y gestión de expedientes.

## 🛠️ Tecnologías
* Backend: Python / Django
* Base de Datos: PostgreSQL
* Frontend: HTML5 / CSS3

## 🚀 Instalación y Ejecución Local
1. Clona este repositorio:
   `git clone https://github.com/ItsssDaniel/SGCM.git`
2. Activa tu entorno virtual e instala las dependencias (Django, psycopg2).
3. Crea una base de datos en PostgreSQL llamada `sgcm_gps`.
4. Aplica las migraciones para generar las tablas:
   `python manage.py migrate`
5. Levanta el servidor local:
   `python manage.py runserver`

## 🌿 Flujo de Trabajo (Ramas)
* **Prohibido** hacer commits directos a `main`.
* Toda nueva tarea debe trabajarse en una rama (ej. `feat/login`, `fix/errores-bd`).
* Se requiere un Pull Request revisado para integrar código a la rama principal.