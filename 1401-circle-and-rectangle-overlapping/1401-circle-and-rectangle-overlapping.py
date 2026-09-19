class Solution:
    def checkOverlap(self, radius: int, xCenter: int, yCenter: int, x1: int, y1: int, x2: int, y2: int) -> bool:
        xi = xCenter
        yi = yCenter
        if xCenter < x1:
            xi = x1
        elif xCenter > x2:
            xi = x2
        if yCenter < y1:
            yi = y1
        elif yCenter > y2:
            yi = y2
        d = (xi - xCenter )**2 + (yi - yCenter)**2
        if d <= radius ** 2:
            return True
        else:
            return False