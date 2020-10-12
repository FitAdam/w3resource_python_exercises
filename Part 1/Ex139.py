"""139. Write a Python program to valid a IP address. """



class Solution(object):
   def validIPAddress(self, IP):
      """
      :type IP: str
      :rtype: str
      """
      def isIPv4(s):
         try: return str(int(s)) == s and 0 <= int(s) <= 255
         except: return False
      def isIPv6(s):
         if len(s) > 4:
            return False
         try : return int(s, 16) >= 0 and s[0] != '-'
         except:
            return False
      if IP.count(".") == 3 and all(isIPv4(i) for i in IP.split(".")):
         return "IPv4"
      if IP.count(":") == 7 and all(isIPv6(i) for i in IP.split(":")):
         return "IPv6"
      return "Neither"
ob = Solution()





print(ob.validIPAddress("45.56.164.80"))
print(ob.validIPAddress("2001:4860:4860::8888"))


