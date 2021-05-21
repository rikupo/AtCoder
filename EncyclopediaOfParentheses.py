import numpy as np

#  これだと謎に通らない.手動入力だと大丈夫なのに．
#  出力フォーマットかテストケースになんか引っかかってそう．
#
def main():
    N = int(input())
    #N = 6
    #print(f"N is {N}")
    outputstr = ""
    if N < 0:
        return 0
    if int(N/2) == N/2:
        for i in range(int(N/2)):
            outputstr = outputstr + "()"
        print(outputstr,end="")

    else:
        #print("hello")
        print("",end="")

if __name__ == '__main__':
    main()