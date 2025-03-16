import math
from typing import Optional, Tuple

def solve_bilinear_eq(a: float, b: float, c: float)-> Optional[Tuple[float, float]]:
    if a == 0:
        if b == 0:
            return 
        return (-c/b,)
    elif b == 0:
        ans = -c/a
        if ans < 0:
            return 
        return (-math.sqrt(ans), math.sqrt(ans))
    else:
        D = b**2 - 4*a*c
        if D<0:
            return
        ans_1 = (-b - math.sqrt(D))/(2*a)
        ans_2 = (-b + math.sqrt(D))/(2*a)
        if ans_1 > ans_2:
            return (ans_2, ans_1)
        return (ans_1, ans_2)
    
    
if __name__ == "__main__":
    assert solve_bilinear_eq(1, -4, 4) == (2, 2)
    assert solve_bilinear_eq(1, 0, 4) == None
    assert solve_bilinear_eq(1, 8, 7) == (-7, -1)
    assert solve_bilinear_eq(1, -3, -28) == (-4, 7)
    assert solve_bilinear_eq(1, -3, -28) == (-4, 7)
    assert solve_bilinear_eq(0, 2, 4) == (-2,)
    assert solve_bilinear_eq(0, 0, 4) == None
    assert solve_bilinear_eq(0, 0, 0) == None
    assert solve_bilinear_eq(1, 0, 4) == None
    assert solve_bilinear_eq(1, 0, -4) == (-2, 2)