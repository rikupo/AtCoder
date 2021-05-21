import numpy as np

def tansaku(nodes,num):
    next_candidate = nodes[num]
    if

def main():
    #N = int(input())

    N = 4
    nodes = [[]]
    for i in range(N):
        nodes.append([])
    for i in range (N):
        Atemp,Btemp = map(int,input().split())
        nodes[Atemp].append(Btemp)  # AにはBと
        nodes[Btemp].append(Atemp)  # BにはAとの関係を記入

    print(N)
    print(nodes)
    # スタートは1でそこから幅優先探索

    tansaku(nodes,1)







if __name__ == '__main__':
    main()