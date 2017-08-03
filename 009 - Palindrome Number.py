class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        if (x<0 or x!=0 and x%10==0):
            return False
        else:
            revnum = 0
            while(x > revnum):
                revnum = revnum * 10 + x % 10
                x /= 10
            return x==revnum or x==revnum/10