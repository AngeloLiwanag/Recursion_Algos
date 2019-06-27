# JUNE 27, 2019

# function printItoX
def printItoX(i,x):
    if i == x:
        return
    else:
        print(i)
        return printItoX(i+1, x)

# printCurrAndSum 
def printCurrAndSum(sum, curr, end):
    if curr == end:
        print(sum)
        return
    else:
        print(curr)
        print(sum += curr)
        return printCurrAndSum(sum, curr+1, end)

# printMaxArray
def printCurrAndSum(max, arr, idx):
    if idx == len(arr):
        return
    else:
        if max < arr[idx]:
            max = arr[idx]
            return printMaxArray(max, arr, idx+1)
        else:
            return printMaxArray(max, arr, idx+1)

# returnOddsArray
def returnOddsArray(idx, arr):
    if idx == len(arr):
        return
    else:
        if arr[idx] % 2 !=0:
            arr.append(arr[idx])
            return returnOddsArray(idx+1, arr)
        else:
            arr.pop(arr[idx])
            return returnOddsArray(idx+1, arr)