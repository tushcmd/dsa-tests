def triangle_sum(n):
    # Initialize the triangle with the first row
    triangle = [[1]]
    total_sum = 1

    for row in range(2, n + 1):
        # Start new row with 1
        new_row = [1]
        
        # Calculate middle numbers
        for i in range(1, row - 1):
            num = (triangle[-1][i-1] + triangle[-1][i]) * row
            new_row.append(num)
        
        # End row with 1
        new_row.append(1)
        
        # Multiply each number in the row by the row number
        new_row = [num * row for num in new_row]
        
        # Add the sum of this row to the total
        total_sum += sum(new_row)
        
        # Add the new row to the triangle
        triangle.append(new_row)

    return total_sum

# Test the function
n = 9
result = triangle_sum(n)
print(f"For n = {n}, the total sum is: {result}")

# def triangle_sum(n):
       
#        triangle = [[1]]
#        total_sum = 1
       
#        for row in range(2, n+1):
           
#            next_row = [1]
           
#            for col in range(1, row-1):
#                next_row.append(triangle[row-2][col-1] + triangle[row-2][col])
               
#            next_row.append(1)
           
#            triangle.append(next_row)
           
#            total_sum += sum(next_row)
           
#        return total_sum
   
# n = 9
# result = triangle_sum(n)
# print(f"For n = {n}, the total sum is: {result}")