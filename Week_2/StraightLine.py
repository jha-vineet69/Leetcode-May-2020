#My Solution:
#Problems: Unreadable at some place, unoptimised formula
class Solution:
    def checkStraightLine(self, coordinates: List[List[int]]) -> bool:
        if len(coordinates)==2:
            return True
        for i in range(len(coordinates)-2):
            if(self.distance(coordinates[i][0],coordinates[i][1],coordinates[i+1][0],coordinates[i+1][1],coordinates[i+2][0],coordinates[i+2][1])!=0):
                return False
        return True
        
        
    def distance(self, x1, y1, x2, y2, x3, y3):
        return (x1*(y2-y3) + x2*(y3-y1) + x3*(y1-y2))


#Better Solution:
#Concise, Optimised
class Solution:
    def checkStraightLine(self, coordinates: List[List[int]]) -> bool:
        if len(coordinates)==2:
            return True
        x0,y0 = coordinates[0]
        x1,y1 = coordinates[1]
        for i in range(2,len(coordinates)):
            x,y = coordinates[i]
            if(y1-y0)*(x-x0)!=(y-y0)*(x1-x0):
                return False
        return True
        
                 
            
        