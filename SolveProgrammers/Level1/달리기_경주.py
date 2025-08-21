def solution(players, callings):
    player_dict = {player: i for i, player in enumerate(players)}
    
    for call in callings:
        # idx
        players[player_dict[call]], players[player_dict[call]-1] = players[player_dict[call]-1], players[player_dict[call]]
        player_dict[call] -= 1
        player_dict[players[player_dict[call]+1]] += 1
    return players
        