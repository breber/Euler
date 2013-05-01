'''
By starting at the top of the triangle below and moving to adjacent numbers on the row below, the maximum total from top to bottom is 23.

       3
      7 4
     2 4 6
    8 5 9 3

That is, 3 + 7 + 4 + 9 = 23.

Find the maximum total from top to bottom of the triangle in extra/problem018.txt
'''

def find_longest_path(triangle):
    """
    Finds the longest path down the triangle.

    We start at the top of the triangle. We then go row-by-row, updating
    each node's number with the value of it's greatest parent plus its own
    value. Since we have found the longest distance to the parents, the longest
    distance to the current level will be the longest path to the parent plus
    the value of the current node.
    """
    for row in range(1, len(triangle)):
        l = 0
        for r in range(0, len(triangle[row])):
            # Edge of the triangle (only one parent)
            if r == 0 or r == len(triangle[row]) - 1:
                maxParent = triangle[row - 1][l]
            else:
                parentL = triangle[row - 1][l]
                parentR = triangle[row - 1][l + 1]
                maxParent = max(parentL, parentR)
            
            triangle[row][r] = maxParent + triangle[row][r]
            
            if r != 0:
                l += 1


triangle = []

file = open("extra/problem018.txt")
for line in file:
    row = []
    items = line.split(' ')
    
    for item in items:
        row.append(int(item))

    triangle.append(row)

find_longest_path(triangle)

print max(triangle[len(triangle) - 1])
