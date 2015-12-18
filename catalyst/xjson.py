import json
import iso8601
import io

from datetime import datetime, date


class JsonWriter(object):
    def __init__(self, stream=None, indent="  ", max_indent_depth=3):
        self.stream = stream or io.StringIO()
        self._depth = 0
        self.indent = indent
        self.max_indent_depth = max_indent_depth

    def write_value(self, obj):
        if isinstance(obj, dict):
            self.write_object(obj)
        elif isinstance(obj, (list, tuple)):
            self.write_array(obj)
        else:
            json.dump(obj, self.stream, default=_default)

    def _newline(self, inc=0):
        self._depth += inc
        if (self._depth + max(0, -inc)) <= self.max_indent_depth:
            self.stream.write("\n")
            self.stream.write(self.indent * min(self.max_indent_depth, self._depth))

    def write_object(self, obj):
        self.stream.write("{")
        if len(obj) == 0:
            self.stream.write("}")
            return
        self._newline(1)
        n = len(obj)
        for key, value in obj.items():
            self.write_value(key)
            self.stream.write(": ")
            self.write_value(value)
            n -= 1
            if n > 0:
                self.stream.write(", ")
                self._newline()
        self._newline(-1)
        self.stream.write("}")

    def write_array(self, obj):
        self.stream.write("[")
        if len(obj) == 0:
            self.stream.write("]")
            return
        self._newline(1)
        n = len(obj)
        for value in obj:
            self.write_value(value)
            n -= 1
            if n > 0:
                self.stream.write(", ")
                self._newline()
        self._newline(-1)
        self.stream.write("]")


def _default(obj):
    if isinstance(obj, datetime):
        return {'$datetime': obj.isoformat()}
    elif isinstance(obj, date):
        return {'$date': obj.isoformat()}
    else:
        return obj


def _object_hook(obj):
    if len(obj) == 1:
        key, = obj.keys()
        if key == '$datetime':
            return iso8601.parse_date(obj[key])
        elif key == '$date':
            return iso8601.parse_date(obj[key]).date()
    return obj


def dump(obj, f):
    jw = JsonWriter(f)
    jw.write_value(obj)


def dumps(obj):
    jw = JsonWriter()
    jw.write_value(obj)
    return jw.stream.getvalue()


def loads(*args, **kwargs):
    return json.loads(*args, object_hook=_object_hook, **kwargs)


def load(*args, **kwargs):
    return json.load(*args, object_hook=_object_hook, **kwargs)