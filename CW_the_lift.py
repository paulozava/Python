class Dinglemouse(object):

    def __init__(self, queues, capacity):
        self.queues = queues
        self.capacity = capacity
        self.build_floors = len(queues)

    def theLift(self):
        return []

# Lift Rules
# The Lift only goes up or down!
# Each floor has both UP and DOWN Lift-call buttons (except top and ground floors which have only DOWN and UP respectively)
# The Lift never changes direction until there are no more people wanting to get on/off in the direction it is already travelling
# When empty the Lift tries to be smart. For example,
# If it was going up then it may continue up to collect the highest floor person wanting to go down
# If it was going down then it may continue down to collect the lowest floor person wanting to go up
# The Lift has a maximum capacity of people
# When called, the Lift will stop at a floor even if it is full, although unless somebody gets off nobody else can get on!
# If the lift is empty, and no people are waiting, then it will return to the ground floor

# People Rules
# People are in "queues" that represent their order of arrival to wait for the Lift
# All people can press the UP/DOWN Lift-call buttons
# Only people going the same direction as the Lift may enter it, and they do so according to their "queue" order
# If a person is unable to enter a full Lift, they will press the UP/DOWN Lift-call button again after it has departed without them
