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
    print(
        f"- #{pokemon['id']} {pokemon['name']} | "
        f"type: {pokemon['type']} | niveau: {pokemon['level']}"
    )


def list_pokemon(pokedex):
    print("\nPokedex actuel:")

    for pokemon in pokedex:
        display_pokemon(pokemon)


def add_pokemon(pokedex):
    print("\nAjout d'un Pokemon")
    name = input("Nom: ").strip()
    pokemon_type = input("Type: ").strip().lower()
    level = read_positive_int("Niveau: ")

    new_pokemon = {
        "id": len(pokedex) + 1,
        "name": name,
        "type": pokemon_type,
        "level": level,
    }

    pokedex.append(new_pokemon)
    print(f"{name} a ete ajoute au Pokedex.")


def find_by_type(pokedex, wanted_type):
    matches = []
    normalized_type = wanted_type.strip().lower()

    for pokemon in pokedex:
        if pokemon["type"].strip().lower() == normalized_type:
            matches.append(pokemon)

    return matches


def count_strong_pokemon(pokedex, minimum_level):
    total = 0

    for pokemon in pokedex:
        if pokemon["level"] >= minimum_level:
            total += 1

    return total


def random_trainer_tip():
    tips = [
        "Pense a bien nommer tes variables.",
        "En Python, l'indentation fait partie du code.",
        "Teste souvent: un petit changement, un petit test.",
        "Lis ton code a voix haute: s'il est clair, c'est bon signe.",
    ]
    return random.choice(tips)


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
