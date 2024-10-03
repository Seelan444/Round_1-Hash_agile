class Seelan :
    def reverce( args) :
        arr = [1, 3, 5, 7, 9, 11]
        n = len(arr)
        k = 3
        k = k % n
        i = 0
        j = 0
        i = n - k
        j = n - 1
        while (i < j) :
            temp = arr[i]
            arr[i] = arr[j]
            arr[j] = temp
            i += 1
            j -= 1
        i = 0
        j = n - k - 1
        while (i < j) :
            temp = arr[i]
            arr[i] = arr[j]
            arr[j] = temp
            i += 1
            j -= 1
        i = 0
        j = n - 1
        while (i < j) :
            temp = arr[i]
            arr[i] = arr[j]
            arr[j] = temp
            i += 1
            j -= 1
        t = 0
        while (t < n) :
            print(str(arr[t]) + " ", end ="")
            t += 1
if __name__ == '__main__':
    Seelan.reverce([])