class P100:
    def __init__(self):
        pass


    def init(self):
        pass


    def pdr(self, s1, s2):
        def rec(i, j):
            if i == len(s1) and j == len(s2):
                return 0, ""
            if i == len(s1):
                ops = "".join(f"i{s2[k]}{s2[k]}" for k in range(j, len(s2)))
                return len(s2) - j, ops
            if j == len(s2):
                ops = "".join(f"b{s1[k]}" for k in range(i, len(s1)))
                return len(s1) - i, ops

            cost_sub = 0 if s1[i] == s2[j] else 1
            c1, op1 = rec(i + 1, j + 1)
            best = (cost_sub + c1, f"s{s1[i]}{s2[j]}" + op1)

            c2, op2 = rec(i, j + 1)
            if 1 + c2 < best[0]:
                best = (1 + c2, f"i{s2[j]}{s2[j]}" + op2)

            c3, op3 = rec(i + 1, j)
            if 1 + c3 < best[0]:
                best = (1 + c3, f"b{s1[i]}" + op3)

            if i + 1 < len(s1) and j + 1 < len(s2) and s1[i] == s2[j + 1] and s1[i + 1] == s2[j]:
                c4, op4 = rec(i + 2, j + 2)
                if 1 + c4 < best[0]:
                    best = (1 + c4, f"w{s1[i]}{s1[i+1]}{s2[j]}{s2[j+1]}" + op4)

            return best

        return rec(0, 0)


    def pdr_a(self, s1, s2):
        from functools import lru_cache

        @lru_cache(None)
        def rec(i, j):
            if i == len(s1) and j == len(s2):
                return 0, ""
            if i == len(s1):
                ops = "".join(f"i{s2[k]}{s2[k]}" for k in range(j, len(s2)))
                return len(s2) - j, ops
            if j == len(s2):
                ops = "".join(f"b{s1[k]}" for k in range(i, len(s1)))
                return len(s1) - i, ops

            cost_sub = 0 if s1[i] == s2[j] else 1
            c1, op1 = rec(i + 1, j + 1)
            best = (cost_sub + c1, f"s{s1[i]}{s2[j]}" + op1)

            c2, op2 = rec(i, j + 1)
            if 1 + c2 < best[0]:
                best = (1 + c2, f"i{s2[j]}{s2[j]}" + op2)

            c3, op3 = rec(i + 1, j)
            if 1 + c3 < best[0]:
                best = (1 + c3, f"b{s1[i]}" + op3)

            if i + 1 < len(s1) and j + 1 < len(s2) and s1[i] == s2[j + 1] and s1[i + 1] == s2[j]:
                c4, op4 = rec(i + 2, j + 2)
                if 1 + c4 < best[0]:
                    best = (1 + c4, f"w{s1[i]}{s1[i+1]}{s2[j]}{s2[j+1]}" + op4)

            return best

        return rec(0, 0)


    def pdi(self, s1, s2):
        n, m = len(s1), len(s2)
        dp = [[(0, "") for _ in range(m + 1)] for _ in range(n + 1)]

        for i in range(1, n + 1):
            dp[i][0] = (i, dp[i - 1][0][1] + f"b{s1[i-1]}")
        for j in range(1, m + 1):
            dp[0][j] = (j, dp[0][j - 1][1] + f"i{s2[j-1]}{s2[j-1]}")

        for i in range(1, n + 1):
            for j in range(1, m + 1):
                best = (float('inf'), "")

                cost_sub = 0 if s1[i - 1] == s2[j - 1] else 1
                c1, op1 = dp[i - 1][j - 1]
                best = (cost_sub + c1, op1 + f"s{s1[i-1]}{s2[j-1]}")

                c2, op2 = dp[i][j - 1]
                if 1 + c2 < best[0]:
                    best = (1 + c2, op2 + f"i{s2[j-1]}{s2[j-1]}")

                c3, op3 = dp[i - 1][j]
                if 1 + c3 < best[0]:
                    best = (1 + c3, op3 + f"b{s1[i-1]}")

                if i > 1 and j > 1 and s1[i - 2] == s2[j - 1] and s1[i - 1] == s2[j - 2]:
                    c4, op4 = dp[i - 2][j - 2]
                    if 1 + c4 < best[0]:
                        best = (1 + c4, op4 + f"w{s1[i-2]}{s1[i-1]}{s2[j-2]}{s2[j-1]}")

                dp[i][j] = best

        return dp[n][m]


    def best_solution(data: list[str]) -> str:
        pass #TODO: code


if __name__ == "__main__":
        s1, s2 = data
        cost, ops = self.edit_distance_iter(s1, s2)
