import random

class puzzel_details:
    def __init__(self, positions):
        self.positions = positions
        self.puzzel = [
            [0, 3, 4, 0],
            [4, 0, 0, 2],
            [1, 0, 0, 3],
            [0, 2, 1, 0]
        ]
        

    def get_random_puzzel(self):
        one = [
            [0, 3, 4, 0],
            [4, 0, 0, 2],
            [1, 0, 0, 3],
            [0, 2, 1, 0]
        ]

        two = [
            [0, 0, 4, 0],
            [4, 0, 3, 0],
            [0, 4, 0, 3],
            [0, 1, 0, 0]
        ]

        three = [
            [0, 0, 1, 0],
            [4, 0, 0, 0],
            [0, 0, 0, 2],
            [0, 3, 0, 0]
        ]
        
        self.all_puzzels = [one, two, three]

        puzzel = random.choice(self.all_puzzels)
        self.puzzel = puzzel
