# Store moves in a stack
def str2stack(inString):
    # Moves are a csv string, separate by commas into an array
    move_list = inString.split(',')
    stack = []

    # Store in stack while removing whitespace
    for move in move_list:
        stack.append(move.strip()) 

    stack.reverse()
    return(stack)

def input(arr1,arr2,arr3):
    concatenated_str = ''.join(map(str, arr1 + arr2 + arr3))
    return(str2stack(concatenated_str))