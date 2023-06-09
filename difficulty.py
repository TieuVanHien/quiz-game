class Dif:
    def __init__(self, dif):
        difficulties = ["Easy", "Hard", "Medium"]
        lowercase_difficulty = [difficulty.lower() for difficulty in difficulties]
        lowercase_dif = dif.lower()
        if lowercase_dif in lowercase_difficulty:
            self.dif = lowercase_dif
        else:
            raise ValueError("Invalid difficulty. Please choose a different difficulty by easy, medium and hard")