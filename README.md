
## Objectif de la seance

A la fin des 1h30, les eleves doivent etre capables de:

- lire et ecrire un petit script Python;
- manipuler des variables, des chaines, des listes et des dictionnaires;
- utiliser des `if`, des boucles et des fonctions;
- resoudre 2 petits exercices d'algo;
- comprendre la base d'une API en Flask avec un endpoint `GET`, un endpoint `POST` et une page HTML.

## Deroule conseille

1. `0 a 15 min` - Intro Python
   Comparer rapidement Python a d'autres langages deja connus: indentation, pas de point-virgule, types simples, lecture tres directe.
2. `15 a 45 min` - Exercice 1
   Faire `ex/01_syntaxe_pokedex`.
3. `45 a 55 min` - Exercice 2
   Faire `ex/02_algo_two_sum`.
4. `55 a 65 min` - Exercice 3
   Faire `ex/03_algo_valid_palindrome`.
5. `65 a 85 min` - Exercice 4
   Faire `ex/04_flask_mini_pokedex`.
6. `85 a 90 min` - Recap
   Revenir sur ce qui change le plus entre Python et les autres langages.

## Ordre conseille

1. [ex/01_syntaxe_pokedex/README.md](/Users/erwann/development/coursPython1/ex/01_syntaxe_pokedex/README.md)
2. [ex/02_algo_two_sum/README.md](/Users/erwann/development/coursPython1/ex/02_algo_two_sum/README.md)
3. [ex/03_algo_valid_palindrome/README.md](/Users/erwann/development/coursPython1/ex/03_algo_valid_palindrome/README.md)
4. [ex/04_flask_mini_pokedex/README.md](/Users/erwann/development/coursPython1/ex/04_flask_mini_pokedex/README.md)

## Commandes utiles

Lancer un script Python:

```bash
python3 ex/01_syntaxe_pokedex/main.py
python3 ex/02_algo_two_sum/main.py
python3 ex/03_algo_valid_palindrome/main.py
```

Lancer l'exercice Flask:

```bash
python3 ex/04_flask_mini_pokedex/app.py
```

Puis ouvrir:

- `http://127.0.0.1:5000/`
- `http://127.0.0.1:5000/api/pokemon`

## Mini memo Python

### 1. Variables

```python
name = "Pikachu"
level = 12
is_legendary = False
```

### 2. Affichage

```python
print("Bonjour")
print(f"{name} est niveau {level}")
```

### 3. Conditions

```python
if level >= 10:
    print("Pokemon solide")
else:
    print("Pokemon debutant")
```

### 4. Boucles

```python
for number in [1, 2, 3]:
    print(number)

while True:
    break
```

### 5. Listes

```python
pokemon_names = ["Pikachu", "Salameche", "Carapuce"]
pokemon_names.append("Bulbizarre")
```

### 6. Dictionnaires

```python
pokemon = {
    "name": "Pikachu",
    "type": "electrik",
    "level": 12,
}

print(pokemon["name"])
```

### 7. Fonctions

```python
def present(name):
    return f"Salut {name}"
```

### 8. Imports

```python
import random

choice = random.choice(["eau", "feu", "plante"])
```
