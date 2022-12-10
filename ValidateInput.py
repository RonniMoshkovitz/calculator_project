from configuration import *
from InputOutput import *

"""
validates the entered string, to start pars
"""


def validate_input(equation_str: str) -> str:
    """
    The function removes extra minus signs, spaces and tabs and checks for invalid chars in the equation input string.
    It treats invalid input if needed (for invalid symbols, dots, or missing brackets).
    :param equation_str: input equation
    :return: validated string equation (the input equation without extra minus signs, spaces and tabs)
    """
    # Removes extras
    equation_str = remove_extra_spaces(equation_str)
    equation_str = remove_extra_minus_signs(equation_str)

    # Checks for invalid symbols in the equation, may raise an exception accordingly
    try:
        check_validity(equation_str)
    except Exception as e:
        display_info(e)
        exit(1)

    return equation_str


def check_validity(equation_str: str):
    """
    Checks for invalid symbols in the equation string. It raises an exception if an invalid symbol is found,
    or a dot is located in an invalid location, or if there are missing brackets.
    :param equation_str: string of the equation
    """
    for i, symbol in enumerate(equation_str):

        # Checks for invalid symbols
        if not is_valid_symbol(symbol):
            raise Exception(f"the symbol: {symbol} in index: {i} is not supported.")

        # Checks for invalid dots
        if symbol is DOT and not is_valid_dot(equation_str, i):
            raise Exception(f"invalid dot in index: {i}, dots cant be next to one another or without a digit behind")

    # Checks for misplaced or missing brackets
    if not are_valid_brackets(equation_str):
        raise Exception(f"brackets are invalid. missing matching bracket")


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
