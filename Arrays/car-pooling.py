import math

# There is a car with capacity empty seats. The vehicle only drives east (i.e.,
#    it cannot turn around and drive west).

# You are given the integer capacity and an array trips where trips[i] = [numPassengersi, fromi,
#    toi] indicates that the ith trip has numPassengersi passengers and the locations to pick them up
#    and drop them off are fromi and toi respectively. The locations are given as the number of
#    kilometers due east from the car's initial location.
#
# Return true if it is possible to pick up and drop off all passengers for all the given trips, or false otherwise.

# trips = [[2,1,5],[3,3,7]], capacity = 4 --> false
# trips = [[2,1,5],[3,3,7]], capacity = 5 --> true

# Constraints:
#   1 <= trips.length <= 1000
#   trips[i].length == 3
#   1 <= numPassengersi <= 100
#   0 <= fromi < toi <= 1000
#   1 <= capacity <= 105

# Trick: for each trip add the number of people getting in at the starting point,
#   and subtract the number of people getting out at the stopping point. Using a separate array and its indexes
#   to represent a unit of distance, and the value to represent the number of current riders'

# This solution is generic and doesn't depend on the trips.length or the fromi toi constraints


def car_pooling(trips, capacity):
    max_distance = -math.inf
    for trip in trips:
        if trip[2] > max_distance:
            max_distance = trip[2]

    capacity_accumulator = [0] * (max_distance + 1)
    for num_riders, start, stop in trips:
        capacity_accumulator[start] += num_riders
        capacity_accumulator[stop] -= num_riders

    capacity_accumulator_length = len(capacity_accumulator)
    current_riders = 0
    for i in range(capacity_accumulator_length):
        current_riders += capacity_accumulator[i]
        if current_riders > capacity:
            return False

    return True

print(car_pooling([[2,1,5],[3,3,7]], 4))
print(car_pooling([[2,1,5],[3,3,7]], 5))