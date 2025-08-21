def solution(board, h, w):
    count = 0
    if h > 0:
        if board[h - 1][w] == board[h][w]:
            count += 1
    if h < len(board) - 1:
        if board[h + 1][w] == board[h][w]:
            count += 1
    if w > 0:
        if board[h][w - 1] == board[h][w]:
            count += 1
    if w < len(board[0]) - 1:
        if board[h][w + 1] == board[h][w]:
            count += 1
    return count