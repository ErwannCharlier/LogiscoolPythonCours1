from flask import Flask, jsonify, request

app = Flask(__name__)

pokedex = [
    {"id": 1, "name": "Pikachu", "type": "electrik", "level": 12},
    {"id": 2, "name": "Carapuce", "type": "eau", "level": 9},
    {"id": 3, "name": "Salameche", "type": "feu", "level": 10},
]


@app.get("/api/pokemon")
def get_pokemon():
    # TODO:
    # Renvoyer la liste `pokedex` en JSON.
    return jsonify([])


@app.post("/api/pokemon")
def create_pokemon():
    # TODO:
    # 1. Lire le JSON envoye.
    # 2. Recuperer `name`, `type` et `level`.
    # 3. Creer un nouveau dictionnaire Pokemon.
    # 4. L'ajouter a `pokedex`.
    # 5. Renvoyer le Pokemon cree avec le statut 201.
    return jsonify({"message": "TODO: ajoute un Pokemon ici."}), 501


@app.get("/")
def home():
    # TODO:
    # Construire une petite page HTML qui affiche le contenu du Pokedex.
    return """
    <html>
        <body>
            <h1>Mini Pokedex</h1>
            <p>TODO: affiche ici les Pokemon de la liste.</p>
        </body>
    </html>
    """


if __name__ == "__main__":
    app.run(debug=True)
