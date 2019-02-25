#Fill: Implement the "paint nil" function that one might see on many image editing programs.
# That is, given a screen (represented by a two-dimensional array of colors), a point, and a new color,
# nil in the surrounding area until the color changes from the original color.


def path_fill(image,sr,sc,new_color):
    rows = len(image)
    cols = len(image[0])
    original_color = image[sr][sc]
    def dfs(row,col):
        if not (0<=row < rows and 0 <= col < cols) or original_color != image[row][col]:
            return
        image[row][col] = new_color

        [dfs(row+x,col+y) for x,y in ((0,1),(0,-1),(1,0),(-1,0))]
    if original_color != new_color:
        dfs(sr,sc)
    return image


image1 = [[10, 10, 10, 10, 10, 10, 10, 40],
        [30, 20, 20, 10, 10, 40, 40, 40],
        [10, 10, 20, 20, 10, 10, 10, 10],
        [10, 10, 30, 20, 20, 20, 20, 10],
        [40, 40, 10, 10, 10, 10, 10, 10]]

image2 = [[30, 30, 30, 30, 30, 30, 30, 40],
              [30, 20, 20, 30, 30, 40, 40, 40],
              [10, 10, 20, 20, 30, 30, 30, 30],
              [10, 10, 30, 20, 20, 20, 20, 30],
              [40, 40, 30, 30, 30, 30, 30, 30]]
image3 = path_fill(image1,3,1,40)
print(image3)
