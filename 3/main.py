#!/bin/python3

with open("ids_list.txt", "r") as f:
    ids_content = f.read()

ranges_list = ids_content.split(',')
ranges_list[-1] = ranges_list[-1][:-1] # removing \n in the end of the last id range

def is_even(num: int):
    if num%2==0:
        return True
    else:
        return False

class Id(object):
    def __init__(self, value):
        self.value = value
    
    def is_valid(self):
        # Checking id value
        # if it starts with zero its invalid
        if self.value.startswith("0"):
            return False
        # if it contains doubled pattern its invalid
        # doubled pattern means they are always even?
        if is_even(len(self.value)): # checking if its even
            # trying to find a pattern
            # if its doubled then left part equals to left part??
            left_part = self.value[:int(len(self.value)/2)]
            right_part = self.value[int(len(self.value)/2):]
            if left_part == right_part:
                return False
            else:
                return True
        else:
            return True

    def get_value(self):
        return self.value

invalid_ids = []

for i in range(len(ranges_list)):
    list_in_range = []
    rangemin=ranges_list[i].split('-')[0] # first number in range
    rangemax=ranges_list[i].split('-')[1] # second number in range
    for i in range(int(rangemin), int(rangemax)+1):
        list_in_range.append(str(i))
        id_instance = Id(str(i))
        if id_instance.is_valid() == False:
            invalid_ids.append(id_instance.get_value())

accum = 0
for i in range(len(invalid_ids)):
    accum += int(invalid_ids[i])
print(accum)
