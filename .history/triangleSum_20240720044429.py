# function triangleSum(n) {
#     let total = 0;
#     for (let i = 1; i <= n; i++) {
#         let rowSum = (i * (i + 1)) / 2;
#         total += rowSum;
#     }
#     return total;
# }

def triangleSum(n):
    total = 0
    for i in range(1, n+1):
        rowSum = (i * (i + 1)) / 2
        total += rowSum
    return total

print(triangleSum(9))