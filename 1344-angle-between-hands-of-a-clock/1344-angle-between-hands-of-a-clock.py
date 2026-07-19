class Solution:
    def angleClock(self, hour: int, minutes: int) -> float:
        degree_of_hour = (hour % 12 ) * 30 
        degree_of_minutes = minutes * 6
        movement_of_hour_by_minutes = minutes * 0.5
        angle = abs(degree_of_hour + movement_of_hour_by_minutes - degree_of_minutes)
        return min(angle, 360 - angle)
