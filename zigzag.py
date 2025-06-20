import time, sys

indent = 0 #how many spaces to indent
indent_increasing = True

try:
    while True:
        print(' ' * indent, end='')
        print('********')
        time.sleep(0.1)

        if indent_increasing:
            indent = indent + 1
            if indent == 20:
                indent_increasing = False
        else:
            indent = indent - 1
            if indent == 0:
                indent_increasing = True


#we place the rest of the program inside a try statement. When the user presses CTRL-C while a Python program is
# running, Python raises the KeyboardInterrupt exception. If there is no try-except statement to catch this exception,
# the program crashes with an ugly error message. However, we want our program to cleanly handle the KeyboardInterrupt
# exception by calling sys.exit()
except KeyboardInterrupt:
    sys.exit()