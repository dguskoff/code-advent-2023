def part_1():
    file_contents = open("Data/_9_1.txt", "r")
    lines_raw = file_contents.readlines()
    report_raw = [x.strip() for x in lines_raw]
    ans = 0
    i = 0
    for line in report_raw:
        values = [int(x) for x in line.split()]
        dummy = dive(values)
        ans += dummy
        i += 1
        if i == 74:
            print(values)
            print(dummy)
    print(ans)


def dive(the_list):
    deeper = 0
    new_list = []
    for i in range(len(the_list) - 1):
        value = the_list[i + 1] - the_list[i]
        new_list.append(value)
        deeper += value

    if deeper == 0:
        return the_list[0]
    else:
        return dive(new_list) + the_list[-1]


part_1()
