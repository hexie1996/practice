class Solution(object):
    def spiralOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        if (matrix == []):
            return []
        if (len(matrix) > 0):
            lenth_row = len(matrix[0])
        lenth_column = len(matrix)
        flag_row = 1
        flag_column = 0
        num_row = 0
        num_column = 0
        result = []
        current_row = 0
        current_column = 0
        while (1):
            result.append(matrix[current_column][current_row])
            if (flag_row == 1):
                if (current_row == lenth_row - int(num_column / 2) - 1):
                    flag_row = 0
                    flag_column = 1
                    num_row = num_row + 1
            elif (flag_row == -1):
                if (current_row == int(num_column / 2)):
                    flag_row = 0
                    flag_column = -1
                    num_row = num_row + 1
            elif (flag_column == 1):
                if (current_column == lenth_column - int(num_row / 2) - 1):
                    flag_row = -1
                    flag_column = 0
                    num_column = num_column + 1
            else:
                if (current_column == int(num_row / 2)):
                    flag_row = 1
                    flag_column = 0
                    num_column = num_column + 1
            current_row = current_row + flag_row
            current_column = current_column + flag_column
            if (len(result) == lenth_row * lenth_column):
                break
        return result
