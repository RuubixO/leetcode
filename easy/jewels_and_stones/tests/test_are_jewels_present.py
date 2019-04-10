import pytest
import jewels_and_stones


def test_how_many_jewels_in_stones():
    J = "aA"
    S = "aAAbbbb"

    assert jewels_and_stones.num_jewels_in_stones(self, J, S) == 3
