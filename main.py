import csv

# Garchomp
# Salamence
# Mega Charizard Y
# Mega Charizard X
# Dragonite
# Mega Rayquaza
# Mega Mewtwo X
# Mega Mewtwo Y

team1 = []
team2 = []

def baseSetup():
    global team1, team2
    found = 0
    while True:
        pokemon = input(f"Please enter the name of a Pokemon {len(team1)}/8: ")

        with open('cleanPokemon.csv', 'r') as file:
            reader = csv.reader(file)
            for i in reader:
                if i[1].lower() == pokemon.lower():
                    found += 1
                    team1.append(i)
                    break
            if found == 0:
                print("Pokemon not found!")
            found = 0
            if len(team1) == 8:
                break
    
    print("Now player 2 picks their team!")
    while True:
        pokemon = input("Please enter the number of a Pokemon: ")

        with open('cleanPokemon.csv', 'r') as file:
            reader = csv.reader(file)
            for i in reader:
                if i[1].lower() == pokemon.lower():
                    team2.append(i)
                    break
        if len(team2) == 8:
            break
    print("Player 1 vs Player 2 BEGINS NOW!")
    print("Player 1 is sporting a rather interesting team: ")
    for i in team1:
        print(i[1])
    print("\n\n")
    print("While player 2 has gone for a more balanced and traditional setup: ")
    for i in team2:
        print(i[1])
    print("\n\n")
    
    for i in range(len(team1)):
        team1[i] = convertToDict(team1[i])
    for i in range(len(team2)):
        team2[i] = convertToDict(team2[i])

def convertToDict(pokemon: list):
    pokemonList = ["Number", "Name", "Type 1", "Type 2", "Abilities", "HP", "Att", "Def", "Special attack", "Special defence", "Speed", "BST", "Mean", "Standard Deviation", "Generation", "Experience type", 
                   "Experience to level 100", "Final Evolution", "Catch Rate", "Legendary", "Mega Evolution", "Alolan Form", "Galarian Form", "Against Normal", 
                   "Against Fire", "Against Water", "Against Electric", "Against Grass", "Against Ice", "Against Fighting", "Against Poison", "Against Ground", 
                   "Against Flying", "Against Psychic", "Against Bug", "Against Rock", "Against Ghost", "Against Dragon",  "Against Dark", "Against Steel", "Against Fairy", "Height", "Weight", "BMI"]
    pokemonDict = {}
    index = 0
    for i in pokemonList:
        pokemonDict[i] = pokemon[index]
        index += 1
    return pokemonDict

def switchTurn(turn: int):
    if turn == 0:
        turn = 1
        return turn
    turn = 0
    return turn

if __name__ == "__main__":
    baseSetup()
    turn = 0
    
    #todo Add the turn based battle system
    