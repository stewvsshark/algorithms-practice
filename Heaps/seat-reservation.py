import heapq

# SeatManager(int n) Initializes a SeatManager object that will manage n seats numbered from 1 to n.
#   All seats are initially available.
# int reserve() Fetches the smallest-numbered unreserved seat, reserves it, and returns its number.
# void unreserve(int seatNumber) Unreserves the seat with the given seatNumber.

# Constraints:
#   For each call to reserve, it is guaranteed that there will be at least one unreserved seat.
#   For each call to unreserve, it is guaranteed that seatNumber will be reserved.


class SeatManager:
    def __init__(self, n):
        self.n = n
        self.seat_queue = list(range(1, n+1))
        heapq.heapify(self.seat_queue)

    def reserve(self):
        seat_num = heapq.heappop(self.seat_queue)
        return seat_num

    def un_reserve(self, seat_number):
        heapq.heappush(self.seat_queue, seat_number)

