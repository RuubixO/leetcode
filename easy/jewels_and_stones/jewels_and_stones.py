def num_jewels_in_stones(self, J, S):
        jewel_count = 0
        for stone in S:
            if S in J:
                jewel_count + 1
            return (jewel_count)
