__author__ = 'spark'
# Maximum Subarray Problem


def max_subarray_linear(A):  #O(n)
    max_ending_here = max_so_far = A[0]
    for x in A[1:]:
        max_ending_here = max(x, max_ending_here + x)
        max_so_far = max(max_so_far, max_ending_here)
    return max_so_far


def max_subarray_quadratic(A):  # O(n^2)
    max_so_far = 0;
    for i in range(len(A)):    # for (i = 0; i < n; i++)
        sum = 0
        for j in range(i, len(A)):   # for (j = i; j < n; j++)
            sum += A[j]
            max_so_far = max(sum, max_so_far)
    return max_so_far


def max_subarray_cubic(A):
    max_so_far = 0
    for i in range(len(A)):         # for(i = 0; i < n; i++)
        for j in range(i, len(A)):  # for(j = i; j < n; j++) {\
            sum = 0
            for k in range(i, j+1):  # for (k = i; k <= j; k++)
                sum += A[k]
                max_so_far = max(sum, max_so_far)
    return max_so_far


def max_subarray_recursive(l, u, A):  # O(nlogn)
    if l > u:   # zero elements
        return 0
    if l == u:  # one element
        return max(0, A[l])
    m = (l+u) / 2
    # find max crossing to left
    lmax = sum = 0
    for i in range(m, l-1, -1):   # for (i=m; i>=l i--)
        sum += A[i]
        lmax = max(sum, lmax)
    # find max crossing to right
    rmax = sum = 0
    for j in range(m+1, u+1):     # for(i=m+1; i<=u; i++)
        sum += A[j]
        rmax = max(sum, rmax)

    return max(max(max_subarray_recursive(l, m, A), max_subarray_recursive(m+1, u, A)), lmax + rmax)


if __name__ == '__main__':               # linear algorithm
    A = [-2, 1, -3, 4, -1, 2, 1, -5, 4]  # 4, -1, 2, 1 = 6  (runtime complexity o(n))  Kadane's algorithm
    print(max_subarray_linear(A))

    print(max_subarray_quadratic(A))

    print(max_subarray_cubic(A))

    print(max_subarray_recursive(0, len(A)-1, A))
