def minimumGroups(awards, k):
    awards.sort()
    min_award = awards[0]
    count = 1
    for award in awards:
        if award - min_award > k:
            count += 1
            min_award = award
    return count


if __name__ == "__main__":
    print(minimumGroups([1,5,5,6,8,9,2], 3)) #3
    print(minimumGroups([1,13,6,8,9,3,5], 4)) #3
    print(minimumGroups([3,1,4,3,9], 10)) #1