import pulp
from data.job_data import processing_time, precedence, jobs

model = pulp.LpProblem("3D_Print_Scheduling", pulp.LpMinimize)

S = pulp.LpVariable.dicts("Start", jobs, lowBound=0)

y = pulp.LpVariable.dicts(
"Order",
[(i,k) for i in jobs for k in jobs if i < k],
cat='Binary'
)

Cmax = pulp.LpVariable("Cmax", lowBound=0)

model += Cmax

for i in jobs:
    model += Cmax >= S[i] + processing_time[i]

for i,j in precedence:
    model += S[j] >= S[i] + processing_time[i]

M = 24

for i in jobs:
    for k in jobs:
        if i < k:
            model += S[i] + processing_time[i] <= S[k] + M*(1 - y[(i,k)])
            model += S[k] + processing_time[k] <= S[i] + M*(y[(i,k)])

model.solve()

print("Status:", pulp.LpStatus[model.status])

for i in jobs:
    print(f"Job {i} start time:", S[i].value())

print("Execution Order:",
      [j for j,_ in sorted([(i,S[i].value()) for i in jobs], key=lambda x: x[1])])

print("Optimal Makespan:", Cmax.value())
