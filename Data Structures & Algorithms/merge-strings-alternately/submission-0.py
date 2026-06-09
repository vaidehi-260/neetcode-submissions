class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        i, j = 0, 0
        st = []
        while i < len(word1) and j <len(word2):
            st.append(word1[i])
            st.append(word2[i])
            i+=1
            j+=1
        st.append(word1[i:])
        st.append(word2[j:])
        return "".join(st)
