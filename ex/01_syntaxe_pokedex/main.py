import random

STARTER_POKEMON = [
    {"id": 1, "name": "Pikachu", "type": "electrik", "level": 12},
    {"id": 2, "name": "Carapuce", "type": "eau", "level": 9},
    {"id": 3, "name": "Bulbizarre", "type": "plante", "level": 11},
]


def display_menu():
    print("\n=== MINI POKEDEX PYTHON ===")
    print("1. Afficher le Pokedex")
    print("2. Ajouter un Pokemon")
    print("3. Chercher par type")
    print("4. Compter les Pokemon d'un niveau minimum")
    print("5. Quitter")


def read_positive_int(message):
    value = input(message).strip()

    while not value.isdigit():
        value = input("Entre un nombre entier positif: ").strip()

    return int(value)


def display_pokemon(pokemon):
    # TODO:
    # Affiche un Pokemon avec un format lisible.
    # Exemple:
    # - #1 Pikachu | type: electrik | niveau: 12
    print(f"[TODO] Pokemon a afficher: {pokemon}")


def list_pokemon(pokedex):
    # TODO:
    # Parcours la liste `pokedex` et affiche chaque Pokemon.
    print("\nPokedex actuel:")
    print("[TODO] Ajoute ici une boucle pour afficher tous les Pokemon.")


def add_pokemon(pokedex):
    print("\nAjout d'un Pokemon")
    # TODO:
    # 1. Demande le nom.
    # 2. Demande le type.
    # 3. Demande le niveau avec `read_positive_int(...)`.
    # 4. Cree un dictionnaire Pokemon.
    # 5. Ajoute-le dans `pokedex`.
    print("[TODO] Cette fonction doit ajouter un nouveau Pokemon.")


def find_by_type(pokedex, wanted_type):
    # TODO:
    # Renvoie une liste de Pokemon dont le type correspond a `wanted_type`.
    return []


def count_strong_pokemon(pokedex, minimum_level):
    # TODO:
    # Compte combien de Pokemon ont un niveau >= minimum_level.
    return 0


def random_trainer_tip():
    tips = [
        "Pense a bien nommer tes variables.",
        "En Python, l'indentation fait partie du code.",
        "Teste souvent: un petit changement, un petit test.",
        "Lis ton code a voix haute: s'il est clair, c'est bon signe.",
    ]
    # TODO:
    # Retourne un conseil aleatoire avec random.choice(...)
    return "[TODO] Ajoute un vrai conseil aleatoire."


def main():
    pokedex = [pokemon.copy() for pokemon in STARTER_POKEMON]

    while True:
        display_menu()
        choice = input("\nTon choix: ").strip()

        if choice == "1":
            list_pokemon(pokedex)
        elif choice == "2":
            add_pokemon(pokedex)
        elif choice == "3":
            wanted_type = input("Type cherche: ").strip()
            matches = find_by_type(pokedex, wanted_type)

            if matches:
                print(f"\nPokemon trouves pour le type '{wanted_type}':")
                for pokemon in matches:
                    display_pokemon(pokemon)
            else:
                print("\nAucun Pokemon pour ce type.")
        elif choice == "4":
            minimum_level = read_positive_int("Niveau minimum: ")
            total = count_strong_pokemon(pokedex, minimum_level)
            print(f"\nIl y a {total} Pokemon avec un niveau >= {minimum_level}.")
        elif choice == "5":
            print(f"\nConseil du dresseur: {random_trainer_tip()}")
            print("A bientot.")
            break
        else:
            print("Choix invalide. Essaie encore.")


if __name__ == "__main__":
    main()
