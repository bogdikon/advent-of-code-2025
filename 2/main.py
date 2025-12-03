#!/bin/python3

with open("passwords_list.txt", "r") as f:
    content = f.read()


lines_content = content.split("\n")
del lines_content[-1] # removing empty string

class DialPoints(object):
    def __init__(self, pointer_position):
        self.pointer_position = pointer_position
        self.counter = 0

    def rotate_right(self, points_to_rotate):
        for i in range(points_to_rotate):
            self.pointer_position += 1
            if self.pointer_position == 100:
                self.pointer_position = 0
                self.counter += 1
        return self.pointer_position

    def rotate_left(self, points_to_rotate):
        for i in range(points_to_rotate):
            self.pointer_position -= 1
            if self.pointer_position == 0:
                self.counter +=1
            if self.pointer_position == -1:
                self.pointer_position = 99
        return self.pointer_position

    def get_current_pos(self):
        return self.pointer_position

    def get_counter(self):
        return self.counter

def parse_rotations():
    dial = DialPoints(50)
    for i in range(len(lines_content)):
        if lines_content[i].startswith("R"):
            dial.rotate_right(int(lines_content[i][1:]))
        elif lines_content[i].startswith("L"):
            dial.rotate_left(int(lines_content[i][1:]))
    return dial.get_counter()

print(parse_rotations())
