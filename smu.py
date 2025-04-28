#!/usr/bin/env python3

import sys
import re
import fixlist

def make_body(content: str) -> str:
    res = ""
    for line in content.split("\n"):
        print(line)
        cn = "normal"
        content = line
        if re.match(r"^![a-zA-Z] ", line):
            match line[1]:
                case "b":
                    cn = "bold"
                case "q":
                    cn = "quote"
            content = line[3:]
        content = content.strip()
        res +=f"<div class=\"{cn}\">{content}</div>\n"
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
'''


def make_footer() -> str:
    return r"""</body>
</html>"""


if __name__ == "__main__":
    if len(sys.argv) < 3:
        raise Exception("Missing input or output file")
    with open(sys.argv[1], "rt", encoding="utf-8") as iF, open(sys.argv[2], "wt", encoding="utf-8") as oF:
        oF.write(make_header(True))
        oF.write(
                "".join(make_body(iF.read()).split("\n").map(lambda s: "    " + s + "\n"))
        )
        oF.write(make_footer())
