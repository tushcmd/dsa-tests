

def triangle_sum(n):
       
       triangle = [[1]]
       total_sum = 1
       
       for row in range(2, n+1):
           
           next_row = [1]
           
           for col in range(1, row-1):
               next_row.append(triangle[row-2][col-1] + triangle[row-2][col])
               
           next_row.append(1)
           
           triangle.append(next_row)
           
           total_sum += sum(next_row)
           
       return total_sum
   
n = 9
result = triangle_sum(n)
print(f"For n = {n}, the total sum is: {result}")