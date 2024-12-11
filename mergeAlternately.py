class Solution(object):
    def mergeAlternately(self, word1, word2):
        result = ""
        word1Length = len(word1)
        word2Length = len(word2)
        if word1Length > word2Length:
            for i in range(word2Length):
                print(word1[i])
                result = result + word1[i] + word2[i]

            result = result + word1
        elif word2Length < word2Length:
            for i in range(word1Length):
                print(word1[i])
                result = result + word1[i] + word2[i]
        else:
            for i in range(word1Length):
                result = result + word1[i] + word2[i]
        return result


merge_String_Obj = Solution()
word1, word2 = "ab", "pqrs"
print(merge_String_Obj.mergeAlternately(word1, word2))
