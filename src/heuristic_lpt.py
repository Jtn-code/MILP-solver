from data.job_data import processing_time, jobs

lpt_order = sorted(jobs, key=lambda x: processing_time[x], reverse=True)

time = 0
schedule = {}

for j in lpt_order:
    schedule[j] = time
    time += processing_time[j]

print("LPT Order:", lpt_order)
print("Makespan:", time)
