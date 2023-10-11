def maxSubarrayLength(badges):
    negPos = -1
    maxLen = 0
    noOfNeg = 0

    for i in range(len(badges)):
        if badges[i] < 0:
            noOfNeg += 1
            if negPos == -1:
                negPos = i
        else:
            if noOfNeg % 2 == 0:
                maxLen = max(i- negPos, maxLen) #TBC
            else:
                maxLen = max(i - negPos, maxLen)

    return maxLen 

if __name__ == "__main__":
    # print(maxSubarrayLength([1,1,1,1,1])) #5
    print(maxSubarrayLength([1, -1, -1, 1, 1, -1])) #5
    print(maxSubarrayLength([1, -1, -1, -1, 1, 1])) #4
    print(maxSubarrayLength([-1,1,-1,1])) #4