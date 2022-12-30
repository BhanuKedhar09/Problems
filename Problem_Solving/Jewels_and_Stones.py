#https://leetcode.com/problems/jewels-and-stones/description/
class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        # stones = "".join(set(stones))
        count =0
        for stone in stones:
            if stone in jewels:
                count = count+1
            else:
                pass
        print(stones)
        return count
