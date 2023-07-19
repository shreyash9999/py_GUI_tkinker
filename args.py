def add(*args):
    #CAN ADD ANY NUMBER OF WORDS
    sum = 0
    for n in args:
        sum += n
    return sum


print(add(2, 3, 4, 5, 6, 3))

def cal(**kwargs):
    print(kwargs)
    print(kwargs["add"])
#CAN ANY NUMBER OF STUFFF IN DICTORNARY/ kwargs is a dictornay of any number of items
cal(add="2", multy="5")