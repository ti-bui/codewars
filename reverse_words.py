# link: https://www.codewars.com/kata/5259b20d6021e9e14c0010d4/train/python


def reverse_words(text):
    new_str = []
    str_arr = text.split(' ')
    for i in str_arr:
        new_str.append(i[::-1])
    return ' '.join(new_str)


print(reverse_words("This is an example!"))
