def Main():
    ans = {}
    n = int(input("Enter the value of n:"))
    if n<1:
        raise IndexError("Please enter positive value")
    else:
        for i in range(1,n+1):
            ans[i] = i * i
        print(ans)
if __name__ == '__main__':
    Main() 
