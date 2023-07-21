import numpy as np
import math
import RandMin
import RoundRobin
import PureRand
from prettytable import PrettyTable

# Parameters for different test cases
m = 5  # number of servers available
d = 2  # number of servers randomly selected
mu = 0.2  # servers’ service time follows exponential distribution of rate parameter mu
lam = 20  # the customer arrivals follow the Poisson arrival process with mean arrival rate lambda

customers = 10000  # number of customers
seeds = [10, 20, 30, 40, 50, 60, 700, 800, 999, 5000]
RM_max_queue = []
RM_avg_queue = []
RM_avg_service = []

RR_max_queue = []
RR_avg_queue = []
RR_avg_service = []

PR_max_queue = []
PR_avg_queue = []
PR_avg_service = []

for seed in seeds:
    #  Initialization
    np.random.seed(seed)
    interarrival_times = [round(time*60) for time in np.random.exponential(scale=1/lam, size=customers)]
    arrival_times = np.cumsum(interarrival_times)
    service_times = [round(time*60) for time in np.random.exponential(scale=mu, size=customers)]

    rand_min = RandMin.RandMin(arrival_times, service_times, m, d, seed)
    pure_rand = PureRand.PureRand(arrival_times, service_times, m, seed)
    round_robin = RoundRobin.RoundRobin(arrival_times, service_times, m)

    wait_times, system_times, departure_times, selected, max_len, average_len = rand_min.run()
    average_system_len = (sum(system_times)/len(system_times))
    RM_max_queue.append(max_len)
    RM_avg_queue.append(average_len)
    RM_avg_service.append(average_system_len)

    wait_times, system_times, departure_times, selected, max_len, average_len = pure_rand.run()
    average_system_len = (sum(system_times)/len(system_times))
    PR_max_queue.append(max_len)
    PR_avg_queue.append(average_len)
    PR_avg_service.append(average_system_len)

    wait_times, system_times, departure_times, selected, max_len, average_len = round_robin.run()
    average_system_len = (sum(system_times)/len(system_times))
    RR_max_queue.append(max_len)
    RR_avg_queue.append(average_len)
    RR_avg_service.append(average_system_len)

print("RM:")
x = PrettyTable()
x.add_column("Seed", seeds)
x.add_column("Max Queue Length", RM_max_queue)
x.add_column("Average Queue Length", RM_avg_queue)
x.add_column("Average Service Time", RM_avg_service)
print(x)

print("RR:")
x = PrettyTable()
x.add_column("Seed", seeds)
x.add_column("Max Queue Length", RR_max_queue)
x.add_column("Average Queue Length", RR_avg_queue)
x.add_column("Average Service Time", RR_avg_service)
print(x)

print("PR:")
x = PrettyTable()
x.add_column("Seed", seeds)
x.add_column("Max Queue Length", PR_max_queue)
x.add_column("Average Queue Length", PR_avg_queue)
x.add_column("Average Service Time", PR_avg_service)
print(x)
