class Solution:
    def areSentencesSimilar(self, sentence1: str, sentence2: str) -> bool:
        s1 = sentence1.split(" ")
        s2 = sentence2.split(" ")
        if len(s1)>len(s2):
            s1,s2=s2,s1
        prefix = 0
        l1 = 0
        while l1<len(s1):
            if s1[l1]==s2[l1]:
                prefix+=1
                l1+=1
            else:
                break
        suffix = 0
        l2 = len(s1)-1
        r2 = len(s2)-1
        while l2>=0:
            if s1[l2]==s2[r2]:
                l2-=1
                r2-=1
                suffix+=1
            else:
                break

        total= prefix+suffix
        return total>=len(s1)
        