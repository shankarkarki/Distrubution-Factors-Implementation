import numpy as np

bus = [1.05, 1.00, 1.02]
numline = 3
frombus = [1, 1, 2]
tobus = [2, 3, 3]
xline = [0.1 + 0.2j, 0.2 + 0.4j, 0.15 + 0.3j]
BranchStatus = [1, 1, 1]
numbus = len(bus)
flow = np.zeros((numline, numbus), dtype=complex)

for iline in range(numline):
    if BranchStatus[iline] == 1:
        i = frombus[iline]
        j = tobus[iline]
        flow[iline, i] = 1 / xline[iline]
        # flow[iline, j] = -1 / xline[iline]

print(flow)


