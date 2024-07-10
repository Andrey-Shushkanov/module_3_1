calls = 0

def count_calls():
   global calls
   calls += 1

def string_info(string):
    count_calls()
    return len(string), string.upper(), string.lower()

def is_contains(string, list_to_search):
    count_calls()
    for item in list_to_search:
        if string.upper() in item.upper():
            a = True
            break
        else:
            a = False
    return  a



print(string_info('qwetuyio'))
print(string_info('qwetsdfgfduyio'))
print(is_contains('Urban', ['ban', 'BaNaN', 'urBAN']))
print(is_contains('cycle', ['recycling', 'cyclic']))
print(calls)