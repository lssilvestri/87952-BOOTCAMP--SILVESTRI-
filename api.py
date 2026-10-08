from flask import Flask, request, jsonify

from repositories.persona_repository import PersonaRepository
from services.persona_service import PersonaService


app = Flask(__name__)

repository = PersonaRepository()
service = PersonaService(repository)


@app.get("/personas")
def obtener_personas():
    personas = service.obtener_personas()

    return jsonify([
        {
            "dni": persona.dni,
            "nombre": persona.nombre
        }
        for persona in personas
    ])


@app.get("/personas/<int:dni>")
def obtener_persona(dni):
    try:
        persona = service.obtener_persona(dni)

        return jsonify({
            "dni": persona.dni,
            "nombre": persona.nombre
        })

    except ValueError as error:
        return jsonify({"error": str(error)}), 404


@app.post("/personas")
def crear_persona():
    datos = request.get_json()

    try:
        persona = service.crear_persona(
            datos["dni"],
            datos["nombre"]
        )

        return jsonify({
            "dni": persona.dni,
            "nombre": persona.nombre
        }), 201

    except (ValueError, KeyError) as error:
        return jsonify({"error": str(error)}), 400


@app.put("/persona/<int:dni>")
@app.put("/personas/<int:dni>")
def modificar_persona(dni):
    datos = request.get_json()

    try:
        persona = service.modificar_persona(
            dni,
            datos["nombre"]
        )

        return jsonify({
            "dni": persona.dni,
            "nombre": persona.nombre
        })

    except (ValueError, KeyError) as error:
        return jsonify({"error": str(error)}), 400


@app.delete("/persona/<int:dni>")
@app.delete("/personas/<int:dni>")
def eliminar_persona(dni):
    try:
        service.eliminar_persona(dni)

        return jsonify({
            "mensaje": "Persona eliminada correctamente"
        })

    except ValueError as error:
        return jsonify({"error": str(error)}), 404


if __name__ == "__main__":
    app.run(debug=True)