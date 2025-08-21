def solution(bandage, health, attacks):
    from collections import deque
    time = 0
    attacks = deque(attacks)
    start = attacks[0][0]
    end = attacks[-1][0] + 1
    maxHealth = health
    time = 0
    for i in range(start, end):
        if i == attacks[0][0]:
            health -= attacks[0][1]
            if health <= 0:
                return -1
            time = 0
            attacks.popleft()
            continue
        if health < maxHealth and time >= 0:
            health += bandage[1]
            time += 1
            if health >= maxHealth: health = maxHealth
        if time == bandage[0]:
            health += bandage[2]
            if health >= maxHealth: health = maxHealth
            time = 0
    return health