class Persona:
    def __init__(self, dni: int, nombre: str):
        self._validar_dni(dni)
        self._validar_nombre(nombre)

        self.dni = dni
        self.nombre = nombre

    def _validar_dni(self, dni):
        if not isinstance(dni, int):
            raise ValueError("El DNI debe ser un número entero")

        if dni <= 0:
            raise ValueError("El DNI debe ser mayor a 0")

    def _validar_nombre(self, nombre):
        if not isinstance(nombre, str):
            raise ValueError("El nombre debe ser un texto")

        if not nombre:
            raise ValueError("El nombre no puede estar vacío")

        if len(nombre) > 30:
            raise ValueError("El nombre no puede tener más de 30 caracteres")

        if not nombre.isalpha():
            raise ValueError("El nombre solo puede contener letras")

        if nombre[0].isupper() is False:
            raise ValueError("El nombre debe comenzar con mayúscula")

        if nombre[1:] != nombre[1:].lower():
            raise ValueError(
                "Las demás letras del nombre deben estar en minúscula"
            )