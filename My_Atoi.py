class Solution(object):
    def myAtoi(self, str):
        """
        :type str: str
        :rtype: int
        """
        newstr = str.lstrip()
        result = ''
        if len(newstr) > 0:
            if (ord(newstr[0]) > 47 and ord(newstr[0]) < 58) or ord(newstr[0]) == 43 or ord(newstr[0]) == 45:
                result += newstr[0]
                flag = 0
                for i in newstr[1:]:
                    if ord(i) > 47 and ord(i) < 58:
                        result += i
                        flag += 1
                    else:
                        break
                if flag == 0 and (ord(result) == 43 or ord(result) == 45):
                    return 0
                if int(result) < 0:
                    return max(int(result),-2147483648)
                else:
                    return min(2147483647,int(result))
            else:
                return 0
        else:
            return 0
