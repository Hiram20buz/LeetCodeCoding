class Solution(object):
   def reverse(self, x):
      """
      :type x: int
      :rtype: int
      """
      x = str(x)
      if x[0] == '-':
         a = int('-' + x[-1:0:-1])
         if a >= -2147483648 :
            return a
         else:
            return 0
      else:
          a = int(x[::-1])
          if a<=2147483647:
              return a
          else:
              return 0

              
ob1 = Solution()
print(ob1.reverse(-123))