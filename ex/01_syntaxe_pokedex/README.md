# Exercice 1 - Mini Pokedex en console

## But

Tu vas completer un petit programme Python en console qui gere un mini Pokedex.

Le programme doit pouvoir:

- afficher les Pokemon deja presents;
- ajouter un nouveau Pokemon;
- filtrer les Pokemon par type;
- compter les Pokemon avec un niveau minimum;
- afficher un petit message aleatoire quand on quitte.

## Ce que tu vas travailler

- variables et types;
- `input()` et conversion en `int`;
- `if / elif / else`;
- boucles `for` et `while`;
- listes et dictionnaires;
- fonctions;
- `import random`.

## Fichier a completer

Travaille dans [main.py]
## Mission

Le starter contient deja:

- un mini Pokedex de depart;
- un menu;
- une boucle principale;
- plusieurs fonctions avec des `TODO`.

Ton travail est de remplacer les parties inachevees.

## Etapes conseillees

1. Lance le fichier une premiere fois pour voir le menu.
2. Complete `display_pokemon(pokemon)`.
   Cette fonction doit afficher proprement un Pokemon.
3. Complete `list_pokemon(pokedex)`.
   Cette fonction doit parcourir la liste et afficher tous les Pokemon.
4. Complete `add_pokemon(pokedex)`.
   Demande a l'utilisateur un nom, un type et un niveau, puis ajoute un dictionnaire dans la liste.
5. Complete `find_by_type(pokedex, wanted_type)`.
   Cette fonction doit renvoyer une nouvelle liste avec seulement les Pokemon du bon type.
6. Complete `count_strong_pokemon(pokedex, minimum_level)`.
   Cette fonction doit compter combien de Pokemon ont un niveau superieur ou egal au minimum demande.
7. Complete `random_trainer_tip()`.
   Cette fonction doit retourner un conseil aleatoire grace a `random.choice(...)`.

## Exemple d'utilisation

```text
=== MINI POKEDEX PYTHON ===
1. Afficher le Pokedex
2. Ajouter un Pokemon
3. Chercher par type
4. Compter les Pokemon d'un niveau minimum
5. Quitter

Ton choix: 1

Pokedex actuel:
- #1 Pikachu | type: electrik | niveau: 12
- #2 Carapuce | type: eau | niveau: 9
- #3 Bulbizarre | type: plante | niveau: 11
```

## Check-list de reussite

Ton programme est bon si:

- il se lance sans erreur;
- l'option 1 affiche tous les Pokemon;
- l'option 2 ajoute un vrai Pokemon dans la liste;
- l'option 3 filtre bien par type;
- l'option 4 compte bien les Pokemon assez forts;
- l'option 5 affiche un message aleatoire avant de quitter.

## Bonus

Si tu termines vite:

- trie les Pokemon par niveau du plus fort au plus faible;
- ajoute une option pour afficher seulement le Pokemon le plus fort;
- empeche l'ajout d'un niveau negatif.

## Indices progressifs

Indice 1:
Quand tu veux parcourir tous les Pokemon, pense a `for pokemon in pokedex:`.

Indice 2:
Un Pokemon peut etre stocke comme ca:

```python
{
    "id": 4,
    "name": "Roucool",
    "type": "vol",
    "level": 7,
}
```

Indice 3:
Pour comparer des types sans etre bloque par les majuscules, pense a `.strip().lower()`.
