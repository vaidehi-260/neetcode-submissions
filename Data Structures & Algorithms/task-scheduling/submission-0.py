class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        freq = [0] * 26
        for task in tasks:
            index = ord(task) - ord('A')
            freq[index] += 1
        maxFreq = 0
        for i in range(26):
            if freq[i] > maxFreq:
                maxFreq = freq[i]
        countMax = 0
        for i in range(26):
            if freq[i] == maxFreq:
                countMax += 1

        cycles = (maxFreq - 1) * (n + 1) + countMax

        if cycles > len(tasks):
            return cycles

        return len(tasks)