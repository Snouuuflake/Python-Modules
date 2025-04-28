#!/usr/bin/env python3

import sys
import re
import sens_1_0_0

sens_1_0_0.fix_list()


def make_body(content: str) -> str:
    def make_href(s):
        return f'href="{s}"' if s else ""

    res = ""
    for line in content.split("\n"):
        print(line)
        cn = "normal"
        tag = "div"
        content = line
        href = None
        if re.match(r"^![a-zA-Z] ", line):
            match line[1]:
                case "b":
                    cn = "bold"
                case "q":
                    cn = "quote"
                case "t":
                    cn = "title"
                case "l":
                    cn = "minilink link"
                    tag = "a"
                    href = content
            content = line[3:]
        content = content.strip()
        res += f"<{tag} class=\"{cn}\" {make_href(href)}>{
            content}</{tag}>\n"
    return res


def make_header(css: bool) -> str:
    return r'''
<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<meta http-equiv="X-UA-Compatible" content="ie=edge">
    ''' + ((r'<style>' + make_css() + '</style>') if css else '') + r'''
</head>
<body>'''


def make_css() -> str:
    return r'''
:root {
--sky: #04a5e5;
}
body
{
font-family: 'Helvetica', 'Arial', sans-serif;
font-size: 14pt;
}
div {
min-height: 0.5em;
}
.bold {
font-weight: bold;
}
.normal {
color: rgb(100,100,100);
}
.quote {
color: rgb(150,150,150);
text-align: center;
padding: 0.5em 1em;
}
.title {
font-size: 20pt;
font-weight: bold;
}
.minilink {
color: var(--sky);
font-size: 11pt;
}
'''


def make_footer() -> str:
    return r"""
    </body>
</html>"""


def main(i: str, o: str):
    with open(i, "rt", encoding="utf-8") as iF, open(o, "wt", encoding="utf-8") as oF:
        oF.write(make_header(True))
        oF.write(
            "".join(make_body(iF.read()).split(
                "\n").map(lambda s: "    " + s + "\n"))
        )
        oF.write(make_footer())


if __name__ == "__main__":
    if len(sys.argv) < 3:
        raise Exception("Missing input or output file")
    main(sys.argv[1], sys.argv[2])
