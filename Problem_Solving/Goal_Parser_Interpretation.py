# https://leetcode.com/problems/goal-parser-interpretation/description/
class Solution:
    def interpret(self, command: str) -> str:
        output = ""
        s = command
        for i in range(len(command)):
            # print(s[i])
            if i+1 <= len(command):
                print(s[i], end = " ")
                # if s[]
                if s[i] == "(":
                    if s[i+1] == ")":
                        output += "o"
                        continue
                    else:
                        continue
                elif s[i] == ")":
                    continue
                else:
                    output+= s[i]
                    continue
            # if i = len(s)-1

        print()
        print(output)
        output = output.replace("(", "")
        output = output.replace(")","")
        return output

                