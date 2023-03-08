
def rectangle(n,m):
    base =1

    for i in range(1,n+1):
        for j in range(1,m+1):

            if (i==1 or i==n) or (j==1 or j==m )and (i-- and j--):
                print('4',end=" ")

            else:
                print(" ",end=" ")




        print()

r = rectangle(7,7)
print(r)