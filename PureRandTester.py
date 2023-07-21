from prettytable import PrettyTable
import numpy as np
import PureRand

class PureRand:
    def __init__(self, arrival_times, service_times, m):
        self.arrival_times = arrival_times
        self.service_times = service_times
        self.m = m

    def update_queues(self, queues, arrival_time, departure_times):
        max_queue = 0
        average_queue_len = 0
        for queue in queues.values():
            while len(queue) > 0 and arrival_time > departure_times[queue[0]]:
                queue.pop(0)
            max_queue = max(max_queue, len(queue))
            average_queue_len += len(queue)
        average_queue_len /= len(queues)
        return max_queue, average_queue_len

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
        system_times = []
        departure_times = []
        max_len = 0
        average_len = 0
        # List of customers stored for each server
        queues = {i: [] for i in range(m)}

        for i in range(size):
            arrival_time = arrival_times[i]
            service_time = service_times[i]
            server = selected[i]
            queue = queues[server]
            max_temp, average_temp = self.update_queues(queues, arrival_time, departure_times)
            max_len = max(max_len, max_temp)
            average_len += average_temp

            if i == 0 or len(queue) == 0:
                wait_time = 0
            else:
                prev = queue[-1]
                wait_time = max(0, departure_times[prev] - arrival_time)

            departure_time = arrival_time + wait_time + service_time
            system_time = departure_time - arrival_time

            # Update statistics
            wait_times.append(wait_time)
            departure_times.append(departure_time)
            system_times.append(system_time)
            queues[server].append(i)
        average_len /= size
        return wait_times, system_times, departure_times, selected, max_len, average_len


service_times = [1, 2, 1, 2, 5, 11, 1, 1, 22, 1]
arrival_times = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
m = 2
x = PrettyTable()
rand_min = PureRand.PureRand(arrival_times, service_times, m)
customer_nums = [i+1 for i in range(len(service_times))]
wait_times, system_times, departure_times, selected, max_len, average_len = rand_min.run()
selected_q = [i+1 for i in selected]
column_names = ["Customer #", "Selected Queue","Arrival Time", "Departure Time", "Service Time", "Wait Time", "System Time"]
data = [customer_nums, selected_q, arrival_times, departure_times, service_times, wait_times, system_times]
length = len(column_names)


for i in range(length):
     x.add_column(column_names[i],data[i])

print(x)
