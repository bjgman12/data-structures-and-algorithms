

def multi_bracket_validation(input_str):
    """this function take in a string and return a value true
    or false base on if the brackets are balance or not

    Args:
        input_str ([type]): [description]

    Returns:
        [type]: [description]

    """
    #checks a base case to reduce computing where not needed
    if len(input_str) % 2 is not 0:
        return False

    opens = tuple('({[')
    closed = tuple (')}]')

    mapped = dict(zip(opens,closed))
    # creates a dictionary with key value pairs setting keys to first arguement and value to second
    # print(map)
    helper = []

    for char in input_str:
        if char in opens:
            helper.append(mapped[char])
        elif char in closed:
            if not helper or char != helper.pop():
                return False
    return not helper



if __name__ == "__main__":
    print(multi_bracket_validation('[](){}'))
    print(multi_bracket_validation('[()]{}'))
    print(multi_bracket_validation('[(]){}'))
    print(multi_bracket_validation('[](){'))

            

