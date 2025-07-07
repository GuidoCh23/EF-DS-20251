# EXAMEN PARCIAL - DESARROLLO DE SOFTWARE
Alumno: Chipana Calderon Guido Anthony
Codigo: 20221428H

## Descripcion del Proyecto
El proyecto se basa de recibir el codigo de una aplicacion heredada de python y un nuevo microservicio desarrollador en python (new-microservice). 
Ambos componentes van a formar parte de sistema hibrido en trasicion hacia una arquitectura de microservicio.
La aplicacion Legacy (legacy-app) necesita conectarse a una base de datos PostgreSQL mientras que el nuevo microservicio se comunica con el monolito mediante una API interna.
La tarea consiste en contenerizar ambos componentes, definir una orquestacion local con Docker Compose, diseñar un despliegue robusto y seguro en Kubernetes, aplicar politicas de red y control de trafico y finalmente establecer un pipeline de CI/CD que valida, construya y depliegue todo el sistema, incluyendo estrategias avanzadas comom despliegue canarios y gestion de manifiestos declarativoss

## Arquitectura del Sistema

### Componentes
- **legacy-app**: Aplicacion Python con FastAPI
- **new-microservice**: Microservicio Python con FastAPI
- **database**: Base de datos PostgreSQL

### Arquitectura de Red
- **Docker Compose**: Red interna `internal-network` con aislamiento entre servicios
- **Kubernetes**: Servicios ClusterIP para comunicacion interna, StatefulSet para PostgreSQL

## Instrucciones de Despliegue

### Despliegue Local con Docker Compose

1. **Construir y levantar servicios:**
```bash
docker-compose up --build
```

2. **Verificar servicios:**
```bash
docker-compose ps
```

3. **Detener servicios:**
```bash
docker-compose down
```

### Despliegue en Kubernetes

1. **Aplicar manifiestos:**
```bash
kubectl apply -f kubernetes/secret.yaml
kubectl apply -f kubernetes/configmap.yaml
kubectl apply -f kubernetes/statefulset.yaml
kubectl apply -f kubernetes/deployment.yaml
```

2. **Verificar despliegue:**
```bash
kubectl get pods
kubectl get services
kubectl get pvc
```

3. **Limpiar recursos:**
```bash
kubectl delete -f kubernetes/
```

**Firma del Estudiante:**

Declaro que esta entrega fue realizada de forma individual, sin asistencia externa, sin herramientas de generacion automatica y cumpliendo con todas las reglas del examen