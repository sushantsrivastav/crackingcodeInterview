

def rotated_search(arr,target,left=0,right=None):
    if right == None:
        right = len(arr) -1
    mid = (left + right)/2
    if target == arr[mid]:
        return True
    if left > right:
        return False
    if arr[mid] < arr[right]:
        if arr[mid] < target <= arr[right]:
            return rotated_search(arr,target,mid+1,right)
        else:
            return rotated_search(arr,target,left,mid-1)
    elif arr[mid] > arr[right]:
        if arr[left] <= target < arr[mid]:
            return rotated_search(arr,target,left,mid-1)
        else:
            return rotated_search(arr,target,mid+1,right)
    elif arr[mid] == arr[right]:
        if arr[mid] != arr[left]:
            return rotated_search(arr,target,left,mid-1)
        else:
            bool = rotated_search(arr,target,mid+1,right)
            if bool is False:
                return rotated_search(arr,target,left,mid-1)
            else:
                return bool
    return False

arr = [2,5,6,0,0,1,2]
target = 9
print(rotated_search(arr,target))