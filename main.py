#Given that you have random points between (0,1) plotted out evenly, calculate Pi
#What do we know?
## C = 2(Pi)r
## A = (Pi)r^2
## (Pi) = A/(r^2)

#Calculate everything within a circle of range. a^2 + b^2 = c^2 -- get points where c < 1, then you have all points within a circle, do maths, then Pi.

#Also side note; I know this is Python, I should be using snake_case ... deal with it.

import random

def getPiValue(n):
    numberPointsWithinCircle = 0
    numberPointsTotal = 0

    for i in range(n):
        xPoint = random.uniform(0, 1)
        yPoint = random.uniform(0, 1)

        distance = xPoint**2 + yPoint**2

        numberPointsTotal += 1
        if distance <= 1:
            numberPointsWithinCircle += 1

    return 4 * numberPointsWithinCircle/numberPointsTotal # 4 as ^ > ˅ <

# Obviously with more points it gets more accurate, but takes more time.
print("Pi is roughly: ", getPiValue(100000))
