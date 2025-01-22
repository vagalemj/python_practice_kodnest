def swap_case(s):
    sample = ''
    for i in (s):
        if i.islower():
            sample += i.upper()
        else:
            sample += i.lower()
    return sample

if __name__ == '__main__':
    s = input()
    result = swap_case(s)
    print(result)