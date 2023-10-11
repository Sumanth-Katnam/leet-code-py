def countSignals(frequencies, filtersRanges):
    start = filtersRanges[0][0]
    end = filtersRanges[0][1]

    for s,e in filtersRanges:
        if start < s:
            start = s
        if end > e:
            end = e

    count = 0
    for i in frequencies:
        if start <= i <= end:
            count += 1

    return count


print(countSignals([8, 15, 14, 16, 21], [[10, 17], [13, 15], [13, 17]]))
print(countSignals([8, 11, 14, 16, 21], [[10, 16], [13, 15], [8, 9]]))
print(countSignals([20, 5, 6, 7, 12], [[10, 20], [5, 15], [5, 30]]))