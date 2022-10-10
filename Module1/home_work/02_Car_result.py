class Car:
    def __init__(self, gas, capacity, gas_per_km, dist):
        self.gas = gas
        self.capacity = capacity
        self.gas_per_km = gas_per_km
        self.__dist = dist

    def fill(self, fill_gas):
        total_gas = self.gas + fill_gas
        if total_gas <= self.capacity:
            self.gas = total_gas
        else:
            self.gas = self.capacity
            print(total_gas - self.capacity, 'лишних л.')

    def ride(self, km_to_ride):
        gas_to_ride = km_to_ride * self.gas_per_km
        if gas_to_ride <= self.gas:
            self.gas -= gas_to_ride
        else:
            km_to_ride = self.gas / self.gas_per_km
            self.gas = 0
        self.__dist += km_to_ride
        print(f'Проехали {km_to_ride} километров')


car1 = Car(0, 10, 1, 0)
car1.fill(16)
car1.ride(50)
