import re

def replace_code(text):
    parts = []
    last_idx = 0

    for m in re.finditer("<python>(.*?)</python>", text):
        parts.append(text[last_idx:m.start()])
        code = m.group(1)
        parts.append(str(eval(code)))
        last_idx = m.end()

    parts.append(text[last_idx:])
    return ''.join(parts)
