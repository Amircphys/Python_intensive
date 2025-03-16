from typing import List, Tuple, Union
num_type = Union[int, float]

def nums_split(lst: List[num_type])-> List[Tuple[num_type]]:
    odd_nums = []
    oddness_nums = []
    for item in lst:
        if item % 2 == 1:
            oddness_nums.append(item)
        else:
            odd_nums.append(item)
    return (odd_nums, oddness_nums)


if __name__ == "__main__":
    assert nums_split([1, 2, 3, 4]) == ([2, 4], [1, 3])
    assert nums_split([]) == ([], [])
    assert nums_split([1]) == ([], [1])
    assert nums_split([0]) == ([0], [])
    assert nums_split([-1, 0, 1]) == ([0], [-1, 1])