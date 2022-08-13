"""
this is an optional test suite

you can download the getid3 testfiles by calling

$ make download_getid3_testfiles

this will download all the files required for the extended testsuite
"""
import itertools
import os
import pytest
from tinytag import TinyTag
from pathlib import Path

testpath = Path(os.path.join(os.path.dirname(__file__), 'getid3'))
print(list(testpath.iterdir()))


def traverse(path):
    retval = []
    for file in path.iterdir():
        if file.is_dir():
            retval += traverse(file)
        else:
            retval.append(file.absolute())
    return retval

testfiles = traverse(testpath)

@pytest.mark.parametrize("testfile", [
    pytest.param(testfile) for testfile in testfiles if TinyTag.is_supported(testfile)
])
def test_file_reading(testfile):
    filename = testfile
    tag = TinyTag.get(filename)
