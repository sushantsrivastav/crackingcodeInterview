#A magic index in an array A [e ... n -1] is defined to be an index such that A[ i] = i.
# Given a sorted array of distinct integers, write a method to find a magic index, if one exists, in array A.
# FOLLOW UP What if the values are not distinct?

def magic_index(arr,dup):
    if not dup:
        magic_index_helper(arr,0,len(arr)-1)
    else:
        magic_index_helper_duplicate(arr,0,len(arr)-1)

def magic_index_helper(arr,start,end):
    mid = (start + end)/2
    if arr[mid] == mid:
        return mid
    if mid < arr[mid]:
        return magic_index_helper(arr,start,mid-1)
    else:
        return magic_index_helper(arr,mid+1,end)

def magic_index_helper_duplicate(arr,start,end):
    mid = (start + end)/2
    midval = arr[mid]
    if mid == midval:
        return mid
    leftindex = min(midval,mid-1)
    left = magic_index_helper_duplicate(arr,start,leftindex)
    if left >= 0:
        return left
    rightindex = max(midval,mid+1)
    right = magic_index_helper_duplicate(arr,mid+1,rightindex)
    return right