class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        res = [-1 for x in range(len(nums2))]
        stack = []
        hasmap = {}
        for x in nums1:
            hasmap[x]=-1
        for y in range(len(nums2)):
            hasmap[nums2[y]] = y
        for z in range(len(nums2)):
            # print(stack)
            if len(stack)==0:
                stack.append(z)
            else:
                # lastele = stack[-1]
                while len(stack)!=0 and nums2[stack[-1]]<nums2[z]:
                    lastele = stack.pop()
                    res[lastele] = nums2[z]
                
                stack.append(z)
        for a in range(len(nums1)):
            nums1[a]  = res[hasmap[nums1[a]]]
        return (nums1)