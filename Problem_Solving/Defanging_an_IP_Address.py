# https://leetcode.com/problems/defanging-an-ip-address/description/
class Solution:
    def defangIPaddr(self, address: str) -> str:
        add = address.split(".")
        return "[.]".join(add)
        