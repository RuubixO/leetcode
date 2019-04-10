class Solution:

    def numJewelsInStones(self, J, S):
        jewel_count = 0
        for stone in S:
            if S in J:
                jewel_count + 1
            return (jewel_count)
