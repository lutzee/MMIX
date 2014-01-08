m=6099
n=2166

def elucidmn(m,n):
    m=m%n
    print 'm= {0} n= {1}'.format(m,n)
    if m==0:
        return(n)
    else:
        return elucidnm(n,m)

def elucidnm(n,m):
    n=n%m
    print 'n= {0} m= {1}'.format(n,m)
    if n==0:
        return m
    else:
        return elucidmn(m,n)

def elucid(m,n):
    r=m%n
    print 'm= {0}, n= {1}'.format(m,n)
    if r==0:
        return n
    else:
        m=n
        n=r
        return elucid(m,n)


print elucidmn(m,n)
print elucid(m,n)

