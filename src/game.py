def initPlayers():
    global PlayerList
    PlayerList = []

def createNewPlayer(name, damage=0, defensePower=0):
    return dict(
        name=name,
        score=0,
        damage=damage,
        health=100,
        defensePower=defensePower,
        defense=False,
    )

def addPlayer(Player):
    global PlayerList
    PlayerList.append(Player)

def removePlayer(nama):
    global PlayerList
    for i in PlayerList:
        if i["name"]==nama:
            PlayerList.remove(i)
            return
    print("There is no player with that name!")

def setPlayer(player, key, value):
    if key in player:
        player[key] = value
        return

def attackPlayer(attacker, target):
    if target["defense"]:
        attacker_damage = max(attacker["damage"] - target["defensePower"], 0)
    else:
        attacker_damage = attacker["damage"]

    score = round(attacker["score"] + 1 - 1 / target["defensePower"] if target['defense'] else 1, 2)
    health = max(target["health"] - attacker_damage, 0)

    setPlayer(attacker, "score", score)
    setPlayer(target, "health", health)
    setPlayer(target, "defense", False)

def displayMatchResult():
    global PlayerList
    sorted_data = sorted(PlayerList, key=lambda x: (-x["score"], -x["health"]))
    for i in range(len(sorted_data)):
        print(f"Rank {i+1}: {sorted_data[i]["name"]} | Score: {sorted_data[i]["score"]} | Health: {sorted_data[i]["health"]}")