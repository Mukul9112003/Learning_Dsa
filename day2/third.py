n="Nitin"
m="Mukul"
def palindrome(s):
    s=s.lower()
    left=0
    right=len(s)-1
    while left<right:
        if s[left]!=s[right]:
            return False
        left+=1
        right-=1
    return True
print(palindrome(n))
print(palindrome(m))
def rec_palindrome(s,left,right):
    if left>=right:
        return True
    if s[left]!=s[right]:
        return False
    return rec_palindrome(s,left+1,right-1)
print(rec_palindrome(n.lower(),0,len(n)-1)) #None
print(rec_palindrome(m.lower(),0,len(m)-1))