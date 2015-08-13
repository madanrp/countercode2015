__author__ = 'madanp'
import sys
def get_diff_count(m, n):
    #m, n = min([m,n]), max([m,n])
    if m == n or (n - m) <= 1:
        return 0
    m_even = (m%2 == 0)
    n_even = (n%2 == 0)

    if (m_even and n_even):
        return (n - m)/2 -1
    elif not m_even and not n_even:
        return  (n-m)/2 - 1
    elif m_even and not n_even:
        return (n - (m+1))/2 - 1
    elif not m_even and n_even:
        return (n - 1 - m) /2 -1

n, k = map(int, raw_input().split())
a = map(int, raw_input().split())
a.sort()
len_a = len(a)
count = 0

if len_a == 0:
    print n/2 if n%2 == 0 else n/2 + 1
else:
    total_possible = (n/2 if n%2 == 0 else n/2 + 1)
    if len_a == total_possible:
        print len_a
        sys.exit()


    first_elem = a[0]
    if first_elem % 2 == 0:
        count += get_diff_count(0, first_elem)
    else:
        count += get_diff_count(1, first_elem)
        if first_elem > 1:
            count += 1

    for i in range(1, len_a):
        curr = a[i]
        prev = a[i-1]
        count += get_diff_count(prev, curr)

    last_elem = a[-1]
    count += (get_diff_count(last_elem, n) + 1)
    print count + len_a








