# EXAMEN PARCIAL - DESARROLLO DE SOFTWARE
Alumno: Chipana Calderon Guido Anthony
Codigo: 20221428H

## Descripcion del Proyecto
El proyecto se basa de recibir el codigo de una aplicacion heredada de python y un nuevo microservicio desarrollador en python (new-microservice). 
Ambos componentes van a formar parte de sistema hibrido en trasicion hacia una arquitectura de microservicio.
La aplicacion Legacy (legacy-app) necesita conectarse a una base de datos PostgreSQL mientras que el nuevo microservicio se comunica con el monolito mediante una API interna.
La tarea consiste en contenerizar ambos componentes, definir una orquestacion local con Docker Compose, diseñar un despliegue robusto y seguro en Kubernetes, aplicar politicas de red y control de trafico y finalmente establecer un pipeline de CI/CD que valida, construya y depliegue todo el sistema, incluyendo estrategias avanzadas comom despliegue canarios y gestion de manifiestos declarativoss