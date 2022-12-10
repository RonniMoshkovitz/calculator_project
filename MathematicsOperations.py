"""
module of all the mathematics operations supported on this calculator
"""


def add(operand_a: float, operand_b: float) -> float:
    """
    The function preforms addition of two operands, and returns the result.
    :param operand_a: first operand
    :param operand_b: second operand
    :return: addition result
    """
    return operand_a + operand_b


def sub(operand_a: float, operand_b: float) -> float:
    """
    The function preforms subtraction on two operands, and returns the result.
    :param operand_a: first operand
    :param operand_b: second operand
    :return: subtraction result
    """
    return operand_a - operand_b


def mult(operand_a: float, operand_b: float) -> float:
    """
    The function preforms multiplication of two operands, and returns the result.
    :param operand_a: first operand
    :param operand_b: second operand
    :return: multiplication  result
    """
    return operand_a * operand_b


def div(operand_a: float, operand_b: float) -> float:
    """
    The function preforms division on two operands, and returns the result.
    :param operand_a: first operand
    :param operand_b: second operand
    :return: division result
    """
    return operand_a / operand_b


def power(operand_a: float, operand_b: float) -> float:
    """
    The function preforms the first operand by the power of the second operand, and returns the result.
    :param operand_a: first operand
    :param operand_b: second operand
    :return: power result
    """
    return pow(operand_a, operand_b)


def modulo(operand_a: float, operand_b: float) -> float:
    """
    The function preforms modulo on two operands, and returns the result.
    :param operand_a: first operand
    :param operand_b: second operand
    :return: modulo result
    """
    return operand_a % operand_b


def maximum(operand_a: float, operand_b: float) -> float:
    """
    The function returns the operand with the higher value.
    :param operand_a: first operand
    :param operand_b: second operand
    :return: operand with the higher value
    """
    return operand_a if operand_a > operand_b else operand_b


def minimum(operand_a: float, operand_b: float) -> float:
    """
    The function returns the operand with the lower value.
    :param operand_a: first operand
    :param operand_b: second operand
    :return: operand with the lower value
    """
    return operand_a if operand_a < operand_b else operand_b


def avg(operand_a: float, operand_b: float) -> float:
    """
    The function returns the average of the operands.
    :param operand_a: first operand
    :param operand_b: second operand
    :return: average of operands
    """
    return (operand_a + operand_b) / 2


def neg(operand: float) -> float:
    """
    The function returns the negative value to the operand.
    :param operand: operand
    :return: negative value to the operand
    """
    return -operand


def factorial(operand: float) -> float:
    """
    The function returns the factorial of the operand.
    :param operand: operand
    :return: factorial result
    """
    if operand == 1:
        return 1
    # runs recursively and multiples by all the native nums from 1 to the operand
    return factorial(operand - 1) * operand
