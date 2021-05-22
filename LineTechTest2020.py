import numpy as np
import datetime
import sys

def main():
    #N,T,D = input_checker()
    #print(f"{N} \n {T} \n {D}")

    N = [1,2,3]
    T = ["10:33:35.513","10:33:49.401","10:34:11.049"]
    D = [0.0,71.9,69.5]
    #T = list(map(datetime.datetime.strptime,T,"%H:%M:%S.%f"))
    for i in range(len(T)):
        T[i] = datetime.datetime.strptime(T[i],"%H:%M:%S.%f")
    print(f"{N} \n {T} \n {D}")


def input_checker():

    '''
    input template

1 10:33:35.513 0.0
2 10:33:49.401 71.9
3 10:34:11.049 69.5


    N = [1,2,3]
    T = ["10:33:35.513","10:33:49.401","10:34:11.049"]
    D = [0.0,71.9,69.5]

    '''
    N = []
    T = []
    D = []
    i = 1
    while True:
        try:
            input_list = input()
            n, t, d = input_list.split()
        except ValueError:
            if len(input_list) == 0:  # 最終行は空白
                if i <= 2:  # データ数が2未満で終了
                    print("not enough input")
                    return 0
                break
            else:
                print("ERROR")
                return 0
        N.append(int(n))
        #  各種エラー処理
        try:  # 時間が正規のフォーマットかチェック
            time = datetime.datetime.strptime(t, "%H:%M:%S.%f")
        except ValueError:
            print("ERROR WRONG TIME STAMP")
            return 0
        if time.hour > 99:
            print("ERROR Hour over")
            return 0
        if i >= 2:
            timegap = (time - before_time).seconds
            if timegap < 0:  # 時系列順になっているか
                print("ERROR order")
                return 0
            if timegap > 45:  # 前回データから45秒以上はなれていないか
                print("ERROR 45rule")
                return 0
        elif i == 1:
            if float(d) != 0.0:  # 初乗りレコードが0から始まっているか
                print("ERROR zero starts")
                return 0
        T.append(time)
        D.append(float(d))

        before_time = time
        i += 1

    return N, T, D


if __name__ == '__main__':
    main()
