from typing import List, Union
num_type = Union[int, float]

def get_closest_to_zero(lst: List[num_type])-> List[num_type]:
    min_distance = float('inf')
    for num in lst:
        if abs(num) < min_distance:
            min_distance = abs(num)
    ans = []
    for num in lst:
        if abs(num) == min_distance:
            ans.append(num)
    return ans


if __name__ == "__main__":
    assert get_closest_to_zero([]) == []
    assert get_closest_to_zero([-1, 0, 1]) == [0]
    assert get_closest_to_zero([-1, -1, 1]) == [-1, -1, 1]
    assert get_closest_to_zero([-1, -1, 1, 2, 3, 4]) == [-1, -1, 1]
    assert get_closest_to_zero([-16, -15, 10, 20, 3, 64]) == [3]
    assert get_closest_to_zero([-16, -15, -3, 10, 20, 3, 64, 3]) == [-3, 3, 3]