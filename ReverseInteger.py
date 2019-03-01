

#Given a 32-bit signed integer, reverse digits of an integer.


class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        answer = 0
        sign = 1 if x > 0 else -1
        x = abs(x)
        while x > 0:
            answer = answer * 10 + x % 10
            x /= 10
        return sign*answer if sign*answer < 2147483648 and sign*answer >= -2147483648 else 0
        ## consider the overflow
	
	
	
	# better performance 
import math
class Solution(object):
	def reverse(self, x):
		sign = 1
		if x < 0 :
			sign = 0
		x = int(str(abs(x))[::-1])
		if x > pow(2,31)-1 or x < -pow(2,31):
			return 0
		if not sign:
			x= -x
		return x
        