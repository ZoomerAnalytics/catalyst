import io
import re
from datetime import datetime

DATETIME_LITERAL = re.compile("[0-9]{4}-[0-9]{2}-[0-9]{2}T[0-9]{2}:[0-9]{2}:[0-9]{2}")
NUMERIC_LITERAL = re.compile("[-+]?[0-9]*\.?[0-9]+([eE][-+]?[0-9]+)?")

class Item(object):
    def __init__(self, values, *items):
        self.values = list(values)
        self.items = list(items)


def _string(line, pos):
    s = ""
    if line[pos] != '"':
        return pos, None
    pos += 1
    while line[pos] != '"':
        if line[pos] == '\\':
            pos += 1
            s += {
                't': '\t',
                '\\': '\\',
                'n': '\n',
                '"': '"',
            }[line[pos]]
            pos += 1
        else:
            s += line[pos]
            pos += 1
    pos += 1
    return pos, s


def _number(line, pos):
    m = NUMERIC_LITERAL.match(line, pos)
    if m is None:
        return pos, None
    l = m.endpos - m.pos
    n = float(line[pos:pos+l])
    return pos + l, n


def _datetime(line, pos):
    m = DATETIME_LITERAL.match(line, pos)
    if m is None:
        return pos, None
    l = m.endpos - m.pos
    dt = datetime.strptime(line[pos:pos+l], "%Y-%m-%dT%H:%M:%S")
    return pos + l, dt


def _object(line, pos):
    pos, obj = _string(line, pos)
    if obj is not None:
        return pos, obj
    pos, obj = _datetime(line, pos)
    if obj is not None:
        return pos, obj
    pos, obj = _number(line, pos)
    if obj is not None:
        return pos, obj
    if line.startswith("true"):
        return pos+4, True
    if line.startswith("false"):
        return pos+5, False
    if line.startswith("null"):
        return pos+4, None
    raise Exception("Could not parse value")


def _values(line, pos):
    values = []
    while pos < len(line):
        pos, s = _object(line, pos)
        values.append(s)
        assert pos == len(line) or line[pos] == ' '
        pos += 1
    return values

def _load(lines, pos, items, indent):
    p_indent = len(indent)
    while pos < len(lines):
        line = lines[pos].rstrip()
        if line:
            if line.startswith(indent):
                if line[p_indent] in ('\t', ' '):
                    p = p_indent
                    while line[p] in ('\t', ' '):
                        p += 1
                    pos = _load(lines, pos, items[-1].items, line[:p])
                else:
                    items.append(Item(_values(line, p_indent)))
                    pos += 1
            else:
                return pos
    return pos


def _fmt(v):
    if v is None:
        return "null"
    if isinstance(v, datetime):
        return v.strftime("%Y-%m-%dT%H:%M:%S")
    if isinstance(v, str):
        return '"' + repr(v)[1:-1] + '"'
    if isinstance(v, (int, float)):
        return repr(v)
    if v:
        return "true"
    else:
        return "false"


def load(f):
    return loads(f.read())


def loads(s):
    lines = s.splitlines()

    items = []
    _load(lines, 0, items, "")
    return items


def _dump(f, items, indent):
    for i in items:
        f.write(indent)
        f.write(" ".join(_fmt(v) for v in i.values))
        f.write("\n")
        _dump(f, i.items, indent + "\t")


def dump(items, f):
    _dump(f, items, "")


def dumps(items):
    with io.StringIO() as f:
        _dump(f, items, "")
        return f.getvalue()


if __name__ == "__main__":
    loads(
        """hello
            abc
            def
        goodbye"""
    )