# Program to solve the problem 14 on projecteuler.net by Luc VuTuan

one_to_nine = {1: 'one', 2: 'two', 3: 'three',
               4: 'four', 5: 'five', 6: 'six',
               7: 'seven', 8: 'eight', 9: 'nine'}

ten_to_nineteen = {10: 'ten', 11: 'eleven', 12: 'twelve',
                   13: 'thirteen', 14: 'fourteen', 15: 'fifteen',
                   16: 'sixteen', 17: 'seventeen', 18: 'eighteen',
                   19: 'nineteen'}

twenty_to_ninety = {20: 'twenty', 30: 'thirty', 40: 'forty', 50: 'fifty',
                    60: 'sixty', 70: 'seventy', 80: 'eighty', 90: 'ninety'}


def translate_number(number):
    if 1 <= number <= 9:
        return one_to_nine[int(number)]
    elif 10 <= number <= 19:
        return ten_to_nineteen[int(number)]
    elif 20 <= number <= 99:
        if number % 10 == 0:
            return twenty_to_ninety[int(number)]
        else:
            return twenty_to_ninety[int(number) - (int(number) % 10)] + "-" \
                   + translate_number(int(number % 10))
    elif 100 <= number <= 999:
        if number % 100 == 0:
            return one_to_nine[int(number) / 100] + " hundred"
        else:
            return one_to_nine[int(number) / 100] + " hundred and " + translate_number(number % 100)


def count_letter(number_str):
    count = 0
    for i in str(number_str):
        if i != "-" and i != " ":
            count += 1
    return count

total = 0

for i in range(1,1001):
    if i != "-" and i != " ":
        total += count_letter(translate_number(i))

print total