# %%

# Task: Given a string as our input, find the number of times we see a character that
#  we've already seen before.

def duplicateCharacters(input):
    # Change string input into list so we can loop through. 
    list_str = list(input)
    # Dictionary that will store the characters and their number of appearances. 
    character_dictionary = {} 
    # counts number of time we have a character that appears more than once. 
    duplicate_counter = 0
    for character in list_str:
        if character in character_dictionary.keys():
            occurences_of_char = character_dictionary[character]
            character_dictionary[character] += 1 
            occurences_of_char += 1  
            if occurences_of_char == 2:
                duplicate_counter += 1 
            else:
                continue 
        else:
            character_dictionary[character] = 1
    print(character_dictionary)
    return duplicate_counter

print(duplicateCharacters('aaaasthreghionhgfe56666'))
# %%

# Task: Given a string of characters, find the second highest digit that occurs, 
# if less than 2 digits then return -1. 
def secondHighestDigit(input):
    # create a list of the characters in the string. 
    list_str = list(input) 
    # A list to store the digits in our string. 
    list_of_digits = [] 
    for character in input: 
        # Try cast the character in our string to an integer. (checks if digit or not)
        try: 
            digit = int(character)
            list_of_digits.append(digit)
        # if not a digit, i.e is a string, then move to next character in string.
        except: 
            continue
    # Provided we have atleast 2 digits we can pick the second biggest number. 
    if len(list_of_digits) >= 2:
        list_of_digits.sort(reverse=True) 
        return list_of_digits[1]
    # Exceptions for no digits or one digit. 
    else:
        return -1 

print(secondHighestDigit('dd5gkd45fsgv9cdfnj2'))
# %%
# Task: Suppose there is a robot who starts by facing north, we are given a string of characters
# that represent the movements of this robot. We should only count for F,L,R in this string and 
# other characters discarded. F = Forward, L = Turn Left, R = Turn right. Return the integer value
# that denotes the number of moves the robot has to take to get back to it's starting position. 

def flr(directions):
    # Lets first start by extracting the instructions for the robot. 
    instructions = []
    allowed_instructions = ['F', 'L', 'R']
    for char in directions:
        if char in allowed_instructions:
            instructions.append(char)
    
    # Now we need a way to interpret the instructions provided and determine the end point, 
    # Then we know the quickest way back to origin (0,0) from (X,Y) is to traverse the             # triangle formed by (X,Y), (X,0) (0,0) OR (X,Y), (0,Y) (0,0) the choice of triangle is        #  determine by the direction the robot is facing. 
    
    left_dict = {'N': 'W', 'W' : 'S', 'S' : 'E', 'E' : 'N'}
    right_dict = {'N' : 'E', 'E' : 'S', 'S' : 'W', 'W' : 'N'}
    
    # Initial Position
    position = [[0,0], 'N']
    
    for direction in instructions:
        if direction == 'L':
            position[1] = left_dict[position[1]]
        elif direction == 'R':
            position[1] = right_dict[position[1]]
        else:
            if position[1] == 'N':
                position[0][1] += 1 
            elif position[1] == 'E':
                position[0][0] += 1 
            elif position[1] == 'S':
                position[0][1] -= 1 
            else:
                position[0][0] -= 1  
        print(position[1])
    print(position)
    # Now we know the final position of the robot afer the directions. 
    x = position[0][0]
    y = position[0][1]
    direction = position[1]
    if x > 0 and y > 0:
        if direction == 'W' or direction == 'S':
            return abs(x) + abs(y) + 1
        else:
            return x+y+2 
    elif x < 0 and y < 0:
        if direction == 'N' or direction == 'E':
            return abs(x) + abs(y) + 1 
        else:
            return abs(x) + abs(y) + 2
    elif x > 0 and y < 0:
        if direction == 'N' or direction == 'W':
            return abs(x) + abs(y) + 1
        else:
            return abs(x) + abs(y) + 2 
    elif x < 0 and y > 0:
        if direction == 'E' or direction == 'S':
            return abs(x) + abs(y) + 1
        else:
            return abs(x) + abs(y) + 2
    elif x > 0 and y == 0:
        if direction == 'W':
            return abs(x) 
        elif direction == 'N' or direction == 'S':
            return abs(x) + 1
        else:
            return abs(x) + 2
    elif x < 0 and y==0:
        if direction == 'E':
            return abs(x)
        elif direction == 'N' or direction == 'S':
            return abs(x) + 1 
        else:
            return abs(x) + 2
    elif x == 0 and y > 0:
        if direction == 'S':
            return abs(y)
        elif direction == 'E' or direction == 'W':
            return abs(y) + 1 
        else:
            return abs(y) + 2
    elif x == 0 and y < 0:
        if direction == 'N':
            return abs(y)
        elif direction == 'E' or direction == 'W':
            return abs(y) + 1
        else:
            return abs(y) + 2 
    else:
        return 0 


print(flr('FFFLLRFFRLLFRSHYAM'))

#%%