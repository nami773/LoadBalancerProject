import numpy as np
import math
import RandMin
import RoundRobin
import PureRand

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

    # print("arrival times: ", arrival_times)
    # print("Interarrival times: ", sum(interarrival_times)/len(interarrival_times))
    # print("service times:", service_times)
    # print("Service times: ", sum(service_times)/len(service_times))

    rand_min = RandMin.RandMin(arrival_times, service_times, m, d, seed)
    pure_rand = PureRand.PureRand(arrival_times, service_times, m, seed)
    round_robin = RoundRobin.RoundRobin(arrival_times, service_times, m)

    # result = {'arrival_times': arrival_times, 'service_times': service_times, 'wait_times': wait_times, 'system_times': system_times, 'departure_times': departure_times}
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
print("max queue: ")
for i in RM_max_queue:
    print(i)
print("avg queue: ")
for i in RM_avg_queue:
    print(i)
print("avg service: ")
for i in RM_avg_service:
    print(i)
print("++++++++++++++++++++++")
print("RR:")
print("max queue: ")
for i in RR_max_queue:
    print(i)
print("avg queue: ")
for i in RR_avg_queue:
    print(i)
print("avg service: ")
for i in RR_avg_service:
    print(i)
print("++++++++++++++++++++++")
print("PR:")
print("max queue: ")
for i in PR_max_queue:
    print(i)
print("avg queue: ")
for i in PR_avg_queue:
    print(i)
print("avg service: ")
for i in PR_avg_service:
    print(i)
