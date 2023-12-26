n=int(input("Enter a number="))

def pattern(n):
    i=1
    while(i<=n):
        j=1
        while(j<=i):
            print("*",end="")
            j+=1
        i+=1
        print()
    i=1
    while(i<=n):
        print("*"*i)
        i+=1

    for i in range(1,n+1):
        for j in range(1,i+1):
            print("*",end="")
        print()
    '''
    *
    **
    ***
    ****
    *****
    '''
def pattern1(n):
    i=1
    j=1
    while(i<=n):
        j=n
        while(j>=i):
            print("*",end="")
            j-=1
        i+=1
        print()


    for i in range(n,0,-1):
        for j in range(1,i+1):
            print("*",end="")
        print()

    '''
    *****
    ****
    ***
    **
    *
    '''

def pattern2(n):
    i=1
    while(i<=n):
        j=1
        while(j<=i):
            print(j,end="")
            j+=1
        i+=1
        print()

    for i in range(1,n+1):
        for j in range(1,i+1):
            print(j,end="")
        print()
    '''
    1
    12
    123
    1234
    12345
    '''

def pattern3(n):
    i=0
    while(i<n):
        j=1
        while(j<=n-i):
            print(j,end="")
            j+=1
        i+=1
        print()


    for i in range(n,0,-1):
        for j in range(1,i+1):
            print(j,end="")
        print()

    '''
    12345
    1234
    123
    12
    1
    '''
def pattern4(n):
    i=1
    j=1
    while(i<=n):
        j=n
        while(j>=i):
            print(j,end="")
            j-=1
        print()
        i+=1

    for i in range(0,n):
        for j in range(n,i,-1):
            print(j,end="")
        print()
    '''
    54321
    5432
    543
    54
    5
    '''
# -----------------------------------------------------------------------
pattern(n)
pattern1(n)
pattern2(n)
pattern3(n)
pattern4(n)