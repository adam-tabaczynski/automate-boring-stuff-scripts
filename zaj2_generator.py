def my_gen(max_num):
    #return [range(1,max_num)] # bad code, with big enough number will crash
    for el in range(1, max_num):
        yield el # yield keyword turns function into generator

def main():
    gen = my_gen(10)
    for el in gen:
        print(el)

my_gen(5)
