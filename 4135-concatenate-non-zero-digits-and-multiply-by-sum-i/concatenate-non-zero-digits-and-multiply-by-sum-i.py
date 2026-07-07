class Solution(object):
    def sumAndMultiply(self, n):
        s=str(n)
        m=len(s)

        x=""
        sum=0
        for i in range(0,m):
            if s[i]=='0':
                pass
            else:
                x=x+s[i]
                sum=sum+int(s[i])

        if x=="":
            return 0
        else:
            xx=int(x)
            return xx*sum


