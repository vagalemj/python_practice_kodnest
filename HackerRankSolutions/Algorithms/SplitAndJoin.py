def split_n_join(line):
    s = '-'.join(line.split())
    return s

if __name__ == '__main__':
    line = input()
    result = split_n_join(line)
    print(result)