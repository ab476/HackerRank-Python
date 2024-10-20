import textwrap

def wrap(string, max_width):
    op_str = ""
    for i in range(len(string)):
        if (i != 0) and (i % max_width == 0):  # If max_width is reached
            op_str += "\n"  # Add a newline
        op_str += string[i]  # Add the current character

    return op_str  # Return the wrapped string

if __name__ == '__main__':
    string, max_width = input(), int(input())
    result = wrap(string, max_width)
    print(result)