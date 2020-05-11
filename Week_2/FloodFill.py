class Solution:
    def changeColor(self, image, i, j, newColor,oldColor):
        if image[i][j]!=oldColor:
            return
        image[i][j]=newColor
        if i!=0:
            self.changeColor(image,i-1,j,newColor,oldColor)
        if j!=0:
            self.changeColor(image,i,j-1,newColor,oldColor)
        if i!=len(image)-1:
            self.changeColor(image,i+1,j,newColor,oldColor)
        if j!=len(image[0])-1:
            self.changeColor(image,i,j+1,newColor,oldColor)

        
        
    def floodFill(self, image: List[List[int]], sr: int, sc: int, newColor: int) -> List[List[int]]:
        oldColor = image[sr][sc]
        if oldColor == newColor:
            return image
        
        self.changeColor(image,sr,sc,newColor, oldColor)
        return image
        
        
        