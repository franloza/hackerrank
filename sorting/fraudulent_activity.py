def activityNotifications(expenditure, d):
    counting_sort = [0 for i in range(200)]
    notifications = 0
    i = d
    for c in expenditure[i-d:i]:
        counting_sort[c] += 1
    max_value = max(expenditure[i-d:i])

    while i < len(expenditure):
        if expenditure[i] >= median(expenditure[i-d:i], counting_sort, max_value) * 2:
            notifications += 1
        if expenditure[i] > max_value:
            max_value = expenditure[i]
        counting_sort[expenditure[i]] += 1
        counting_sort[expenditure[i-d]] -= 1
        i += 1

    return notifications

def median(l, counting_sort, max_value):
    sorted_l = []

    for i in range(max_value+1):
        sorted_l.extend([i]*counting_sort[i])

    length = len(sorted_l)
    if length % 2 == 0:
        # Even
        return (sorted_l[length//2 - 1] + sorted_l[length // 2]) / 2
    else:
        # Odd
        return sorted_l[length // 2]

if __name__ == "__main__":
    activityNotifications([2,3,4,2,3,6,8,4,5], 5)