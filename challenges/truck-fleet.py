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
        from dataclasses import dataclass
        INT_INF = np.iinfo(np.int64).max

        @dataclass
        class Frame:
            idx: int #TODO: to avoid developing the full stack tree
            t: int
            w: np.ndarray
            state_key: Tuple[int, int, int]
            best: int

        base_state_key = (t, len(w), w.sum())
        state_stack = [Frame(0, t, w, base_state_key, INT_INF)]
        while state_stack:
            cur_state = state_stack.w[-1]
            if len(cur_state.w) == 0:
                state_stack.pop()
                self.A[cur_state.state_key] = 1 if t < 700 else 0
                continue

            if cur_state.idx < len(cur_state.w):
                cur_state.w[0], cur_state.w[cur_state.idx] = cur_state.w[cur_state.idx], cur_state.w[0]
                f = Frame(0, t - cur_state.w[idx], w[1:], (t, len(w[1:]), w[1:].sum()), INT_INF)
                #TODO: a full stack of frames with the length of this
            else:
                state_stack.pop()
                self.A[cur_state.state_key] = cur_state.best

        return self.A[base_state_key]


    def best(self, data: str) -> int:
        self.init(data)
        #return self.pdr(self.T, self.W)
        return self.pdr_a(self.T, self.W)
        #return self.pdi(self.T, self.W)


if __name__ == "__main__":
    p = P010()
    data = "300 300 340 360 700 600 500 400 300 200 100 50 450 340 230 120"
    print(p.best(data))
