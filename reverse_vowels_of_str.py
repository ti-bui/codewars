# https://leetcode.com/problems/reverse-vowels-of-a-string/description/?envType=study-plan-v2&envId=leetcode-75

def reverseVowels(s):
    vowels = 'aeiouAEIOU'
    s_list = list(s)
    s_vowels = []

    for c in s:
        if c in vowels:
            s_vowels.append(c)
    s_vowels.reverse()

    vowel_pos = 0

    for i in range(len(s_list)):
        if s_list[i] in vowels:
            s_list[i] = s_vowels[vowel_pos]
            vowel_pos += 1

    return ''.join(s_list)


example = "IceCreAm"

print(reverseVowels(example))
