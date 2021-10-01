# Added my solution for this project.
import copy
import random
# Consider using the modules imported above.

class Hat:
    def __init__(self, **args):
        self.contents = []
        for ballColor, numberBalls in args.items():
            self.contents.extend([ballColor] * numberBalls)
        

    def draw(self, drawNumber):
        if drawNumber >= len(self.contents):
            return self.contents 
        else:
            drawnBalls = random.sample(self.contents, drawNumber)
            for item in drawnBalls:
                self.contents.remove(item)
            return drawnBalls
    


def experiment(hat, expected_balls, num_balls_drawn, num_experiments):
    counter = 0
    for item in range(num_experiments):
        randomBalls = hat.draw(num_balls_drawn)
        for ballColor, numberBalls in expected_balls.items():
            if randomBalls.count(ballColor) > numberBalls :
                counter = counter + 1
    
    return (counter / num_experiments)
