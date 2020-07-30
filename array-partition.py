class Solution(object):
    def partitionDisjoint(self, A,n):
        N = n
        maxleft = [None] * N
        minright = [None] * N

        m = A[0]
        for i in range(N):
            m = max(m, A[i])
            maxleft[i] = m

        m = A[-1]
        for i in range(N-1, -1, -1):
            m = min(m, A[i])
            minright[i] = m

        for i in range(1, N):
            if maxleft[i-1] <= minright[i]:
                return i
val=Solution()
N=int(input())
a=list(map(int,input().split()))
print(val.partitionDisjoint(a,N))
