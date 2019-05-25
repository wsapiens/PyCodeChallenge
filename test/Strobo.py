"""
-------------------
Long-form question
-------------------
    A "Strobogrammatic Number" is a number that looks the same
    when rotated 180 degrees (upside down) on an LED screen.
    E.g.
       11 -> 11, Strobogrammatic
       252 -> 252, Strobogrammatic
       37 -> LE, Not!
    Write a function to determine whether a number is strobogrammatic.

    ####  ####  ####
    #        #  #
    ####  ####  ####
       #  #        #
    ####  ####  ####
"""

# 0 after 180° rotation : (0 → 0)
# 1 after 180° rotation : (1 → 1)
# 2 after 180° rotation : (2 → 2)
# 5 after 180° rotation : (5 → 5)
# 8 after 180° rotation : (8 → 8)
# 6 after 180° rotation : (6 → 9)
# 9 after 180° rotation : (9 → 6)


def is_strobogrammatic(number):
    strobo_numbers = ['0', '1', '2', '5','6', '8', '9']
    s = str(number)
    reverse = []
    for c in s[::-1]:
        if c == '6':
            reverse.append('9')
        elif c == '9':
            reverse.append('6')
        else:
            reverse.append(c)
    reverse = ''.join(reverse)

    for i in range(len(s)):
        if s[i] not in strobo_numbers:
            return False
        elif s[i] in ['6', '9'] and len(s)%2 !=0:
            return False
        elif s[i] != reverse[i]:
            return False
    return True

def get_strobogrammatic_numbers(n):
    result = []
    i = 0
    while len(result) < n:
        if is_strobogrammatic(i):
            result.append(i)
        i +=1
    return result

def test_strobo():
    test_cases = [
      (0, True),
      (2, True),
      (3, False),
      (6, False),
      (10, False),
      (13, False),
      (11, True),
      (16, False),
      (33, False),
      (69, True),
      (101, True),
      (131, False),
      (161, False),
      (18081, True),
    ]
    for test, result in test_cases:
        my_result = is_strobogrammatic(test)
        print(test, result, my_result)
        # assert my_result == result, ('Error for value: ' + str(test))

test_strobo()

result = get_strobogrammatic_numbers(5)
print(result)
