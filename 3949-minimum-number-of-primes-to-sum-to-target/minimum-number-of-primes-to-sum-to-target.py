class Solution:
    def minNumberOfPrimes(self, n: int, m: int) -> int:
        def first_m_primes(m):
            primes = []
            num = 2
            while len(primes) < m:
                is_prime = True
                for p in primes:
                    if p * p > num:
                        break
                    if num % p == 0:
                        is_prime = False
                        break
                if is_prime:
                    primes.append(num)
                num += 1
            return primes
        primes = first_m_primes(m)
        dp = [float('inf')]*(n+1)
        dp[0]= 0
        for prime in primes:
            for i in range(prime,n+1):
                if dp[i-prime]+1 < dp[i]:
                    dp[i] = dp[i-prime]+1
        return dp[n] if dp[n] != float('inf') else -1 