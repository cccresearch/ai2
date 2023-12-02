import re
from datetime import datetime, timedelta
import calendar

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


def now():
    t = datetime.now()
    return f"{t.strftime('%m/%d/%Y, %H:%M:%S')} {calendar.day_name[t.weekday()]}"

# =============== plugin ======================
def system2(question):
    return f"<system2>{question}</system2>"

def memory(datetime, job):
    return f"<memory>{datetime}:{job}</memory>"