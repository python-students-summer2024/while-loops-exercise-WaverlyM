

def get_starting_number():
    x=1
    while x==1:
        user_num = input('How many bottles? ')
        try:
           if int(user_num)>0:
            x+=1
        except:
            print('That is not a valid number. ')
    return int(user_num)
   
   
        

def sing(num_bottles):
    for _ in range(num_bottles):
        if num_bottles ==1:
           x='bottle'
           print(f'{num_bottles} {x} of beer on the wall, {num_bottles} {x} of beer.')
        elif num_bottles>1:
           x='bottles'
           print(f'{num_bottles} {x} of beer on the wall, {num_bottles} {x} of beer.')

        num_bottles-=1

        if num_bottles ==1:
            x='bottle'
            print(f'Take one down, pass it around, {num_bottles} {x} of beer on the wall.\n')

        elif num_bottles>1:
            x= 'bottles'
            print(f'Take one down, pass it around, {num_bottles} {x} of beer on the wall.\n')

        elif num_bottles==0:
                print('Take it down, pass it around, no more bottles of beer on the wall!\n')
        


