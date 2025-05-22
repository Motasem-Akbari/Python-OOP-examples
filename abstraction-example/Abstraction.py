from abc import ABC, abstractmethod

# Abstract Base Class
class Transport(ABC):
    def __init__(self, name):
        self.name = name

    @abstractmethod
    def start_journey(self):
        pass

    @abstractmethod
    def end_journey(self):
        pass


# Subclasses with concrete implementations
class Bus(Transport):
    def start_journey(self):
        return f"{self.name} (Bus) is started."

    def end_journey(self):
        return f"{self.name} (Bus) is stopped."


class Train(Transport):
    def start_journey(self):
        return f"{self.name} (Train) is started."

    def end_journey(self):
        return f"{self.name} (Train) is stopped."


class Airport(Transport):
    def start_journey(self):
        return f"{self.name} (Airplane) is started."

    def end_journey(self):
        return f"{self.name} (Airplane) is stopped."


# List of transport identifiers
transport_names = [
    'B39', 'B25', 'T257', 'A995007', 'A7412335',
    'T741', 'B74', 'T789', 'A753951', 'B50'
]

# Creating instances based on prefix
vehicles = []
for name in transport_names:
    if name.startswith("B"):
        vehicles.append(Bus(name))
    elif name.startswith("T"):
        vehicles.append(Train(name))
    elif name.startswith("A"):
        vehicles.append(Airport(name))

# Starting journeys
print("---- Journey Started ----\n")
for vehicle in vehicles:
    print(vehicle.start_journey())

print("\n---- After Arrival ----\n")
for vehicle in vehicles:
    print(vehicle.end_journey())