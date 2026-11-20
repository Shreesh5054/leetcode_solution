class Solution:
    def largestAltitude(self, gain: list[int]) -> int:
        altitude = 0
        maximum = 0

        for i in gain:
            altitude += i
            maximum = max(maximum, altitude)

        return maximum 