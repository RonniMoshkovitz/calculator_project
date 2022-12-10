from configuration import *
from InputOutput import *

"""
validates the entered string, to start pars
"""


def remove_extra_minus_signs(equation_str: str) -> str:
    """
    The function removes extra minus signs from the input string.
    :param equation_str: input equation string
    :return: the input equation without extra minus signs
    """
    while MINUS_SIGN * 3 in equation_str:
        equation_str = equation_str.replace(MINUS_SIGN * 3, MINUS_SIGN)
    return equation_str


def remove_extra_spaces(equation_str: str) -> str:
    """
    The function removes extra spaces from the input string.
    :param equation_str: input equation string
    :return: the input equation without extra spaces and tabs
    """
    return "".join(equation_str.split())


def is_valid_symbol(symbol: str) -> bool:
    """
    The function checks if the current symbol is valid (supported by the calculator)
    :param symbol: symbol in the equation
    :return: True if the symbol is valid, False otherwise
    """
    return symbol.isdigit() or symbol in OPERATORS + BRACKETS + DOT


def is_valid_dot(equation_str: str, index: int) -> bool:
    """
    The function checks if the current symbol is a valid dot.
    :param equation_str: string of the equation
    :param index: index of the space / tab
    :return: True if the dot is valid, False otherwise
    """
    # incase 12. is invalid:
    return index < len(equation_str) - 1 and equation_str[index + 1].isdigit()


def are_valid_brackets(equation_str: str, ) -> bool:
    """
    The function checks for missing brackets in the equation.
    :param equation_str: string of the equation
    :return: True if the brackets are valid, False for missing brackets
    """
    bracket_count = 0
    for symbol in equation_str:
        # A closing bracket was placed before an opening one (missing an opening bracket)
        if bracket_count < 0:
            return False
        # Counts opening and closing brackets in the equation ( adds one for opening ones and subs one for opening ones)
        if symbol == BRACKETS[0]:
            bracket_count += 1
        if symbol == BRACKETS[1]:
            bracket_count -= 1
    # Checks for missing bracket (missing closing brackets)
    return bracket_count == 0
