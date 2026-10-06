# CRUD de Personas

API REST desarrollada con Python y Flask para administrar personas.

## Estructura del proyecto

El proyecto utiliza una arquitectura dividida en capas:

```text
persona_crud/
│
├── models/
│   └── persona.py
│
├── repositories/
│   └── persona_repository.py
│
├── services/
│   └── persona_service.py
│
├── api.py
└── README.md


## Diagrama de clases

```mermaid
classDiagram

class Persona {
    -dni: int
    -nombre: str
    +Persona(dni: int, nombre: str)
    +validar_dni()
    +validar_nombre()
}

class PersonaRepository {
    -personas: dict
    +guardar(persona)
    +buscar_por_dni(dni)
    +buscar_todos()
    +actualizar(persona)
    +eliminar(dni)
}

class PersonaService {
    -repository: PersonaRepository
    +crear_persona(dni, nombre)
    +obtener_personas()
    +obtener_persona(dni)
    +modificar_persona(dni, nombre)
    +eliminar_persona(dni)
}

class API {
    +GET /personas
    +GET /personas/dni
    +POST /personas
    +PUT /personas/dni
    +DELETE /personas/dni
}

API --> PersonaService
PersonaService --> PersonaRepository
PersonaService --> Persona
PersonaRepository --> Persona
