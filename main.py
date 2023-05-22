import time

def this_function():
    print("This is test function")

def fibonanci(n):
    # # Second attempt
    f = [0, 1]
    
    for i in range(2, n+1):
        f.append(f[i-1] + f[i-2])

    return f[n]

    # # First attempt
    # if n <= 1:
    #     return n
    # return fibonanci(n-1) + fibonanci(n-2)


def walk(w,h):
    # # Second attempt

    arr = []
    for i in range(w):
        col = []
        for j in range(h):
            if(i == 0 or j == 0):
                val = 1
            else:
                val = 0
            col.append(val)
        arr.append(col)

    for i in range(1, w, 1):
        for j in range(1, h, 1):
            arr[i][j] = arr[i-1][j] + arr[i][j-1]

    return arr[w - 1][h - 1]

    # # First attempt

    # if w == 2 and h == 2:
    #     return 2
    # elif w < 2 or h < 2:
    #     return 1
    # return walk(w-1,h) + walk(w,h-1)


if __name__ == "__main__":
   
    start = time.time()
    res = walk(100,100) 
    print(res)
    end = time.time()
    print("Time used: ", end-start)