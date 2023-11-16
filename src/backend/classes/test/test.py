import re

test_expresion = """
1d20

2d20

15d20
"""



if __name__ == '__main__':
    regx = r'(\d+)(d)(\d+)'
    matches = re.findall(regx, test_expresion)
    print(f"{len(matches)=}")
