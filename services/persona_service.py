from models.persona import Persona


class PersonaService:
    def __init__(self, repository):
        self.repository = repository

    def crear_persona(self, dni, nombre):
        persona = Persona(dni, nombre)

        if self.repository.buscar_por_dni(dni) is not None:
            raise ValueError("Ya existe una persona con ese DNI")

        self.repository.guardar(persona)

        return persona

    def obtener_personas(self):
        return self.repository.buscar_todos()

    def obtener_persona(self, dni):
        persona = self.repository.buscar_por_dni(dni)

        if persona is None:
            raise ValueError("La persona no existe")

        return persona

    def modificar_persona(self, dni, nombre):
        persona = self.repository.buscar_por_dni(dni)

        if persona is None:
            raise ValueError("La persona no existe")

        # El DNI no se modifica.
        nueva_persona = Persona(dni, nombre)

        self.repository.actualizar(nueva_persona)

        return nueva_persona

    def eliminar_persona(self, dni):
        persona = self.repository.buscar_por_dni(dni)

        if persona is None:
            raise ValueError("La persona no existe")

        self.repository.eliminar(dni)