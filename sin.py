# approximate sin, once again, in a single line
import math

fact = lambda x: 2 if x == 2 else x*fact(x-1);sin = lambda angle, precision: angle+sum([(((i+1)%4)-1)*(angle**i)/fact(i) for i in range(3, 2*precision+2)])

print(sin(math.pi/6, 50))
