from flask import Flask, jsonify, request

app = Flask(__name__)

pokedex = [
    {"id": 1, "name": "Pikachu", "type": "electrik", "level": 12},
    {"id": 2, "name": "Carapuce", "type": "eau", "level": 9},
    {"id": 3, "name": "Salameche", "type": "feu", "level": 10},
]


def normalize_level(raw_level):
    if isinstance(raw_level, int):
        return raw_level

    if isinstance(raw_level, str) and raw_level.isdigit():
        return int(raw_level)

    return None


@app.get("/api/pokemon")
def get_pokemon():
    return jsonify(pokedex)


@app.post("/api/pokemon")
def create_pokemon():
    data = request.get_json(silent=True) or {}

    name = str(data.get("name", "")).strip()
    pokemon_type = str(data.get("type", "")).strip().lower()
    level = normalize_level(data.get("level"))

    if not name or not pokemon_type or level is None:
        return jsonify(
            {
                "error": "Le JSON doit contenir name, type et level.",
            }
        ), 400

    new_pokemon = {
        "id": len(pokedex) + 1,
        "name": name,
        "type": pokemon_type,
        "level": level,
    }

    pokedex.append(new_pokemon)
    return jsonify(new_pokemon), 201


@app.get("/")
def home():
    html_items = ""

    for pokemon in pokedex:
        html_items += (
            "<li>"
            f"#{pokemon['id']} - {pokemon['name']} "
            f"({pokemon['type']}, niveau {pokemon['level']})"
            "</li>"
        )

    return f"""
    <html>
        <head>
            <title>Mini Pokedex Flask</title>
        </head>
        <body style="font-family: sans-serif; max-width: 700px; margin: 40px auto;">
            <h1>Mini Pokedex Flask</h1>
            <p>Cette page HTML est servie par Flask.</p>
            <p>Tu peux aussi consulter l'API JSON sur <code>/api/pokemon</code>.</p>
            <ul>{html_items}</ul>
        </body>
    </html>
    """


if __name__ == "__main__":
    app.run(debug=True)
