def longestSubarrayWithSumK(arr, n, k):
    max_len = 0
    i = j = 0
    sum = arr[0]

    while j < n:
        if sum == k:
            max_len = max(max_len, j - i + 1)
            j += 1
            if j < n:
                sum += arr[j]
        elif sum < k:
            j += 1
            if j < n:
                sum += arr[j]
        elif sum > k:
            if i == j:
                i += 1
                j += 1
                if j < n:
                    sum = arr[j]
            else:
                sum -= arr[i]
                i += 1

    return max_len


def main():
    n, k = map(int, input().split())
    arr = list(map(int, input().split()))

    result = longestSubarrayWithSumK(arr, n, k)
    print(result)


if __name__ == "__main__":
    main()
