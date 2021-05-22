import numpy as np
final_depth = []

def tansaku(nodes,passed,num,depth,before_node):
    global final_depth
    print("-------------")
    print(f"** Now Node {num} n depth {depth}")
    next_candidate = nodes[num]
    print(f"next up to {next_candidate}")
    depth = depth + 1
    if before_node < 0:
        print("ITS BEGAN")
    for i in nodes[num]:
        print(f"For node {i}")
        if passed[i] == False:
            print(f"next is {i}")
            passed[i] = True
            before_node = num
            tansaku(nodes,passed,i,depth,before_node)
        else:
            print(f"{i} was already passed, before is {before_node}")
            if before_node == i:
                print("its just looking back")
                if len(nodes[num]) == 1:  # 1つしか接続されていない場合 == 終点
                    print(f"final depth == {depth - 1}")
                    final_depth.append(depth-1)


            continue


def main():

    global final_depth
    #N = int(input())

    N = 10
    nodes = [[]]
    passed = np.full(N+1,False)
    print(passed)
    for i in range(N):
        nodes.append([])
    nodes[1] = [2,3]
    nodes[2] = [1,4]
    nodes[3] = [1,7]
    nodes[4] = [2,5,6]
    nodes[5] = [4]
    nodes[6] = [4]
    nodes[7] = [3,8]
    nodes[8] = [7,9,10]
    nodes[9] = [8]
    nodes[10] = [8]
    '''
    for i in range (N):
        Atemp,Btemp = map(int,input().split())
        nodes[Atemp].append(Btemp)  # AにはBと
        nodes[Btemp].append(Atemp)  # BにはAとの関係を記入
    '''
    print(N)
    print(nodes)
    # スタートは1でそこから幅優先探索
    start_node = 1  # おそらくブランチが2つ以上のノードで始めるべき
    passed[start_node] = True
    before_node = -1 # 存在しないノードでリセット
    tansaku(nodes,passed,start_node,0,before_node) # o si depth initiarize

    print(f"{final_depth}")







if __name__ == '__main__':
    main()