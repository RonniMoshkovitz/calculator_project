WELLCOME_MSG = """
Wellcome to the ADVANCED OMEGA CALCULATOR!\n
This calculator supports the following operations:\n
\t# +: addition, in form of <operand>+<operand>\n
\t# -: submission, in form of <operand>-<operand>\n
\t# *: multiplication, in form of <operand>*<operand>\n
\t# /: division, in form of <operand>/<operand>\n
\t# ^: power, in form of <operand>^<operand>\n
\t# $: maximum, in form of <operand>$<operand>\n
\t# &: minimum, in form of <operand>&<operand>\n
\t# @: average, in form of <operand>@<operand>\n
\t# %: module, in form of <operand>%<operand>\n
\t# ~: negative, in form of ~<operand>\n
\t# !: factorial, in form of <operand>!\n
\n
To display the menu again, please enter: Menu\n
To exit, please enter: EXIT\n
"""


def get_equation() -> str:
    equation = ""
    try:
        equation = input("Please enter your equation: ")
    except EOFError as e:
        display_info(e)
        exit(1)

    return equation


def display_wellcome_msg():
    print(WELLCOME_MSG)


def display_info(info: str or Exception):
    print(info)


def display_solution(equation: str, solution: float):
    display_info(f"{equation} = {solution}")

