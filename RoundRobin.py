class RoundRobin:
    def __init__(self, arrival_times, service_times, m):
        self.arrival_times = arrival_times
        self.service_times = service_times
        self.m = m
