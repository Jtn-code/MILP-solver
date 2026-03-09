import random
from data.job_data import processing_time, jobs

random_order = jobs.copy()
random.shuffle(random_order)

time = 0
schedule = {}

for j in random_order:
    schedule[j] = time
    time += processing_time[j]

print("Random Order:", random_order)
print("Makespan:", time)
