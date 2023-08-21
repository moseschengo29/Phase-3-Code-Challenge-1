# # Challenge 1
print('--CHALLENGE 1--')
hour = input('Enter hour: ')
minutes = input('Enter minutes: ')
period = input('Enter period (am/pm): ')



def time(hour, minute, period):
    if hour.isdigit() and minute.isdigit():
        if 1 <= int(hour) <= 12 and 0 <= int(minute) <= 59 and period in ('pm', 'am'):
            if period == 'am':
                if int(hour) < 10:
                    hour = '0' + hour
                if hour == '12':
                    hour = '00'
                else :
                    hour = hour
                
                if int(minute) < 10:
                        minute = '0' + minute            
                        print(f'{hour}{minute}hrs')
            
            if period == 'pm':
                if hour == '12':
                    hour == '12'
                    
                else :
                    hour = int(hour) + 12
                if int(minute) < 10:
                    minute = '0' + minute       
            print(f'Time in 24 hour system: {hour}{minute}hrs' )
            print() # add a space below
            
        else:
            print('Hour must be between 1 - 12, minutes must be between 0 - 59, period must be either am or pm') 
            print() # add a space below
    else:
        print('Hour and minutes must be a number! ')
        exit()        
        
                   
time(hour, minutes, period) 


# Challenge 2
print('--CHALLENGE 2--')
num1 = int(input('Enter first number: '))
num2 = int(input('Enter second number: '))
num3 = int(input('Enter third number: '))

postive_nums = []

def even(num_list):
    for num in num_list:
        if num >= 0:
           postive_nums.append(num)
    
    if len(postive_nums) == 2:
        print(True)
        print() # add a space below
        
    else:
        print(False)
        print() # add a space below
                       

even([num1, num2, num3])

# Challenge 3
print('--CHALLENGE--3')
word = input('Enter a word: ').lower()

def solve(word):
    value = {
        "a": 1, "b": 2, "c": 3, "d": 4, "e": 5,
        "f": 6, "g": 7, "h": 8, "i": 9, "j": 10,
        "k": 11, "l": 12, "m": 13, "n": 14, "o": 15,
        "p": 16, "q": 17, "r": 18, "s": 19, "t": 20,
        "u": 21, "v": 22, "w": 23, "x": 24, "y": 25, "z": 26
    }

    vowels = "aeiou"
    max_value = 0
    current_value = 0

    for char in word:
        if char not in vowels:
            current_value += value[char]
            print(char)
        else:
            max_value = max(max_value, current_value)
            current_value = 0

    # Check if the last consonant substring has the highest value
    max_value = max(max_value, current_value)

    return f'Consonant value {max_value}'


print(solve(word))