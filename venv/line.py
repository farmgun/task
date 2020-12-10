our_list = [1, 2,6, 7, 8, 9, 3, 4, 5,]
item=6

def LinerS(our_list, target_value):
    for item in our_list:
        if item == target_value:
            return True
    return False


def LinerS(our_list, target_value):
    for item in our_list:
        if item == target_value:
            return True
        elif item>target_value:
            return False
    return False


