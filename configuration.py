# priority dict:
OPERATORS_PRIORITY = {"+": 1,
                      "-": 1,
                      "*": 2,
                      "/": 2,
                      "^": 3,
                      "%": 4,
                      "$": 5,
                      "&": 5,
                      "@": 5,
                      "~": 6,
                      "!": 6,
                      "#": 6}

# supported chars:
BRACKETS = "()"
OPERATORS = "".join(OPERATORS_PRIORITY.keys())
MINUS_SIGN = "-"
DOT = "."
