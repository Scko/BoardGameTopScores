import csv

def main():
    games, entries = GetGames()
    print(ScoreGames(games, entries))


def ScoreGames(games, entries):
    #PrintGameNames(games)
    for game in games:
        games[game] = games[game]/entries
    sortedGames = sorted(games.items(), key=lambda x: x[1], reverse=True)
    return sortedGames

def GetGames():
    with open('games.csv', mode='r') as file:
        reader = csv.reader(file, delimiter=',')
        score = sum(1 for row in file) - 1
        file.seek(0)
        entries = 0
        games = {}
        next(reader, None)
        for row in reader:
            entries = len(row)
            for i in range(0,len(row)):
                if row[i] in games:
                    games[row[i]] += score
                else:
                    games[row[i]] = score
            score -= 1
    return games, entries

def PrintGameNames(games):
    keys = []
    for key in games.keys():
        keys.append(key)
    keys.sort()
    print(keys)

if __name__ == "__main__":
    main()
