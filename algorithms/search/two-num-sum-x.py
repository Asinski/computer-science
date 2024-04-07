def twotermswithsumx2(nums, x):
    prevnums = set()
    for nownum in nums:
        if x - nownum in prevnums:
            return nownum, x - nownum
        prevnums.add(nownum)
    return 0, 0
