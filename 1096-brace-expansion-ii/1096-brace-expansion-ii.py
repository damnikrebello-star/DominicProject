class Solution:
    def braceExpansionII(self, expression: str) -> list[str]:
        stack = []

        operands = []
        ops = []       
        
        def combine_last():
            op = ops.pop()
            right = operands.pop()
            left = operands.pop()
            if op == '*':
                res = {a + b for a in left for b in right}
            elif op == ',':
                res = left.union(right)
            operands.append(res)
            
        i = 0
        n = len(expression)
        
        while i < n:
            ch = expression[i]
            
            if ch.isalpha():

                j = i
                while j < n and expression[j].isalpha():
                    j += 1
                word = expression[i:j]

                if i > 0 and (expression[i-1].isalpha() or expression[i-1] == '}'):
                    while ops and ops[-1] == '*':
                        combine_last()
                    ops.append('*')
                
                operands.append({word})
                i = j - 1
                
            elif ch == '{':
                if i > 0 and (expression[i-1].isalpha() or expression[i-1] == '}'):
                    while ops and ops[-1] == '*':
                        combine_last()
                    ops.append('*')
                
                ops.append('{')
                
            elif ch == ',':
                while ops and ops[-1] != '{':
                    combine_last()
                ops.append(',')
                
            elif ch == '}':
                while ops and ops[-1] != '{':
                    combine_last()
                ops.pop() 
                
            i += 1
            
        while ops:
            combine_last()
            
        return sorted(list(operands[-1]))