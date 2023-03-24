import numpy as np
# Chooses a server to distribute the customer purely randomly


class PureRand:
    def __init__(self, arrival_times, service_times, m):
        self.arrival_times = arrival_times
        self.service_times = service_times
        self.m = m

    def run(self):
        #  Initialization
        arrival_times = self.arrival_times
        service_times = self.service_times
        m = self.m
        size = len(arrival_times)

        # Servers to be chosen
        selected = [np.random.randint(0, m) for i in range(size)]

        # Statistics to be collected
        wait_times = []
        departure_times = []
        queues = {i: [] for i in range(m)}

        for i in range(size):
            # Arrival time
            arrival_time = arrival_times[i]
            # Service time
            service_time = service_times[i]
            # Server chosen
            server = selected[i]
            # Queue to enter
            queue = queues[server]

            # Wait time
            if i == 0:
                wait_time = 0
            else:
                wait_time = max(0, departure_times[i - 1][server] - arrival_time)

            # Departure time
            departure_time = arrival_time + wait_time + service_time

            # Queue length
            if i == 0:
                queue_length = 0
            else:
                queue_length = queue_lengths[i - 1][server] + wait_time

            # Update statistics
            wait_times.append(wait_time)
            departure_times.append([departure_time] * m)
            queue_lengths.append([queue_length] * m)
 