import csv

if __name__ == "__main__":
    team1 = []
    team2 = []
    while True:
        pokemon = int(input("Please enter the number of a Pokemon: "))

        with open('cleanPokemon.csv', 'r') as file:
            reader = csv.reader(file)
            for i in reader:
                if int(i[0]) == pokemon:
                    team1.append(i)
                    break
            if len(team1) == 8:
                break
    
    print("Now player 2 picks their team!")
    while True:
        pokemon = int(input("Please enter the number of a Pokemon: "))

        with open('cleanPokemon.csv', 'r') as file:
            reader = csv.reader(file)
            for i in reader:
                if int(i[0]) == pokemon:
                    team2.append(i)
                    break
        if len(team2) == 8:
            break
    print("Player 1 vs Player 2 BEGINS NOW!")
    print("Player 1 is sporting a rather interesting team: " + str(team1))
    print("While player 2 has gone for a more balanced and traditional setup: " + str(team2))