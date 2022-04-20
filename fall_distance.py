# Author: Thomas Wunz
# GitHub username: wunzt
# Date: 4/19/2022
# Description: Function takes the time in seconds and returns the distance fallen in meters.

def fall_distance(time):
    """Takes the time in seconds and returns distance fallen in meters."""
    d = 0.5 * 9.8 * time ** 2
    return(d)

time = float(input())
dist = fall_distance(time)
print(dist)