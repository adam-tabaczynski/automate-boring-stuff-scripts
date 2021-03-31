def main():
    fd = open('test.txt')
    print(fd.read())

# issues with above code:
# 1. check if file exist
# 2. no encoding defined
# 3. lack of file closing, close()
# 4. read() function is shit af, do not use it
