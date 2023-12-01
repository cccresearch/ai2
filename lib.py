import re

def run(code):
    try:
        if code.find('\n')!=-1: raise
        exec(f'_rrr999={code}')
        return str(eval('_rrr999'))
    except:
        return f"<run>{code}</run>"

def replace_code(text):
    parts = []
    last_idx = 0

    for m in re.finditer("<python>(.*?)</python>", text):
        parts.append(text[last_idx:m.start()])
        code = m.group(1)
        parts.append(run(code))
        last_idx = m.end()

    parts.append(text[last_idx:])
    return ''.join(parts)
