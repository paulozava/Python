# https://www.codewars.com/kata/the-lift/train/python


class Dinglemouse(object):

    def __init__(self, queues, capacity):
        self.queues = list(map(list, queues))
        self.capacity = capacity
        self.capacity_used = 0
        self.actual_floor = 0
        self.build_floors = len(queues)
        self.motion = self.get_motion()
        self.buttons_pressed = self.get_calls(queues)
        self.stop_needs = {floor: 0 for floor, queue in enumerate(queues)}
        self.floors_visited = []
        self.up_or_down = ['up', 'down']

    def get_motion (self, acending=True):
        if acending:
            if self.actual_floor >= self.build_floors:
                self.up_or_down.reverse()
        else:
            if self.actual_floor <= self.build_floors:
                self.up_or_down.reverse()
        return self.up_or_down[0]

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
        return buttons_pressed

    def rage_button_click (self):
        self.buttons_pressed[self.actual_floor] = {'up': True, 'down': True}
    
    def embarking (self, floor_orders):
        filter_possibilities = {'up': lambda x: x > self.actual_floor,
                                'down': lambda x: x < self.actual_floor}
        possible_orders = list(filter(filter_possibilities[self.motion], floor_orders))
        self.floors_visited.append(self.actual_floor)
        while self.capacity > self.capacity_used:
            if possible_orders:
                self.capacity_used += 1
                passager_order = possible_orders.pop()
                self.stop_needs[passager_order] += 1
                floor_orders.remove(passager_order)
            else: break
        return floor_orders

    def debarking (self):
        self.floors_visited.append(self.actual_floor)
        debarking_passangers = self.stop_needs[self.actual_floor]
        self.capacity_used -= debarking_passangers
        self.stop_needs[self.actual_floor] = 0

    # g-0   1   2         3   4   5   6
    # ((), (), (5, 5, 5), (), (), (), ())
    def theLift(self):
        carregamento
        descarregamento
        reversao do movimento
        sem novos pedidos

        return []