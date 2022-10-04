class skobki:
   def proverka_skobok(self, str1):
        stack = []
        pchar = {"(": ")", "{": "}", "[": "]"}
        for skobka_current in str1:
            if skobka_current in pchar:
                stack.append(skobka_current)
            elif len(stack) == 0 or pchar[stack.pop()] != skobka_current:
                return False 
        return len(stack) == 0
    
print(skobki().proverka_skobok(input("Введите скобки:")))