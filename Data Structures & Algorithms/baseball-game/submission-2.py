class Solution:
    def calPoints(self, operations: List[str]) -> int:
        n = len(operations)
        arr = []
        count = -1
        for i in operations:
            if i =="C":
                arr.pop()
                count -= 1
            elif i =="D":
                arr.append(2*arr[count])
                count+=1
            elif i =="+":
                arr.append(arr[count]+arr[count-1])
                count+=1
            else:
                arr.append(int(i))
                count+=1
        return sum(arr)