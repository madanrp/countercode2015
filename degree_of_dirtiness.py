__author__ = 'madanp'

test_cases = int(raw_input())
for i in range(test_cases):
    n, m = map(int, raw_input().strip().split())
    if n == 1:
        print "%d %d" % (1, m-1)
    elif m < n:
        if m %2 == 0:
            print "%d %d" % (n - (m/2) + 1, 0)
        else:
            print "%d %d" % ((m/2 + 1), 0)
    elif m == n:
        print int(m/2) + 1, 0
    else:
        n_even = (n % 2 == 0)
        m_even = (m %2 == 0)
        if n_even and m_even:
            rem = (m%n)
            dividend = (m / n)
            if rem == 0:
                print "%d %d" % ( (n/2)+1, dividend - 1)
            else:
                print n - (rem/2) + 1, dividend
        elif n_even and not m_even:
           rem = (m%(n-1))
           dividend = m / (n-1)
           if rem == 0:
               print "%d %d" % (1, dividend)
           else:
               print "%d %d" % ((rem/2)+2, dividend)
        elif not n_even and m_even:
            rem = m % n
            dividend = m / n
            if rem == 0:
                print "%d %d" % (n/2 +1, dividend-1)
            else:
                print "%d %d" % (n - (rem/2), dividend)
        elif not n_even and not m_even:
            rem = m % n
            dividend = m / n
            print "%d %d" %  (rem/2 +1, dividend)



