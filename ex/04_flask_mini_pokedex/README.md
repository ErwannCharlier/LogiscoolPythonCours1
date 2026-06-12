# Exercice 4 - Mini API Flask Pokedex

## But

Tu vas construire une mini API avec Flask.

L'application doit proposer:

- `GET /api/pokemon` pour lire la liste des Pokemon;
- `POST /api/pokemon` pour ajouter un Pokemon;
- `GET /` pour afficher une page HTML simple.

## Ce que tu vas apprendre

- ce qu'est une route;
- comment renvoyer du JSON;
- comment lire des donnees envoyees par le client;
- comment renvoyer une petite page HTML;
- comment garder des donnees en memoire dans une liste Python.

## Fichier a completer

Travaille dans [app.py]

## Comment lancer l'application

Si Flask est deja installe:

```bash
python3 ex/04_flask_mini_pokedex/app.py
```

Ensuite ouvre:

- `http://127.0.0.1:5000/`
- `http://127.0.0.1:5000/api/pokemon`

## Mission

Le starter contient deja:

- l'import Flask;
- l'application `app`;
- une liste `pokedex`;
- les 3 routes principales.

Tu dois completer le comportement de ces routes.

## Etapes conseillees

1. Complete `GET /api/pokemon`.
   Cette route doit renvoyer la liste `pokedex` en JSON.
2. Complete `POST /api/pokemon`.
   Cette route doit lire un JSON avec `name`, `type` et `level`, creer un nouveau Pokemon, l'ajouter a la liste, puis renvoyer l'objet cree avec le statut `201`.
3. Complete `GET /`.
   Cette route doit renvoyer une page HTML simple qui affiche le contenu du Pokedex.

## Exemple de test pour POST

```bash
curl -X POST http://127.0.0.1:5000/api/pokemon \
  -H "Content-Type: application/json" \
  -d '{"name":"Evoli","type":"normal","level":8}'
```

## Check-list de reussite

- `GET /api/pokemon` renvoie une liste JSON;
- `POST /api/pokemon` ajoute bien un Pokemon;
- `POST /api/pokemon` renvoie le statut `201`;
- `GET /` affiche une vraie page HTML lisible.

## Bonus

Si tu termines vite:

- ajoute un filtre optionnel `GET /api/pokemon?type=eau`;
- affiche le nombre total de Pokemon sur la page HTML.

## Indices progressifs

Indice 1:
Pour renvoyer du JSON avec Flask, utilise `jsonify(...)`.

Indice 2:
Pour lire les donnees envoyees par le client, utilise `request.get_json(...)`.

Indice 3:
Tu peux construire une page HTML avec une simple chaine de caracteres multi-lignes.
