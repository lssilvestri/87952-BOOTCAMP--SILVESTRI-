class PersonaRepository:
    def __init__(self):
        self._personas = {}

    def guardar(self, persona):
        if persona.dni in self._personas:
            raise ValueError("Ya existe una persona con ese DNI")

        self._personas[persona.dni] = persona

    def buscar_por_dni(self, dni):
        return self._personas.get(dni)

    def buscar_todos(self):
        return list(self._personas.values())

    def actualizar(self, persona):
        if persona.dni not in self._personas:
            raise ValueError("La persona no existe")

        self._personas[persona.dni] = persona

    def eliminar(self, dni):
        if dni not in self._personas:
            raise ValueError("La persona no existe")

        del self._personas[dni]