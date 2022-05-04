guess_me = 7
number = 1
while True:
    if number < guess_me:
        print('too low')
    elif number > guess_me:
        print('too high')
    else:
        print('found it')
        break
    number += 1
    
guess_me = 5
for x in range(10):
    if x < guess_me:
        print('too low')
    elif x > guess_me:
        print('too high')
    else:
        print('found it')
        break
    
