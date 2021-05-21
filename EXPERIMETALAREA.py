import numpy as np

def main():
    #N = int(input())

    N = 3
    a = [[1,2,3]]
    b = [5,6]
    a.append(b)
    a[0].append(4)
    a[1].append(9)
    print(a)

    nodes = [[]]
    for i in range(N-1):
        nodes.append([])
    print(nodes)
    nodes[0].append(5)
    print(nodes)




if __name__ == '__main__':
    main()