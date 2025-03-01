index = 1
while True:
    rst = 0
    texts = input()

    if texts[0] == "-":

        break

    while texts.count("{}") > 0:
        texts = texts.replace("{}", "")

    while texts.count("{{") > 0:

        rst += 1
        texts = texts.replace("{{", "", 1)
    while texts.count("}}") > 0:

        rst += 1
        texts = texts.replace("}}", "", 1)
    while texts.count("}{") > 0:

        rst += 2
        texts = texts.replace("}{", "")

    print(f"{index}.", rst)
    index += 1
