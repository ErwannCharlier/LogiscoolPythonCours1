# Exercice 2 - Two Sum version simple

## But

Tu vas ecrire une fonction `two_sum(nums, target)` qui renvoie les indices de deux nombres dont la somme vaut `target`.

## Exemple

Si:

```python
nums = [2, 7, 11, 15]
target = 9
```

alors la reponse est:

```python
[0, 1]
```

car:

```python
nums[0] + nums[1] == 9
```

## Regle importante

Pour commencer, fais une solution simple avec deux boucles.

Oui, ce n'est pas la version la plus rapide.
Et c'est tres bien pour aujourd'hui.

## Fichier a completer

Travaille dans [main.py]

## Etapes conseillees

1. Parcours la liste une premiere fois avec un indice `i`.
2. A l'interieur, parcours la suite de la liste avec un indice `j`.
3. Compare `nums[i] + nums[j]` a `target`.
4. Si la somme correspond, renvoie `[i, j]`.
5. Si aucune paire ne marche, renvoie `[]`.

## Cas a tester

```python
print(two_sum([2, 7, 11, 15], 9))      # [0, 1]
print(two_sum([3, 2, 4], 6))           # [1, 2]
print(two_sum([1, 2, 3], 100))         # []
```

## Check-list de reussite

- ta fonction renvoie des indices, pas les valeurs;
- tu n'utilises pas deux fois le meme nombre;
- tu renvoies `[]` si rien ne marche.

## Bonus

Si tu termines vite, essaye une version plus maline avec un dictionnaire pour passer en une seule boucle.

## Indices progressifs

Indice 1:
Pour recuperer l'indice et la valeur, tu peux utiliser `range(len(nums))`.

Indice 2:
La deuxieme boucle peut commencer a `i + 1` pour eviter de tester deux fois la meme paire.
