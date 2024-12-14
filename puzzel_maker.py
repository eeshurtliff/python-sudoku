import random

class Puzzel:
    def __init__(self, positions):
        self.positions = positions
        puzzel_index = self.get_rand_num(3)

        self.start_puzzel = self.get_puzzel(puzzel_index)
        self.answer = self.get_answer(puzzel_index)
        self.game_board = self.start_puzzel
        

    def get_rand_num(self, size):
        return random.randint(0,size-1)

    def get_puzzel(self, index):
        one = [
            0, 3, 4, 0,
            4, 0, 0, 2,
            1, 0, 0, 3,
            0, 2, 1, 0
        ]

        two = [
            0, 0, 4, 0,
            4, 0, 3, 0,
            0, 4, 0, 3,
            0, 1, 0, 0
        ]

        three = [
            0, 0, 1, 0,
            4, 0, 0, 0,
            0, 0, 0, 2,
            0, 3, 0, 0
        ]
        
        self.all_puzzels = [one, two, three]

        puzzel = self.all_puzzels[index]
        return puzzel
        

    def get_answer(self, index):
        one = [
            2, 3, 4, 1,
            4, 1, 3, 2,
            1, 4, 2, 3,
            3, 2, 1, 4
        ]

        two = [
            1, 3, 4, 2,
            4, 2, 3, 1,
            2, 4, 1, 3,
            3, 1, 2, 4
        ]

        three = [
            3, 2, 1, 4,
            4, 1, 2, 3,
            1, 4, 3, 2,
            2, 3, 4, 1         
        ]

        answers = [one, two, three]
        return answers[index]

    def check_spot_empty(self, x, y):
        selected = (x, y)
        spot_index = self.positions.index(selected)
        if self.game_board[spot_index] == 0:
            if spot_index == 0:
                return 17
            return spot_index
        elif self.game_board[spot_index] != self.answer[spot_index]:
            if spot_index == 0:
                return 17
            return spot_index
        else:
            print(self.start_puzzel[spot_index])
            return False
    
    def check_guess(self, guess, index):
        correct = self.answer[index]
        self.game_board[index] = guess
        if guess == correct:
            return True
        return False
    
    def check_solved(self):
        if self.game_board == self.answer:
            return True
        return False
