"""
Bernardo Paulsen

Exercise from class 97 from section 8
from Learn Complete Python In Simple Way.
"""

def main():
    first()
    second()
    third()
    fourth()

def first():
    for i in range(10):
        print(i)
        if i == 7:
            print('Breaking loop')
            break
    print('Outside loop')

def second():
    lis_t = [10,20,30,100,200,400]
    for item in lis_t:
        print(item)
        if item >= 100:
            print('Item bigger than or equal to 100, breaking loop')
            break
    print('Outside loop')

def third():
    for i in range(10):
        if not i%2:
            continue
        print(i)

def fourth():
    lis_t = [10,20,0,30]
    for item in lis_t:
        if item == 0:
            print('Division by zero, skipping number.')
            continue
        print(f'100/{item} = {100/item:.2f}')

main()
