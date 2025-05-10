# Task https://www.codewars.com/kata/52b7ed099cdc285c300001cd/train/python

def sum_of_intervals(intervals):
    if not intervals:
        return 0

    sorted_intervals = sorted(intervals, key=lambda x: x[0])

    merged = [list(sorted_intervals[0])]

    for current in sorted_intervals[1:]:
        current_start, current_end = current
        last_start, last_end = merged[-1]

        if current_start <= last_end:
            merged[-1][1] = max(last_end, current_end)
        else:
            merged.append(list(current))

    total = 0
    for interval in merged:
        total += interval[1] - interval[0]

    return total