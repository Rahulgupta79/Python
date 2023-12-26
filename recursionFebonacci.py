def feb(n):
    if n==0 or n==1:
        return 1
    else:
        return feb(n-1)+feb(n-2)

print(feb(5))