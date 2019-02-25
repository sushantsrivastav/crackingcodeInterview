

def get_mid(arr,low,high):
    mid = (low + high)/2
    if arr[mid] != '':
        return mid
    mid_l = mid -1
    mid_r = mid + 1

    while arr[mid_l] == '' and arr[mid_r] == '':
        if mid_l < low or mid_r > high:
            return None
        mid_l -= 1
        mid_r += 1
    if arr[mid_l] == '':
        return mid_r
    else:
        return mid_l


def sparse_search(arr,x,low=0,high=None):
    if high == None:
        high = len(arr) -1
    if low > high:
        return None

    mid = get_mid(arr,low,high)

    if mid is None:
        return None
    if x > arr[mid]:
        return sparse_search(arr,x,mid+1,high)
    elif x < arr[mid]:
        return sparse_search(arr,x,low,mid-1)
    else:
        return mid


a = ["at","","","","ball","","","car","","","dad","",""]
x = "ball"
print(sparse_search(a,x))