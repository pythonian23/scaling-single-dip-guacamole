# Find which quadrant a coordinate is in. Anything with 0 is undefined because I'm lazy :/
get_quadrant = lambda coord: (int(coord[0] > 0)^int(coord[1] > 0))+2*int(coord[1]<0)+1

print(get_quadrant((1,1)))
print(get_quadrant((-1,1)))
print(get_quadrant((1,-1)))
print(get_quadrant((-1,-1)))
