class Solution:
    def letterCasePermutation(self, s: str) -> List[str]:
        answers  = set()
        def dfs(word, pointer):
            if pointer==len(word):
                word = "".join(word)
                if word not in answers:
                    answers.add(word)
                return 
            currword = word[pointer]
            if word[pointer].isupper():
                word[pointer] = word[pointer].lower()
            else:
                w = word[pointer]
                word[pointer] = w.upper()
            dfs(word, pointer+1)
            word[pointer] = currword
            dfs(word, pointer+1)
            

        s = list(s)
        dfs(s, 0)
        return (answers)
        