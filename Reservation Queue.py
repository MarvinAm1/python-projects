# Importing the queue and time methods
import queue
import time

# Initializing the ReservationQueue class
class ReservationQueue:
# Defining the attributes of the Queue Class
    def __init__(self):
        self.queue = queue.Queue()

# Initializing a method to push (add) items into the queue through the imported queue class
    def add_reservation(self, customer_name):
        self.queue.put(customer_name)

# Initializing a method to extract items from the queue
    def get_reservations(self):
        return self.queue.get()

# Initializing a method to check if the queue is empty
    def is_empty(self):
        return self.queue.empty()

# Initializing a method to check the size of the queue
    def queue_size(self):
        return self.queue.qsize()


# Initializing a class that creates agents which processes the customer reservations using the ReservationQueue class
class Agent(ReservationQueue):
    def __init__(self):
        super().__init__()
        self.queue = queue.Queue()

# Initializing a method that processes customer reservations through agents
    def process_reservation(self):
        while not self.queue.empty():
            reservation_queue = Agent.get_reservations(self)
            print(f"Processing reservation for {reservation_queue}...")
            print(f"Number of reservations left: {Agent.queue_size(self)} \n")
# Adding a time cooldown between each processed reservation
            time.sleep(1)
# Creating a while loop that checks whether the queue is empty and ends the initial while loop
        while Agent.queue_size(self) == 0:
            print(f"No more reservations left to process!")
            break


# Main() driver
# Creating an instance for the first Agent class
reservations1 = Agent()

# Assigning an Agent to a set of reservations
Agent1 = reservations1

# Adding reservations into the queue
reservations1.add_reservation("Mike")
reservations1.add_reservation("Bob")
reservations1.add_reservation("Cam")
reservations1.add_reservation("Kyle")

# Processing the reservations using the first Agent
Agent1.process_reservation()

# Creating a cooldown between the first Agent and the second Agent
time.sleep(3)
print("\nProcessing the next set of reservations... \n")
time.sleep(5)

# Creating an instance for the second Agent class
reservations2 = Agent()

# Assigning a second Agent to a different set of reservations
Agent2 = reservations2

# Adding reservations into the queue
reservations2.add_reservation("Miles")
reservations2.add_reservation("Angel")
reservations2.add_reservation("Mikey")
reservations2.add_reservation("Eugene")

# Processing the second set of reservations using the second Agent
reservations2.process_reservation()















