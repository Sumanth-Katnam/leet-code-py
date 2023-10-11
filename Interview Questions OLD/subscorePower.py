def optimalScoresOfSubArrays(arr):
    prefixSums = []
    positionElementProdSums = []
    positionElementProdSumsReverse = []
    runningSum = 0
    posElementProdSum = 0
    n = len(arr)
    for i in range(n):
        runningSum += arr[i]
        posElementProdSum += (i+1) * arr[i]
        prefixSums.append(runningSum)
        positionElementProdSums.append(posElementProdSum)
    posElementProdSum = 0
    for i in range(n-1,-1,-1):
        posElementProdSum += (n-i) * arr[i]
        positionElementProdSumsReverse.append(posElementProdSum)
        
    sum = lambda sums, l, r: sums[r] - (sums[l-1] if l-1>=0 else 0) if l <= r else 0
    totalScore = 0
    stack = []
    for i in range(n):
        while stack and arr[stack[-1][0]] > arr[i]:
            minElementIndex, leftIndex = stack.pop()
            rightIndex = i
            rightCount = rightIndex - minElementIndex
            leftCount = minElementIndex - leftIndex
            minElement = arr[minElementIndex]
            shiftedPosEleProdSum = sum(positionElementProdSums, leftIndex + 1, minElementIndex) - sum(prefixSums, leftIndex  + 1, minElementIndex) * (leftIndex  + 1)
            currRangeScore = rightCount * minElement * shiftedPosEleProdSum
            totalScore += currRangeScore
            shiftedPosEleProdSum = sum(positionElementProdSumsReverse, n-rightIndex, n-minElementIndex-2) - sum(prefixSums, minElementIndex+1, rightIndex-1)*(n-rightIndex)
            currRangeScore = leftCount * minElement * shiftedPosEleProdSum
            totalScore += currRangeScore
        if not stack: stack.append((i, -1))
        else: stack.append((i, stack[-1][0]))
    while stack:
        minElementIndex, leftIndex = stack.pop()
        rightIndex = n
        rightCount = rightIndex - minElementIndex
        leftCount = minElementIndex - leftIndex
        minElement = arr[minElementIndex]
        shiftedPosEleProdSum = sum(positionElementProdSums, leftIndex + 1, minElementIndex) - sum(prefixSums, leftIndex  + 1, minElementIndex) * (leftIndex  + 1)
        currRangeScore = rightCount * minElement * shiftedPosEleProdSum
        totalScore += currRangeScore
        shiftedPosEleProdSum = sum(positionElementProdSumsReverse, n-rightIndex, n-minElementIndex-2) - sum(prefixSums, minElementIndex+1, rightIndex-1)*(n-rightIndex)
        currRangeScore = leftCount * minElement * shiftedPosEleProdSum
        totalScore += currRangeScore
    return totalScore
