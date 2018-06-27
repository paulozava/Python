# https://www.codewars.com/kata/the-lift/train/python



class Dinglemouse(object):

    def __init__(self, queues, capacity):
        self.queues = queues
        self.capacity = capacity
        self.build_floors = len(queues)
        self.actual_floor = 0
        self.motion = 'up'
        self.buttons_pressed = self.get_calls(queues)


    def get_calls (self, queues):
        buttons_pressed = {}
        for floor, queue in enumerate(queues):
            floor_button = {'up': False, 'down': False}
            for call in queue:
                if call > floor:
                    floor_button['up'] = True
                else:
                    floor_button['down'] = True
            buttons_pressed.update({floor : floor_button})
        return buttons_pressed

    # g-0   1   2         3   4   5   6
    # ((), (), (5, 5, 5), (), (), (), ())
    def theLift(self):
        checagem de pedidos
        movimento
        carregamento
        descarregamento
        reversao do movimento
        sem novos pedidos
        return []