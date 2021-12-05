 def climbStairs(self, n: int) -> int:
        if n==0 | n==1:
            return n
        f = 1
        s = 1
        for i in range(2,n+1):
            t = f+s
            f=s
            s=t
        return s
            
