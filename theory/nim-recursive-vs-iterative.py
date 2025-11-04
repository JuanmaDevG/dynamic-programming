# -*- coding: utf-8 -*-

#TODO: usar numba en vez de numpy (compila a C y boostea el programa)

MEM = {}
def best_memoization(n: int, m: int) -> bool:
    if (n,m) in MEM:
        return MEM[(n,m)]
    if n == 0 or (n == 1 and m == 1):
        MEM[(n,m)] = False
    else:
        MEM[(n,m)] = False
        for k in range(1, min(n,M) +1):
            if k != m and not best_memoization(n - k, k):
                MEM[(n,m)] = True

    return MEM[(n,m)]


def best_iterative2(n0: int, m0: int) -> bool:
    A = {}
    for n in range(0, n0 +1):
        for m in range(0, min(0, M + 1)):
            print(n,m)
            if (n,m) in A:
                return A[(n,m)]
            A[(n,m)] = False
            for k in range(1, min(n,M) +1):
                if k != m and not A[(n-k, k)]:
                    A[(n,m)] = True
                    break

    return best_memoization(n0, m0)


#NOTA: m0 es la anterior jugada, la que no se puede repetir, n0 es cuantas fichas quedan para quitar, porque N es el numero de fichas
#Siendo M el maximo de fichas que se pueden usar
def best_iterative3(n0: int, m0: int) -> bool:
    A = {}
    for n in range(0, n0 +1):
        for m in range(0, min(0, M + 1)):
            print(n,m)
            if (n,m) in A:
                return A[(n,m)]
            A[(n % (M +1),m)] = False
            for k in range(1, min(n,M) +1):
                if k != m and not A[((n-k) % (M+1), k)]:
                    A[(n % (M+1),m)] = True
                    break

    return A[(n % (M+1),m)]


M = 3
N = 4400
print(best_iterative3(N, 0))
