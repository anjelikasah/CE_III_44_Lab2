#print('enter data seperated by space')
#A=list(map(int,input().split()))
def insertion(A):
    for j in range(1, len(A)):
        key=A[j]
        i=j-1

        while i>=0 and A[i]>key:
            A[i+1]=A[i]
            i=i-1

        A[i+1]=key
#insertion(A)
#print(A)
