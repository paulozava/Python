# https://www.codewars.com/kata/the-lift/train/python


class Dinglemouse(object):

    def __init__(self, queues, capacity):
        # print('build = ' + str(queues))
        # print('capacity = ' + str(capacity))
        # print('expect = ')
        self.queues = list(map(list, map(reversed,queues)))
        self.capacity = capacity
        self.capacity_used = 0
        self.actual_floor = 0
        self.build_floors = len(queues) - 1
        self.buttons_pressed = None
        self.stop_needs = {floor: 0 for floor, queue in enumerate(queues)}
        self.floors_visited = [0]
        self.motion = 'up'
        self.up_or_down = ['up', 'down']
        self.descending = False

    def get_calls (self):
        buttons_pressed = {}
        for floor, queue in enumerate(self.queues):
            floor_button = {'up': False, 'down': False}
            for call in queue:
                if call > floor:
                    floor_button['up'] = True
                else:
                    floor_button['down'] = True
            buttons_pressed.update({floor : floor_button})
        self.buttons_pressed = buttons_pressed

    def rage_button_click (self):
        self.buttons_pressed[self.actual_floor] = {'up': True, 'down': True}
        self.buttons_pressed[0]['down'] = False
        self.buttons_pressed[self.build_floors]['up'] = False

    def invert_motion (self):
        self.up_or_down.reverse()
        self.motion = self.up_or_down[0]
        self.descending = not self.descending
        self.get_calls()

    def still_have_calls (self):
        for queue in self.queues:
            if queue:
                return True
        return False
    
    def embarking (self, floor_orders):
        filter_possibilities = {'up': lambda x: x > self.actual_floor,
                                'down': lambda x: x < self.actual_floor}
        possible_orders = list(filter(filter_possibilities[self.motion], floor_orders))
        if self.floors_visited[-1] != self.actual_floor:
            self.floors_visited.append(self.actual_floor)
        self.buttons_pressed[self.actual_floor][self.motion] = False
        while self.capacity_used < self.capacity:
            if possible_orders:
                self.capacity_used += 1
                passager_order = possible_orders.pop()
                self.stop_needs[passager_order] += 1
                floor_orders.remove(passager_order)
            else:
                break
        # print('embarking')
        # print('floor: ' + str(self.actual_floor))
        # print(self.capacity_used)
        # print(self.queues)
        # print('###########')
        return floor_orders

    def debarking (self):
        if self.floors_visited[-1] != self.actual_floor:
            self.floors_visited.append(self.actual_floor)
        debarking_passangers = self.stop_needs[self.actual_floor]
        self.capacity_used -= debarking_passangers
        self.stop_needs[self.actual_floor] = 0
        # print('debarking')
        # print('floor: ' + str(self.actual_floor))
        # print(self.capacity_used)
        # print(self.queues)
        # print('###########')

    def theLift(self):
        self.get_calls()
        while self.still_have_calls():
            floors_and_orders = sorted(enumerate(self.queues), reverse=self.descending)
            for floor, floor_orders in floors_and_orders:
                self.actual_floor = floor
                if self.stop_needs[floor] > 0:
                    self.debarking()
                if self.buttons_pressed[floor][self.motion]:
                    rest_of_orders = self.embarking(floor_orders)
                    self.queues[floor] = rest_of_orders
                    if rest_of_orders:
                        self.rage_button_click()
            self.invert_motion()
        if self.floors_visited[-1] != 0:
            self.floors_visited.append(0)
        return self.floors_visited