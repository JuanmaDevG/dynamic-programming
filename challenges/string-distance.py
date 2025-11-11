# No he usado arrays de numpy ni numba de momento porque es solvente

class P100:
    def __init__(self):
        pass


    def pdr(self, s1, s2) -> str:
        def rec(i, j):
            if i == len(s1) and j == len(s2):
                return 0, ""
            if i == len(s1):
                ops = "".join(f"i{s2[k]}" for k in range(j, len(s2)))
                return len(s2) - j, ops
            if j == len(s2):
                ops = "".join(f"b{s1[k]}" for k in range(i, len(s1)))
                return len(s1) - i, ops

            cost_sub = 0 if s1[i] == s2[j] else 1
            c1, op1 = rec(i + 1, j + 1)
            best = (cost_sub + c1, f"s{s1[i]}{s2[j]}" + op1)

            c2, op2 = rec(i, j + 1)
            if 1 + c2 < best[0]:
                best = (1 + c2, f"i{s2[j]}" + op2)

            c3, op3 = rec(i + 1, j)
            if 1 + c3 < best[0]:
                best = (1 + c3, f"b{s1[i]}" + op3)

            if i + 1 < len(s1) and j + 1 < len(s2) and s1[i] == s2[j + 1] and s1[i + 1] == s2[j]:
                c4, op4 = rec(i + 2, j + 2)
                if 1 + c4 < best[0]:
                    best = (1 + c4, f"w{s1[i]}{s1[i+1]}{s2[j]}{s2[j+1]}" + op4)

            return best

        return rec(0, 0)[1]


    def pdr_a(self, s1, s2) -> str:
        from functools import lru_cache
        @lru_cache(None) # Profe, esto es para memorizar resultados de llamadas con los mismos parámetros (es otra forma de memorizar estado)
        def rec(i, j):
            if i == len(s1) and j == len(s2):
                return 0, ""
            if i == len(s1):
                ops = "".join(f"i{s2[k]}" for k in range(j, len(s2)))
                return len(s2) - j, ops
            if j == len(s2):
                ops = "".join(f"b{s1[k]}" for k in range(i, len(s1)))
                return len(s1) - i, ops

            cost_sub = 0 if s1[i] == s2[j] else 1
            c1, op1 = rec(i + 1, j + 1)
            best = (cost_sub + c1, f"s{s1[i]}{s2[j]}" + op1)

            c2, op2 = rec(i, j + 1)
            if 1 + c2 < best[0]:
                best = (1 + c2, f"i{s2[j]}" + op2)

            c3, op3 = rec(i + 1, j)
            if 1 + c3 < best[0]:
                best = (1 + c3, f"b{s1[i]}" + op3)

            if i + 1 < len(s1) and j + 1 < len(s2) and s1[i] == s2[j + 1] and s1[i + 1] == s2[j]:
                c4, op4 = rec(i + 2, j + 2)
                if 1 + c4 < best[0]:
                    best = (1 + c4, f"w{s1[i]}{s1[i+1]}{s2[j]}{s2[j+1]}" + op4)

            return best

        return rec(0, 0)[1]


    def pdi(self, s1, s2):
        n, m = len(s1), len(s2)
        self.A = [[(0, "") for _ in range(m + 1)] for _ in range(n + 1)]

        for i in range(1, n + 1):
            self.A[i][0] = (i, self.A[i - 1][0][1] + f"b{s1[i-1]}")
        for j in range(1, m + 1):
            self.A[0][j] = (j, self.A[0][j - 1][1] + f"i{s2[j-1]}")

        for i in range(1, n + 1):
            for j in range(1, m + 1):
                best = (float('inf'), "")

                cost_sub = 0 if s1[i - 1] == s2[j - 1] else 1
                c1, op1 = self.A[i - 1][j - 1]
                best = (cost_sub + c1, op1 + f"s{s1[i-1]}{s2[j-1]}")

                c2, op2 = self.A[i][j - 1]
                if 1 + c2 < best[0]:
                    best = (1 + c2, op2 + f"i{s2[j-1]}")

                c3, op3 = self.A[i - 1][j]
                if 1 + c3 < best[0]:
                    best = (1 + c3, op3 + f"b{s1[i-1]}")

                if i > 1 and j > 1 and s1[i - 2] == s2[j - 1] and s1[i - 1] == s2[j - 2]:
                    c4, op4 = self.A[i - 2][j - 2]
                    if 1 + c4 < best[0]:
                        best = (1 + c4, op4 + f"w{s1[i-2]}{s1[i-1]}{s2[j-2]}{s2[j-1]}")

                self.A[i][j] = best

        return self.A[n][m][1]


    def best_solution(self, data: list[str]) -> str:
        s1, s2 = data
        #return self.pdr(s1, s2)
        #return self.pdr_a(s1, s2)
        return self.pdi(s1, s2)


if __name__ == "__main__":
        strings = [
                ["3356711", "3365711"],
                ["121", "11"],
                ["11", "121"]]
        p = P100()

        for i, pack in enumerate(strings):
            print(f"Case {i}: {pack} = {p.best_solution(pack)}")
