
# Aim: Return a list of lists of pascals triangle. 

def pascals_triangle(numRows: int) -> list[list]:
    if numRows == 1:
        return [[1]]
    elif numRows == 2:
        return [[1], [1,1]]
    else:
        triangle_above = pascals_triangle(numRows-1)
        previous_layer = triangle_above[-1]
        new_layer = [1] * numRows
        index_1 = 0
        index_2 = 1
        pos = 1
        # Stop when first index is the second to last position of previous layer.
        while index_1 != numRows-2:
            new_layer[pos] = previous_layer[index_1] + previous_layer[index_2]
            index_1 += 1
            index_2 += 1
            pos += 1
        triangle_above.append(new_layer)
        return triangle_above


# Test cases:
print(pascals_triangle(3))
print(pascals_triangle(4))
print(pascals_triangle(5))
