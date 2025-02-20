import math

def path_length(trail):
    total_length = 0
    for i in range(1, len(trail)):
        x1, y1 = trail[i - 1]
        x2, y2 = trail[i]
        segment_length = math.sqrt((x2 - x1)**2 + (y2 - y1)**2)
        total_length += segment_length
    return total_length

trail = [(142.492, 208.536),
(142.658, 207.060),
(143.522, 205.978),
(145.009, 205.546)]

length = path_length(trail)
print(f"The total length of the trail is: {length:.3f} units")