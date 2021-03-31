import time, sys

indent = 0
isIndentIncreasing = True

try:
    while True:
        print(' ' * indent, end='')
        print('********')
        time.sleep(0.1)

        if isIndentIncreasing:
            indent += 1
            if indent == 10:
                isIndentIncreasing = False
        else:
            indent -= 1
            if indent == 0:
                isIndentIncreasing = True

except:
    sys.exit()
    
