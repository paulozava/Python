# https://www.codewars.com/kata/the-lift/train/python



class Dinglemouse(object):

    def __init__(self, queues, capacity):
        self.queues = queues
        self.capacity = capacity
        self.capacity_used = 0
        self.actual_floor = 0
        self.build_floors = len(queues)
        self.motion = self.get_motion()
        self.buttons_pressed = self.get_calls(queues)
        self.stop_needs = {}

    def get_motion (self):
        if self.actual_floor < self.build_floors:
            return 'up'
        else:
            return 'down'

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
    
    def embarking (self, floor_orders):
        passagers = []
        while self.capacity > self.capacity_used:
            self.capacity_used += 1
            passager_order = floor_orders.pop()


    # g-0   1   2         3   4   5   6
    # ((), (), (5, 5, 5), (), (), (), ())
    def theLift(self):
        carregamento
        descarregamento
        reversao do movimento
        sem novos pedidos
        return []