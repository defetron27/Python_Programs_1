from collections import Counter,OrderedDict

class Unique(Counter,OrderedDict):
    pass

if __name__ == '__main__':
    k = int(input())
    s = list(map(int,input().split()))

    s = [i for i,count in Unique(s).items() if count == 1]

    print(s[0])
