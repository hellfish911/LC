def maxdepth(h):
    n = len(h)
    left = 0
    right = n - 1
    lmax = rmax = 0
    best = 0

    while left <= right:
        if h[left] <= h[right]:
            if h[left] >= lmax:
                lmax = h[left]
            else:
                best = max(best, lmax - h[left])
            left += 1
        else:
            if h[right] >= rmax:
                rmax = h[right]
            else:
                best = max(best, rmax - h[right])
            right -= 1

    return best


heights = [1, 2, 5, 6, 1, 2, 2, 3, 0, 1, 5, 6, 7, 5, 5, 7, 8, 8, 2]
print(maxdepth(heights))
