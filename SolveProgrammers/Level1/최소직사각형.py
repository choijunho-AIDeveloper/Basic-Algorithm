def solution(sizes):
    maxHeight = sizes[0][1]
    maxWidth = sizes[0][0]
    for width, height in sizes[1:]:
        if max(height, maxWidth) * max(width, maxHeight) < max(width, maxWidth) * max(height, maxHeight):
            maxWidth = max(height, maxWidth)
            maxHeight = max(width, maxHeight)
        else:
            maxWidth = max(width, maxWidth)
            maxHeight = max(height, maxHeight)
            
    answer = maxWidth * maxHeight
    return answer