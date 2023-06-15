import os
import sys
import json
from function import handler

def get_stdin():
    buf = ""
    while(True):
        line = sys.stdin.readline()
        buf += line
        if not line.strip("\n"):
            break
    return buf

if(__name__ == "__main__"):
    st = get_stdin()
    inputs = json.loads(st)

    if isinstance(inputs, str):
        inputs = {"inputs": inputs}
    elif isinstance(inputs, Dict):
        assert "inputs" in inputs
    else:
        raise Exception("inputs should either be a str or a dict.")

    ret = handler.query(inputs)
    if ret != None:
        print(ret)
