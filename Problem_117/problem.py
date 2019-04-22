'''
            -10
        10          -20 
    5       -5          -14

    This problem would just use a queue whose members are
    a tuple containing the node value and the level at which it is on.

    Each iteration we place the level at which the queues value was ripped
    and sum that value to a dict.

    Ex of default dict {
        1: -10
        2: -10
        3: -14
    }
    We then take the min of all the values using the level as our key. [min(dict, key=dict.get)]
    
'''