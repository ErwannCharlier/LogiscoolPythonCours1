# Exercice 3 - Valid Palindrome

## But

Tu vas ecrire une fonction `is_palindrome(text)` qui renvoie `True` si un texte se lit de la meme facon dans les deux sens.

Dans cet exercice, on ignore:

- les majuscules et minuscules;
- les espaces;
- la ponctuation.

## Exemple

```python
"Kayak" -> True
"Engage le jeu que je le gagne" -> True
"Python" -> False
```

## Fichier a completer

Travaille dans [main.py]
## Idee conseillee

1. Cree une nouvelle chaine vide.
2. Parcours le texte caractere par caractere.
3. Garde seulement les caracteres alphanumeriques.
4. Passe-les en minuscules.
5. Compare la chaine nettoyee avec son inverse.

## Cas a tester

```python
print(is_palindrome("Kayak"))                           # True
print(is_palindrome("Engage le jeu que je le gagne"))  # True
print(is_palindrome("Esope reste ici et se repose"))   # True
print(is_palindrome("Python"))                         # False
```

## Check-list de reussite

- `Kayak` donne `True`;
- une phrase avec des espaces peut donner `True`;
- la ponctuation ne casse pas le resultat;
- `Python` donne `False`.

## Bonus

Si tu termines vite, essaye une version sans construire une nouvelle chaine complete, en utilisant deux pointeurs.

## Indices progressifs

Indice 1:
`character.isalnum()` permet de savoir si un caractere est une lettre ou un chiffre.

Indice 2:
`text[::-1]` permet de renverser une chaine.
