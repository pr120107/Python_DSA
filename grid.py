'''
Puzzle | Ways to Reach Bottom Right in 6x6 Grid
You begin in the top left corner of a 6x6 grid, and your objective is to move to the bottom right corner. There are just two directions you can move: right or down. Both diagonal and backward movements are prohibited.
How many different ways are there to get from the start to the finish?
(i,j)
i++(+1 for every right move) or j++(+1 for every bottom move)
(1,1),(1,2),(1,3),(1,4),(1,5),(1,6)
(2,1),(2,2),(2,3),(2,4),(2,5),(2,6)
(3,1),(3,2),(3,3),(3,4),(3,5),(3,6)
(4,1),(4,2),(4,3),(4,4),(4,5),(4,6)
(5,1),(5,2),(5,3),(5,4),(5,5),(5,6)
(6,1),(6,2),(6,3),(6,4),(6,5),(6,6)
total:-432(12*36)-1
'''
# arr=[
#     [1,2,3,4,5,6],
#     [7,8,9,10,11,12],
#     [13,14,15,16,17,18],
#     [19,20,21,22,23,24],
#     [25,26,27,28,29,30],
#     [31,32,33,34,35,36]
# ]#6*6=
# for i in range(len(arr)):
#     for j in range(len(arr)):
#         print( arr[i][j],end=" ")
#     print()
def count_paths(m, n):
    # Create a 2D array to store the number of paths to each cell
    dp = [[0] * n for _ in range(m)]
    
    # There is only one way to reach any cell in the first row or first column
    for i in range(m):
        dp[i][0] = 1
    for j in range(n):
        dp[0][j] = 1
    
    # Fill the rest of the dp array
    for i in range(1, m):
        for j in range(1, n):
            dp[i][j] = dp[i-1][j] + dp[i][j-1]
    
    return dp[m-1][n-1]
if __name__ == "__main__":
    m, n = 6, 6  # Grid size
    total_paths = count_paths(m, n)
    print(f"Total ways to reach bottom right in a {m}x{n} grid: {total_paths}")