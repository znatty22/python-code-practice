## This is the text editor interface. 
## Anything you type or change here will be seen by the other person in real time.
# Calculator 

# Yes 1, "1"
# No "A", "%"
#
# 1. A + B
#  e.g. a = 1
#       b = 1 
#       cal.add(a,b) => 2
# 2. A - B
# 3. A * B
#    [A * B] * C 
#    [[ A + A + A + A ...] B times ] C times
# 4. A / B
# 5. A ^ 2 
# 6. A square root 
#

class Calculator(object):
    """
    Simple calculator which supports basic arithmetic operations:
    add, subtract, multiply, divide, and square, and square root.
    """

    def __init__(self):
        pass

    def add(self,operands):
        """
        Adds elements in operand list: A + B + C + ... 
        
        Args:
            operands: list of numbers to operate on

        Returns:
            Result of add operation

        Raises: 
            ValueError:
                One or more operand(s) was not valid.
                Operand must be a token that can 
                be float or int. Chars are invalid tokens.
        """

        sum = 0
        for operand in operands:
            # Try converting input to float.
            try:
                operand = float(operand)
            except ValueError:
                print 'Invalid token in operand list! Ints or floats only'
                return None

            sum+= operand
        
        return sum
    
    def subtract(self,operands):
        """
        Subtracts elements in operand list: A - B - C - ...

        * Negates each operand and adds all operands
        toegether using Calculator.add method.
        
        Args:
            operands: list of numbers to operate on

        Returns:
            Result of subtract operation

        Raises: 
            ValueError:
                One or more operand(s) was not valid.
                Operand must be a token that can 
                be float or int. Chars are invalid tokens.
        """

        operands = [-1*operand for operand in operands]
        return self.add(operands)
    
    def multiply(self,operands):
        """
        Multiplies elements in operand list: A * B * C * ...
        and returns *integer* result.

        * Uses Calculator.add method.
        
        Args:
            operands: list of numbers to operate on

        Returns:
            Result of multiply operation

        Raises: 
            ValueError:
                One or more operand(s) was not valid.
                Operand must be a token that can 
                be float or int. Chars are invalid tokens.
        """

        # Base case - only 1 element in stack, must be the end result
        if len(operands) == 1:
            return float(operands[0])    
        else:
            # Multiply next two operands in stack
            op1 = operands.pop()
            op2 = operands.pop()
            local_result = float(self._multiply2(op1, op2))

            # Push local result onto stack
            operands.append(local_result)

            return self.multiply(operands)
    
    def divide(self,operands):
        """
        Divides elements in operand list: A / B / C / ...

        * Flips each operand (1/operand) in list and
        Uses Calculator.multiply method.
        
        Args:
            operands: list of numbers to operate on

        Returns:
            Result of divide operation

        Raises: 
            ValueError:
                One or more operand(s) was not valid.
                Operand must be a token that can 
                be float or int. Chars are invalid tokens.
            ZeroDivisionError:
                One or more operands was equal to 0.
        """

        try:
            operands = [float(1)/float(operand) for operand in operands]
        except ZeroDivisionError:
            print 'ZeroDivision Error!'
            return None

        return self.multiply_general(operands)
    
    def square(self,operand):
        """
        Multiplies operand with itself: A * A

        Uses Calculator.multiply method.
        
        Args:
            operand: number to operate on

        Returns:
            Result of square operation

        Raises: 
            ValueError:
                One or more operand(s) was not valid.
                Operand must be a token that can 
                be float or int. Chars are invalid tokens.
        """

        return self.multiply([operand,operand])

    def square_root(self,operand):
        """
        Square root of operand: A ^ 0.5

        Uses built in exponential operation.
        
        Args:
            operand: number to operate on

        Returns:
            Result of square root operation

        Raises: 
            ValueError:
                One or more operand(s) was not valid.
                
                Operand must be a token that can 
                be float or int. Chars are invalid tokens.

                Operands must be positive numbers.
        """

        # Try converting input to float.
        try:
            operand = float(operand)
        except ValueError:
            print 'Invalid token in operand list! Ints or floats only'
            return None

        # Operand must be positive    
        try:
            if operand < 0.0:
                raise ValueError
        except ValueError:
            print 'Operand must be a positive number'
            return None    
               
        return (operand**0.5)
     
    def multiply_general(self,operands):
        """
        Multiplies elements in operand list: A * B * C * ...
        and returns float result.

        * Uses built in multiply operation.
        
        Args:
            operands: list of numbers to operate on

        Returns:
            Result of multiply operation

        Raises: 
            ValueError:
                One or more operand(s) was not valid.
                Operand must be a token that can 
                be float or int. Chars are invalid tokens.
        """

        result = 1
        for operand in operands:
            # Try converting input to float.
            try:
                operand = float(operand)
            except ValueError:
                print 'Invalid token in operand list! Ints or floats only'
                return None

            result *= operand
        
        return result

    # ----------------- Private functions  ----------------- #

    def _multiply2(self,op1,op2):
        """
        Helper function which multiplies two operands
        together and returns *integer* result.
        
        Args:
            op1: first operand
            op2: second operand

        Returns:
            Result of multiply operation

        Raises: 
            ValueError:
                One or more operand(s) was not valid.
                Operand must be a token that can 
                be float or int. Chars are invalid tokens.
        """
        
        # Convert to ints
        op1 = int(op1)
        op2 = int(op2)

        # Determine sign of result
        operand1 = op1
        operand2 = op2
        if (op2 < 0) and (op1 >= 0):
            operand1 = op2
            operand2 = op1
        elif (op1 < 0) and (op2 < 0):
            operand1 = abs(op1)
            operand2 = abs(op2)

        # Add operand1 with itself, <operand2> number of times    
        operands = [operand1 for i in range(operand2)]
        
        return self.add(operands)
                

# ----------------- Unit Tests ----------------- #
def test_add(operands, expected):
    c = Calculator()
    result = c.add(operands)
    print 'Testing Calculator.add:'
    print ' Inputs %s' % str(operands)
    print ' Output %s' % str(result)
    print ' Expected: %s' % str(expected) 
    print ' Status: %s' % str(expected == result)

def test_subtract(operands, expected):
    c = Calculator()
    result = c.subtract(operands)
    print 'Testing Calculator.subtract:'
    print ' Inputs %s' % str(operands)
    print ' Output %s' % str(result)
    print ' Expected: %s' % str(expected) 
    print ' Status: %s' % str(expected == result)

def test_multiply(operands, expected):
    c = Calculator()
    print 'Testing Calculator.multiply:'
    print ' Inputs %s' % str(operands)
    result = c.multiply(operands)
    print ' Output %s' % str(result)
    print ' Expected: %s' % str(expected) 
    print ' Status: %s' % str(expected == result)
    
def test_divide(operands, expected):
    c = Calculator()
    result = c.divide(operands)
    print 'Testing Calculator.divide:'
    print ' Inputs %s' % str(operands)
    print ' Output %s' % str(result)
    print ' Expected: %s' % str(expected) 
    print ' Status: %s' % str(expected == result)

def test_square(operand, expected):
    c = Calculator()
    result = c.square(operand)
    print 'Testing Calculator.square:'
    print ' Input %s' % str(operand)
    print ' Output %s' % str(result)
    print ' Expected: %s' % str(expected) 
    print ' Status: %s' % str(expected == result)

def test_square_root(operand, expected):
    c = Calculator()
    result = c.square_root(operand)
    print 'Testing Calculator.square_root:'
    print ' Input %s' % str(operand)
    print ' Output %s' % str(result)
    print ' Expected: %s' % str(expected) 
    print ' Status: %s' % str(expected == result)

def test_multiply2(operands,expected):
    c = Calculator()
    result = c._multiply2(operands[0],operands[1])
    print 'Testing Calculator.multiply2:'
    print ' Input %s' % str(operands)
    print ' Output %s' % str(result)
    print ' Expected: %s' % str(expected) 
    print ' Status: %s' % str(expected == result)

def test_multiply_general(operands,expected):
    c = Calculator()
    result = c.multiply_general(operands)
    print 'Testing Calculator.multiply_general:'
    print ' Input %s' % str(operands)
    print ' Output %s' % str(result)
    print ' Expected: %s' % str(expected) 
    print ' Status: %s' % str(expected == result)    

# Run test cases
test_add(['A',2,3], None)
test_add([1,2,3], 6)
test_add([-1,2,3], 4)

test_subtract([1,2,3], -6)
test_subtract([-1,-2,-3], 6)
test_subtract([0,0,0], 0)

test_multiply_general([2,3,1,1,1],6.0)
test_multiply2([-1,-1],1)
test_multiply2([-1,1],-1)
test_multiply2([1,-1],-1)
test_multiply2([1,1],1)
test_multiply([-1,-1,-10],-10)
test_multiply([-1,1,-10],10)
test_multiply([1,2,3],6)

test_divide([0],None)
test_divide([1,1,1],1)
test_divide([1,2],0.5)
test_divide([1,-1],-1)
test_divide([-1,-1],1)

test_square(0,0)
test_square(2,4)

test_square_root(-1,None)
test_square_root(0,0)
test_square_root(49,7)
test_square_root(10.5,3.24037034920393)

