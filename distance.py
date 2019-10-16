import math
def distance(x1, y1, x2, y2):
    dist = round(math.hypot(x2 - x1, y2 - y1),2)
    print(dist)
    return dist