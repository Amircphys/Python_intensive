from typing import List, Union, Iterable
num_type = Union[int, float]


def merge(lst_1: Iterable[num_type], lst_2: Iterable[num_type])-> List[num_type]:
    ans = []
    if not (lst_1 and lst_2):
        return ans
    idx_1 = 0
    idx_2 = 0
    while idx_1 < len(lst_1) and idx_2 < len(lst_2):
        item_1 = lst_1[idx_1]
        item_2 = lst_2[idx_2]
        if item_1 == item_2:
            if item_1 not in ans:
                ans.append(item_1)
            idx_1 += 1
            idx_2 += 1
        elif item_1 < item_2:
            idx_1 += 1
        else:
            idx_2 += 1
    return ans 

 
def test_merge():
    params = [
        ([], (), []),
        ([1, 1, 2], (1, 1, 2), [1, 2]),
        ([1, 1, 2, 3], (1, 1, 2), [1, 2]),
        ([1, 1, 2], (1, 1, 2, 5), [1, 2]),
        ([1, 1, 2, 5, 7], (1, 1, 2, 3, 4, 7), [1, 2, 7]),
        ([1, 1, 2], (11, 11, 12, 15), []),
        ([1, 1, 2], (), []),
        ([-1, -1, 0, 2], (1, 2, 5, 15), [2]),
        ([-10, -9, 0, 1], (1, 2, 5, 15), [1]),
    ]
    for param in params:
        inp_1, inp_2, expected_out = param
        real_out = merge(inp_1, inp_2)
        assert real_out == expected_out, f"expected_output is: {expected_out}, real_out: {real_out}"
        
        

if __name__ == "__main__":
    test_merge()