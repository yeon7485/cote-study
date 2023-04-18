while(True):
    n = int(input())
    if n == -1:
        break
    else:
        arr = []
        for i in range(1, n//2 + 1):
            if n % i == 0:
                arr.append(i)
        if sum(arr) == n:
            arr = list(map(str, arr))
            s = ' + '.join(arr)
            print(f"{n} = {s}")
        else:
            print(f"{n} is NOT perfect.")
