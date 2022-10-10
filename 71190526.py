class PrefixConverter:
    def __init__(self):
        self.stackList = ['?']
        
    # method untuk menambahkan data baru
    def push(self,data):
        self.stackList.append(data)
        
    # method untuk melihat data paling atas
    def peek(self):
        if self.stackList:
            return self.stackList[-1]
        else:
            return "Isi Stack Kosong"
        
    #method untuk menghapus data paling atas
    def pop(self):
        if self.stackList:
            data = self.stackList.pop(-1)
            return data
        else:
            return "Isi Stack Kosong"
        
    def cekValidExpression(self,expression):
        try:
            a = self.stackList[i]
            b = self.stackList[self.peek()]
            return True if a <= b else False
        except KeyError:
            return False
        
    def infixToPrefix(self,expression):
        operators = []
        operands = []
 
        for i in range(len(infix)):
        
            if (infix[i] == '(' ):
                operators.append(infix[i])
 
            elif (infix[i] == ')'):
                while (len(operators)!=0 and (operators[-1] != '(' )):
                    op1 = operands[-1]
                    operands.pop()
                    op2 = operands[-1]
                    operands.pop()
                    op = operators[-1]
                    operators.pop()
                    tmp = op + op2 + op1
                    operands.append(tmp)
                operators.pop()
            elif (not isOperator(infix[i])):
                operands.append(infix[i] + "")
 
            else:
                while (len(operators)!=0 and getPriority(infix[i]) <= getPriority(operators[-1])):
                    op1 = operands[-1]
                    operands.pop()
 
                    op2 = operands[-1]
                    operands.pop()
 
                    op = operators[-1]
                    operators.pop()
 
                    tmp = op + op2 + op1
                    operands.append(tmp)
                operators.append(infix[i])
 
        while (len(operators)!=0):
            op1 = operands[-1]
            operands.pop()
 
            op2 = operands[-1]
            operands.pop()
 
            op = operators[-1]
            operators.pop()
 
            tmp = op + op2 + op1
            operands.append(tmp)
        return operands[-1]

    while(1):
        s = input("Infix Expression : ")
        print("PrefixConverter : ", infixToPrefix(s))
        
        
#test case
if __name__ == '__main__':
    expresi1 = PrefixConverter()
    print(expresi1.infixToPrefix("1+2+3*4/2-1"))
    print(expresi1.infixToPrefix("A * (B + C) / D"))
    print(expresi1.infixToPrefix("(1+2)*3"))
    print(expresi1.infixToPrefix("20 * 3 - 10 + 289"))
    print(expresi1.infixToPrefix("100 * 30 / 600 - 30 + 100 * 777"))
