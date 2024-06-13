import random
from math import factorial

N_TRIALS = 1000000

ell = 4
L = 10

def all_overlapping(xL_arr):

    for idx, xLi in enumerate(xL_arr):
        for jdx, xLj in enumerate(xL_arr):
            if jdx <= idx:
                continue
            if abs(xLi-xLj) > ell:
                return 0

    return 1

for n_segments in range(2,20,1):

    outcomes = []
    for _ in range(N_TRIALS):
        xLs = [random.random()*(L-ell) for _ in range(n_segments)]
        outcome = all_overlapping(xLs)
        outcomes.append(outcome)

    prop = sum(outcomes) / len(outcomes)
    sigma = (prop * (1-prop) / N_TRIALS) ** 0.5

    rat = ell / (L-ell)
    triangular = n_segments * (n_segments - 1) / 2

    
    # https://en.wikipedia.org/wiki/Simplex#Volume
    # https://math.stackexchange.com/questions/1302005/finding-volume-of-an-n-dimensional-pyramid-numerically
    base_exp_1 = rat ** (n_segments-1) / (n_segments-1)
    base_exp_2 = rat ** n_segments / n_segments
    base_exp = base_exp_1 - base_exp_2

    # no idea where the 2 * triangular comes from, but it matches
    # with the n=2 calculation I did by hand
    # -- I think it might be from my overzealous requrement that
    # -- x1 < x2 < ... < xN (N! combination) when really all I needed
    # -- was x1 < xi < xj < ... < xN, i.e. the ordering of the (N-2)
    # -- middle elements ( [N-2]! combinations ) didn't matter.
    # -- So N!/(N-2)! = N(N-1) = 2*Tri(N)
    expected = 2 * triangular * base_exp
    
    print(f"{n_segments}: p = {prop:.4f} +- {sigma:.4f}. Expected {expected:.4f}")

