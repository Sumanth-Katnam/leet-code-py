def solution(A):
    count = 1
    length = len(A)
    maxConsecutive = length - 1
    for i in range(length - 1, 0 , -1):
        turnOn = A[i]
        maxConsecutive = min(maxConsecutive, turnOn - 1)
        if maxConsecutive == i:
            count += 1
        elif maxConsecutive == 0:
            break
    return count



def solutionB(A):
    max = -1
    sum, moments, should_be_tot = 0, 0, 0
    for i in A:
        if max < i:
            max = i
            should_be_tot = (max*(max + 1))/2
        
        sum += i

        if sum == should_be_tot:
            moments += 1

    return moments

        
if __name__ == "__main__":
    print(solution([2,1,3,5,4]))
    print(solution([2,3,4,1,5]))
    print(solution([1,3,4,2,5]))
    print(solution([5,4,3,2,1]))
    print("------------------")
    print(solutionB([2,1,3,5,4]))
    print(solutionB([2,3,4,1,5]))
    print(solutionB([1,3,4,2,5]))