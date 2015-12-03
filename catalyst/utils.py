import six
import hashlib
import json



class _StatusContext(object):
    def __init__(self, message):
        self.message = message

    def __enter__(self):
        six.print_(self.message, end='...')

    def __exit__(self, exc_type, exc_val, exc_tb):
        if exc_val is None:
            six.print_(" done")
        else:
            six.print_(" FAILED")


def status(message):
    return _StatusContext(message)


def info_hash(info):
    return hashlib.sha1(json.dumps(info, sort_keys=True).encode('utf-8')).hexdigest()


def make_hashable(obj):
    if isinstance(obj, dict):
        return (
            (key, make_hashable(obj[key]))
            for key in sorted(obj.keys())
        )
    elif isinstance(obj, (tuple, list)):
        return tuple(
            make_hashable(item)
            for item in obj
        )
    else:
        return obj
