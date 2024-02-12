import csv

team1 = []
team2 = []

def baseSetup():
    global team1, team2
    while True:
        pokemon = input("Please enter the name of a Pokemon: ")

        with open('cleanPokemon.csv', 'r') as file:
            reader = csv.reader(file)
            for i in reader:
                if i[1].lower() == pokemon.lower():
                    team1.append(i)
                    break
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

def switchTurn(turn: int):
    if turn == 0:
        turn = 1
        return turn
    turn = 0
    return turn

if __name__ == "__main__":
    #baseSetup()
    turn = 0
    #todo Add the turn based battle system
    