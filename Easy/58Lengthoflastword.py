def lengthOfLastWord(self, s: str) -> int:
        str1 = s.strip()
        i=1
        count=0
        while (i<=len(str1)):
            if(str1[-i]==" "):
                return count
            else:
                count += 1
                i +=1
        return count
