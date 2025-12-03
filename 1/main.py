#!/bin/python3

with open("passwords_list.txt", "r") as f:
    content = f.read()

lines_content = content.split("\n")
del lines_content[-1] # removing empty string

class DialPoints(object):
    def __init__(self, points):
        self.points = points
        self.points_list = []
        self.pointer_position = 50 # fuck me
        for i in range(0, points+1): # 0 to 99
            self.points_list.append(i)

    def rotate_right(self, points_to_rotate):
        # checking if pointer position is more than 99
        new_pointpos = self.pointer_position+points_to_rotate
        while new_pointpos > 99:
            new_pointpos -= 100 # no clue maybe its not the right way to do this
        self.pointer_position = new_pointpos
        return (self.pointer_position, self.points_list[self.pointer_position])

    def rotate_left(self, points_to_rotate):
        # checking if pointer position is less than 0
        new_pointpos = self.pointer_position-points_to_rotate
        while new_pointpos < 0:
            new_pointpos += 100 # i guess here i should add 99??
        self.pointer_position = new_pointpos
        return (self.pointer_position, self.points_list[self.pointer_position])

    def get_current_pos(self):
        return self.pointer_position

    def get_current_number(self):
        return self.points_list[self.pointer_position]

def parse_rotations():
    dial = DialPoints(99)
    _counter = 0
    for i in range(len(lines_content)):
        if lines_content[i].startswith("R"):
            dial.rotate_right(int(lines_content[i][1:]))
            if dial.get_current_number() == 0:
                _counter+=1
        elif lines_content[i].startswith("L"):
            dial.rotate_left(int(lines_content[i][1:]))
            if dial.get_current_number() == 0:
                _counter+=1

    return _counter
    

print(parse_rotations())
