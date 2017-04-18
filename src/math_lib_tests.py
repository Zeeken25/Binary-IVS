import unittest
import itertools
import math

import math_lib



class TestParseValidInputTokensAsMathTokens(unittest.TestCase):
    
    """
    Testing if the 'calc_parser' parses input tokens as
    math tokens correctly.
    """
    
    parser = math_lib.CalcParser()
    
    input_tokens = (
        ["-", "1", "*", "-", "2", ".", "5"],
        ["-", "5", ".", "5", "/", "-", "2", "*", "4", "+", "2"],
        ["4", "!", "+", "6", "^", "3", "/", "2"],
        ["2", "7", "$", "3", "-", "9", "*", "-", "4", "+", "4", ".", "5"],
        ["6", "/", "3", "-", "4", "!", "/", "3", "^", "3"] )
    
    expected_tokens = (
        ["-1", "*", "-2.5"],
        ["-5.5", "/", "-2", "*", "4", "+", "2"],
        ["4!", "+", "6", "^", "3", "/", "2"],
        ["27", "$", "3", "-", "9", "*", "-4", "+", "4.5"],
        ["6", "/", "3", "-", "4!", "/", "3", "^", "3"] )

    def test_valid_input(self):
        for t in range( len(self.input_tokens) ):
            # Clearing parser output for each iteration
            parser_output = None
            self.parser.clear_math_tokens_list()
            
            self.parser.parse(self.input_tokens[t])
            parser_output = self.parser.get_math_tokens()
    
            self.assertEqual(parser_output, self.expected_tokens[t])


class TestParseInvalidInputTokensAsMathTokens(unittest.TestCase):
    
    """
    Testing if the 'calc_parser' raises SyntaxError on wrong inputs.
    """
    
    parser = math_lib.CalcParser()
    
    input_tokens = (
        [".", "1", "*", "-", "2", ".", "5"],
        ["-", "5", ".", "5", "/", "*", "2", "*", "4", "+", "2"],
        ["4", "!", "+", "6", "^", "3", "/", "+"],
        ["2", "$", "3", "-", "9", "*", "-", "4", "!", "7", "+", "4", ".", "5"],
        ["6", "/", "3", "-", "4", "^", "/", "3", "^", "3"] )

    def test_invalid_input(self):
        for t in range( len(self.input_tokens) ):
            # Clearing parser output for each iteration
            self.parser.clear_math_tokens_list()

            self.assertRaises(
                    SyntaxError, self.parser.parse, self.input_tokens[t] )         

            
class TestMathBasicBinaryOperations(unittest.TestCase):
    
    """
    Testing all basic binary operations defined in the 'math_lib'.
    test_values = tuple of values from which binary pairs are created
    test_pairs  = all possible pairs from the 'test_values' tuple
    x_op        = x operand for a binary operation
    y_op        = y operand for a binary operation
    exp         = expected value to be compared to the output of the 'math_lib'
    """
    
    mathlib = math_lib.MathLib()
    
    test_values = (
        -2468, -1, 0, 1, 6789, -999.9, -2.4, -1.0, -0.1, 0.1, 1.0, 6.7, 1234.5 )
    test_pairs = [ v for v in itertools.product(test_values, repeat=2) ]
    
    def test_addition(self):
        for x_op, y_op in self.test_pairs:
            exp = eval( str( float(x_op) + float(y_op) ) )
            if exp.is_integer():
                self.assertEqual(
                    self.mathlib.plus(x_op, y_op), str( round(exp) ) )
            else:
                self.assertEqual(self.mathlib.plus(x_op, y_op), str(exp))

    def test_substraction(self):
        for x_op, y_op in self.test_pairs:
            exp = eval( str( float(x_op) - float(y_op) ) )
            if exp.is_integer():
                self.assertEqual(
                    self.mathlib.minus(x_op, y_op), str( round(exp) ) )
            else:
                self.assertEqual(self.mathlib.minus(x_op, y_op), str(exp))

    def test_division(self):
        for x_op, y_op in self.test_pairs:
            try:
                exp = eval( str( float(x_op) / float(y_op) ) )
                if exp.is_integer():
                    self.assertEqual(
                        self.mathlib.divide(x_op, y_op), str( round(exp) ) )
                else:
                    self.assertEqual(
                        self.mathlib.divide(x_op, y_op), str(exp) )
            except ZeroDivisionError:
                self.assertRaises(
                    ZeroDivisionError, self.mathlib.divide, x_op, y_op )

    def test_multiplication(self):
        for x_op, y_op in self.test_pairs:
            exp = eval( str( float(x_op) * float(y_op) ) )
            if exp.is_integer():
                self.assertEqual(
                    self.mathlib.multiply(x_op, y_op), str( round(exp) ) )
            else:
                self.assertEqual(
                    self.mathlib.multiply(x_op, y_op), str(exp) )


class TestMathAdvancedBinaryOperations(unittest.TestCase):
    
    """
    Testing 'power' and 'yroot' operations defined in the "math_lib".
    test_pairs = pairs to be tested
    x_op       = x operand for a binary operation
    y_op       = y operand for a binary operation
    exp        = expected value to be compared to the output of the 'mathlib'
    """
    
    mathlib = math_lib.MathLib()
    
    def test_power(self):
        test_pairs = ((-12, -1), (-1.0, 0), (4.5, 6), (2, 9), (0, 0.1), (0, 0))
        for x_op, y_op in test_pairs:
            exp = pow( float(x_op), float(y_op) )
            if exp.is_integer():
                self.assertEqual(
                    self.mathlib.power(x_op, y_op), str( round(exp) ) )
            else:
                self.assertEqual(self.mathlib.power(x_op, y_op), str(exp))

    def test_y_root_of_x(self):
        test_pairs = ((64, 2), (-120, 5), (-36, 2), (27, -3), (0, 2), (0, 3))
        for x_op, y_op in test_pairs:
            # Preparing the exponent for the pow function
            prep_exp = 1/float(y_op)
            exp = pow( float(x_op), prep_exp )
            
            self.assertEqual(self.mathlib.yroot(x_op, y_op), str(exp))

            
class TestFactorial(unittest.TestCase):
    
    """
    Testing the factorial function defined in the "math_lib".
    test_values = values to be tested
    op          = operand for the factorial
    exp         = expected value to be compared to the output of the 'mathlib'
    """
    
    mathlib = math_lib.MathLib()
    
    def test_factorial(self):
        test_values = (-5.5, -1, 0, 1, 5)
        for op in test_values:
            try:
                exp = math.factorial(op)
                self.assertEqual(
                    self.mathlib.factorial(op), str(exp) )
            except ValueError:
                self.assertRaises(
                    ValueError, self.mathlib.factorial, op )


class TestCalculatorEvaluationOnExamples(unittest.TestCase):
    
    """
    Testing if the evaluation of the input is correct.
    """
    
    mathlib = math_lib.MathLib()
    
    input_tokens = (
        ["6", "!", "-", "3", "$", "2", "7", "*", "-", "1", "/", "2", ".", "5"],
        ["5", "*", "-", "3", "+", "7", "/", "4"],
        ["4", ".", "4", "/", "-", "2", ".", "2", "-", "2"],
        ["6", "^", "3", "/", "2", "$", "6", "4", "/", "-", "0", ".", "5"],
        ["1", "0", "*", "2", ".", "5", "^", "2", "+", "5", "$", "2", ".", "5"] )

    exp_results = ("721.2", "-13.25", "-4", "-54", "63.70112443")
    
    def test_evaluation(self):
        for t in range( len(self.input_tokens) ):
            # Clearing math output for each iteration
            mathlib_output = None
            
            self.mathlib.evaluate(self.input_tokens[t])
            mathlib_output = self.mathlib.get_current_result()
    
            self.assertEqual(mathlib_output, self.exp_results[t])




            
if __name__ == '__main__':
    unittest.main()


    
