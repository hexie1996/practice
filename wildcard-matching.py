class Solution(object):
    def isMatch(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: bool
        """
        ptr_s=0
        ptr_p=0
        if(p=="" and s==""):
            return True
        elif(p==""):
            return False
        elif(s==""):
            i=0
            while(i<=len(p)-1):
                if(p[i]!='*'):
                    return False
                i=i+1
            return True
        while(1):
            if(p[ptr_p]=='*'):
                while(1):
                    if(ptr_p==len(p)-1):
                        return True
                    if(p[ptr_p+1]=='*'):
                        ptr_p=ptr_p+1
                        continue
                    elif(s[ptr_s]==p[ptr_p+1] or p[ptr_p+1]=='?'):
                        if(Solution.isMatch(self,s[ptr_s+1:],p[ptr_p+2:])==True):
                            return True

                    if(ptr_s==len(s)-1):
                        return False
                    else:
                        ptr_s=ptr_s+1
            elif(p[ptr_p]=='?'):
                if(ptr_p==len(p)-1 and ptr_s==len(s)-1):
                    return True
                elif(ptr_p==len(p)-1):
                    return False
                elif(ptr_s==len(s)-1):
                    i=ptr_p+1
                    while(i<=len(p)-1):
                        if(p[i]!='*'):
                            return False
                        i=i+1
                    return True
                else:
                    ptr_p=ptr_p+1
                    ptr_s=ptr_s+1
            else:
                if(ptr_p==len(p)-1 and ptr_s==len(s)-1):
                    if(s[ptr_s]==p[ptr_p]):
                        return True
                    else:
                        return False
                elif(ptr_p==len(p)-1):
                    return False
                elif(ptr_s==len(s)-1):
                    if(s[ptr_s]==p[ptr_p]):
                        i=ptr_p+1
                        while(i<=len(p)-1):
                            if(p[i]!='*'):
                                return False
                            i=i+1
                        return True
                    else:
                        return False
                else:
                    if(s[ptr_s]==p[ptr_p]):
                        ptr_p=ptr_p+1
                        ptr_s=ptr_s+1
                    else:
                        return False
s=Solution()
print(s.isMatch("abbabaaabbabbaababbabbbbbabbbabbbabaaaaababababbbabababaabbababaabbbbbbaaaabababbbaabbbbaabbbbababababbaabbaababaabbbababababbbbaaabbbbbabaaaabbababbbbaababaabbababbbbbababbbabaaaaaaaabbbbbaabaaababaaaabb",
"**aa*****ba*a*bb**aa*ab****a*aaaaaa***a*aaaa**bbabb*b*b**aaaaaaaaa*a********ba*bbb***a*ba*bb*bb**a*b*bb"))