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
To exit, please enter: EXIT\n
"""
__ALL__ = ["get_equation", "display_wellcome_msg", "show_solution"]


def get_equation() -> str:
    return input("Please enter your equation: ")


def display_wellcome_msg():
    print(WELLCOME_MSG)


def display_info(info: str):
    print(info)
