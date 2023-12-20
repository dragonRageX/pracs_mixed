neighbours_object = {
    "A": ["B", "C", "D"],
    "B": ["E", "F"],
    "C": ["G", "H"],
    "D": ["I"],
    "E": [],
    "F": [],
    "G": [],
    "H": [],
    "I": []
}

goal_node = "I"

queue = ["A"]

permitted_depth = 1
max_depth = 3   #maximum depth of the search tree

found = 0

def check_if_popped_element_exists_in_queue(popped_from_stack, queue):
    for i in range(len(queue)):
        if popped_from_stack == queue[i]:
            popped_from_queue = queue.pop(i)   #remove element from queue as well
            queue.extend(neighbours_object[popped_from_queue])   #append children/neighbours of the popped element to the end of the queue
            return True   #we return true if popped element from stack exists in queue
    return False

def push_neighbours_onto_stack(popped_from_stack, stack):
    if(neighbours_object[popped_from_stack] != None):
        stack.extend(neighbours_object[popped_from_stack])   #append children/neighbours of the popped element to the end of the stack

while permitted_depth <= max_depth:
    stack = ["A"]
    while len(stack) != 0:
        popped_from_stack = stack.pop()   #pop the top element from stack
        if popped_from_stack == goal_node:
            found = 1
            break
        else:
            if not(check_if_popped_element_exists_in_queue(popped_from_stack, queue)):   #this defines our level
                push_neighbours_onto_stack(popped_from_stack, stack)   #dfs
                
        print(f"Stack: {stack}")
        print(f"Queue: {queue}")
    
    permitted_depth += 1

if found == 1:
    print("Goal Node found!")
else:
    print("Goal Node not found!")