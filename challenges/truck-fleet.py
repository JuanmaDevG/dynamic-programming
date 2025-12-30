#import numba
import numpy as np
from typing import Dict

from copy import copy

from typing import List, Tuple


"""
    This is essentially the backpack problem but modified.

    Having a fleet of trucks, each one can afford to carry a maximum of 700 tons of goods
    that weight w1, w2, w3, ..., wn. Each of them less than 700 tons. We want to know
    how many trucks we need as minimum to transport the N goods. The goods cannot be
    fragmented.
"""


class P010:
    def __init__(self):
        self.T = 700
        self.W: np.ndarray = None
        self.A: Dict[tuple[int, int], int] = None


    def init(self, data: str):
        self.T: int = 700
        self.W: np.ndarray = np.array([ int(i) for i in data.split() ])
        self.A: Dict[tuple[int,int, int], int] = {}


    def pdr(self, t: int, w: np.ndarray) -> int:
        if len(w) == 0:
            return 1 if t < 700 else 0

        n_trucks = np.inf
        for idx, cur_w in enumerate(w):
            subarray = np.delete(w, idx)
            new_t = t - cur_w
            if new_t == 0:
                n_trucks = min(n_trucks, 1 + self.pdr(700, subarray))
            elif new_t < 0:
                n_trucks = min(n_trucks, 1 + self.pdr(700 - cur_w, subarray))
            else:
                n_trucks = min(n_trucks, self.pdr(new_t, subarray))

        return n_trucks


    def pdr_a_not_optimized(self, t: int, w: np.ndarray):
        if len(w) == 0:
            return 1 if t < 700 else 0

        state_key = (t, len(w), w.sum())
        if state_key in self.A:
            return self.A[state_key]

        n_trucks = np.inf
        for idx, cur_w in enumerate(w):
            subarray = np.delete(w, idx)
            new_t = t - cur_w
            if new_t == 0:
                n_trucks = min(n_trucks, 1 + self.pdr_a(700, subarray))
            elif new_t < 0:
                n_trucks = min(n_trucks, 1 + self.pdr_a(700 - cur_w, subarray))
            else:
                n_trucks = min(n_trucks, self.pdr_a(new_t, subarray))

        self.A[state_key] = n_trucks
        return n_trucks


    def pdr_a(self, t: int, w: np.ndarray) -> int:
        if len(w) == 0:
            return 1 if t < 700 else 0

        state_key = (t, len(w), w.sum())
        if state_key in self.A:
            return self.A[state_key]

        n_trucks = np.inf
        for idx, cur_w in enumerate(w):
            swapper = w[idx]
            w[idx] = w[0]
            new_t = t - cur_w
            if new_t == 0:
                n_trucks = min(n_trucks, 1 + self.pdr_a(700, w[1:]))
            elif new_t < 0:
                n_trucks = min(n_trucks, 1 + self.pdr_a(700 - cur_w, w[1:]))
            else:
                n_trucks = min(n_trucks, self.pdr_a(new_t, w[1:]))
            w[idx] = swapper

        self.A[state_key] = n_trucks
        return n_trucks


    def pdi(self, t: int, w: np.ndarray) -> int:
        #WARNING: THI DOES NOT WORK
        if not w: return 0
        from typing import annotations
        INT_INF = np.iinfo(np.int64).max

        class Frame:
            def __init__(self, t: int, w: np.ndarray, best: int = INT_INF, next_frame: Frame = None, prev_frame: Frame = None):
                self.idx = 0
                self.t = t
                self.w = w
                self.state_key = (t, len(w), w.sum())
                self.best = best
                self.next = next_f
                self.prev = prev_f

            def replace(self, t: int, w: np.ndarray, best: int = INT_INF):
                self.__init__(t, w, best, self.next, self.prev)

        base_frame = Frame(t, w)
        f = base_frame
        for i in range(1, len(w)):
            f.next = Frame(t, w[1:], prev_frame = f)
            f = f.next

        #TODO: rest of the code with a linked list (I'm tired, better later


    def best(self, data: str) -> int:
        self.init(data)
        #return self.pdr(self.T, self.W)
        return self.pdr_a(self.T, self.W)
        #return self.pdi(self.T, self.W)


    def pdr_a_vec(self, t: int, w: np.ndarray) -> int:
        if len(w) == 0:
            return 1 if t < 700 else 0

        state_key = (t, len(w), w.sum())
        if state_key in self.A:
            return self.A[state_key]

        n_trucks = np.inf
        for idx, cur_w in enumerate(w):
            swapper = w[idx]
            w[idx] = w[0]
            new_t = t - cur_w
            params = (#TODO: set params inside the if and exec function and then compare results and assign truck number with index
            if new_t == 0:
                n_trucks = min(n_trucks, 1 + self.pdr_a(700, w[1:]))
            elif new_t < 0:
                n_trucks = min(n_trucks, 1 + self.pdr_a(700 - cur_w, w[1:]))
            else:
                n_trucks = min(n_trucks, self.pdr_a(new_t, w[1:]))
            w[idx] = swapper

        self.A[state_key] = n_trucks
        return n_trucks


    def best_solution(data: str) -> List[int]:
        self.init(data)
        self.assigned_truck = [0 for _ in self.W]
        pdr_a_vec(self.T, self.W)


if __name__ == "__main__":
    p = P010()
    data = "300 300 340 360 700 600 500 400 300 200 100 50 450 340 230 120"
    print(p.best(data))
