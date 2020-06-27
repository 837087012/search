def lis(nums, target):
    right: int= len(nums) - 1
    left: int=0
    while left<=right:
        if nums[left]==target:
            return left
        elif nums[right]==target:
            return right
        elif len(nums)<=2:
            if nums[left]<target and target<=left[right]:
                left+=1
            elif nums[left]==target:
                return left
            else:
                return -1
        else:
            mid=(left+right)//2
            if nums[mid]<target:
                left=mid
                if right-left==1:
                    return -1
            elif nums[mid]>target:
                right=mid
            elif nums[mid]==target:
                return mid
            else:
                return -1


def solution2(nums,target):
    right=len(nums)
    left=-1
    while left<=right:
        if target<nums[0] or target>nums[-1]:
            return -1
        else:
            mid=(right+left)//2
            if nums[mid]>target:
                right=mid
            elif nums[mid]<target:
                left=mid
                if right-left==1:
                    return -1
            elif nums[mid]==target:
                return mid
        print(left,right)
def solution3(nums,target,left: int,right: int):
    if target<nums[0] or target>nums[-1]:
        return -1
    elif target==nums[0]:
        return 0
    elif target==nums[-1]:
        return len(nums)-1
    else:
        if right>=0:
            mid=left+(right-left)//2
            if nums[mid]>target:
                return solution3(nums,target,left,mid)
            elif nums[mid]<target:
                right-=1
                return solution3(nums,target,mid+1,right)
            else:
                return mid
        else:
            return -1





a=[1,2,3,4,4,6,7,8,9,10]
tar=10
# result=lis(a,tar)
# print(result)
# sol=solution2(a,tar)
# print(sol)
sol1=solution3(a,tar,-1,10)
print(sol1)
# print(pow(2,32))