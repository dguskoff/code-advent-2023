import re


def replace_by_index(string, idx, character):
    return string[:idx] + character + string[idx + 1 :]


x_num = 0


def get_char(char, line, ind):
    global x_num
    if char == "." and x_num % 2 != 0:
        return "*"
    elif char == "|":
        x_num += 1
        return "|"
    else:
        return "."


def get_repl_character(char: str, field_row: str, ind: int) -> str:
    global x_num
    if char == "X":
        x_num += 1

    if char == "." and ind == 0 or char == "." and ind == len(field_row) - 2:
        return "O"
    elif char == "." and x_num == 0:
        return "O"
    elif char == "." and x_num != 0 and x_num % 2 == 0:
        return "O"
    elif char == "." and x_num != 0 and x_num % 2 != 0:
        res = re.search("X", field_row[ind:])
        if res is None:
            return "O"
        else:
            return "I"
    else:
        return char


with open("Data/_10_t2.txt") as f:
    field = f.readlines()
    S = [(ind, l.find("S")) for ind, l in enumerate(field) if "S" in l][0]
    field[S[0]] = replace_by_index(field[S[0]], S[1], "F")

    total_inside = 0
    for ind, line in enumerate(field):
        x_num = 0
        if ind != 0 and ind < len(field) - 1:
            new_ine = res = re.sub(r"F-+7", "", line)
            new_ine = res = re.sub(r"F7", "", new_ine)
            new_ine = res = re.sub(r"L-+J", "", new_ine)
            new_ine = res = re.sub(r"LJ", "", new_ine)
            new_ine = res = re.sub(r"F-+J", "|", new_ine)
            new_ine = res = re.sub(r"FJ", "|", new_ine)
            new_ine = res = re.sub(r"L-+7", "|", new_ine)
            new_ine = res = re.sub(r"L7", "|", new_ine)
            new_ine = res = re.sub(r"-+7", ".", new_ine)

            s = "".join([get_char(c, new_ine, i) for i, c in enumerate(new_ine)])

            total_inside += len(re.findall(r"\*", s))

            field[ind] = s

            print(s)

    print(f"Total Is : {total_inside}")
