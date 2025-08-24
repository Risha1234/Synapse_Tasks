import itertools

Pokedex = {
    "Pikachu": ("Electric",),
    "Charizard": ("Fire", "Flying"),
    "Lapras": ("Water", "Ice"),
    "Machamp": ("Fighting",),
    "Mewtwo": ("Psychic", "Fighting"),
    "Hoopa": ("Psychic", "Ghost", "Dark"),
    "Lugia": ("Psychic", "Flying", "Water"),
    "Squirtle": ("Water",),
    "Gengar": ("Ghost", "Poison"),
    "Onix": ("Rock", "Ground")
}

k = int(input("Enter the value for k: "))

names = list(Pokedex.keys())
teams = list(itertools.combinations(names, k))

all_features = []
for team in teams:
    features = set()
    for pokemon in team:
        features.update(Pokedex[pokemon])
    all_features.append((team, features))

#finding max number of features
max_features = max(len(features) for team, features in all_features)

#collecting all best teams
best_teams = [(team, features) for team, features in all_features if len(features) == max_features]

print(f"Teams with max features ({max_features}):\n")
for team, features in best_teams:
    print("Team:", team)
    print("Features:", features)
    print()
