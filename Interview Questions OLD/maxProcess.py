from collections import deque 

def maxProcessPower(processingPowers, boostingPowers, powerMax):
    n = len(processingPowers)
    i, j = 0, 0
    
    q = deque([])
    sum = 0
    ans = 0
    while j < n:
        sum += processingPowers[j]
        while not len(q) == 0 and q[0][0] <= boostingPowers[j]:
            q.popleft()

        q.append((boostingPowers[j], j))
        
        while i <= j and q[-1][0] + sum*(j-i+1) > powerMax:
            if q[-1][1] == i:
                q.pop()
            
            sum -= processingPowers[i]
            i += 1
        
        ans = max(ans, j-i+1)
        j += 1
    
    return ans

if __name__ == "__main__":
    print(maxProcessPower([3, 6, 1, 3, 4], [2, 1, 3, 4, 5], 25)) #2
    print(maxProcessPower([8,8,10,9,12], [4,1,4,5,3], 33)) #2
    print(maxProcessPower([11,12,19], [10,8,7], 6)) #0