class Solution:
    def climbStairs(self, n: int) -> int:
        one, two = 1, 1 
        nextvar = 1

        for i in range(n - 1):
            nextvar = one + two
            one = two
            two = nextvar
        
        return nextvar 