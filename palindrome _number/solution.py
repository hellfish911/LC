# Task https://leetcode.com/problems/palindrome-number/description/

class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        if x < 0:
            return False
        reversed_num = 0
        original = x
        temp = original
        while temp > 0:
            last_digit = temp % 10
            reversed_num = reversed_num * 10 + last_digit
            temp = temp // 10
        return reversed_num == original
