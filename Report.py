import numpy as np

# Parameters for different test cases
m = 20  # number of servers available
d = 10  # number of servers randomly selected

mu = 0.5  # servers’ service time follows exponential distribution of rate parameter mu
lam = 10  # the customer arrivals follow the Poisson arrival process with mean arrival rate lambda

runs = 1000  # number of runs

#  Initialization
interarrival_times = np.random.exponential(scale=1/lam, size=runs)
arrival_times = np.cumsum(interarrival_times)

service_times = [time*60 for time in np.random.exponential(scale=mu, size=runs)]
# print("Interarrival times: ", interarrival_times)
print(service_times)
print("Service times: ", sum(service_times)/len(service_times))
