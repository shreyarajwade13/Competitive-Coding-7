"""
Binary Search approach --

TC - O(n log(max-min))
where n ==> traversal
max = max element array
min = min element in array

SC - O(1)
"""


class Solution:
    def countElements(self, matrix, mid, rows, cols):
        total = 0
        # start from last row
        col = cols - 1

        for row in range(rows):
            while col >= 0 and matrix[row][col] > mid:
                col -= 1
            total += (col + 1)
        return total

    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        if matrix is None or len(matrix) == 0 or k is None: return -1

        rows = len(matrix)
        cols = len(matrix[0])

        n = len(matrix)

        start = matrix[0][0]
        end = matrix[n - 1][n - 1]

        while start <= end:
            # step 1: calculate mid
            # mid = 8
            # mid = 4
            # mid = 6
            mid = start + (end - start) // 2

            # step 2: count elements <= mid
            # count = 2
            # count = 1
            # count = 2
            count = self.countElements(matrix, mid, rows, cols)

            # step 3: check cases
            # count >= k ==> 2
            # count >= k ==> 2
            if count >= k:
                end = mid - 1
            else:
                # start ==> 5 end ==> 7
                start = mid + 1

        return start
