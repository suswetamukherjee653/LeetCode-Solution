class Solution(object):
    def sumAndMultiply(self, s, queries):
        MOD = 10**9 + 7
        n = len(s)

        pref_sum = [0] * (n + 1)
        pref_x = [0] * (n + 1)
        non_zero_count = [0] * (n + 1)
        
        for i in range(n):
            digit = int(s[i])
            pref_sum[i + 1] = (pref_sum[i] + digit) % MOD
            
            if digit != 0:
                pref_x[i + 1] = (pref_x[i] * 10 + digit) % MOD
                non_zero_count[i + 1] = non_zero_count[i] + 1
            else:
                pref_x[i + 1] = pref_x[i]
                non_zero_count[i + 1] = non_zero_count[i]

        pow10 = [1] * (n + 1)
        for i in range(1, n + 1):
            pow10[i] = (pow10[i - 1] * 10) % MOD
            
        ans = []

        for l, r in queries:
            current_sum = (pref_sum[r + 1] - pref_sum[l]) % MOD
            k = non_zero_count[r + 1] - non_zero_count[l]
            
            if k == 0:
                x = 0
            else:
                x = (pref_x[r + 1] - (pref_x[l] * pow10[k]) % MOD) % MOD
            
            current_ans = (x * current_sum) % MOD
            ans.append(current_ans)
            
        return ans